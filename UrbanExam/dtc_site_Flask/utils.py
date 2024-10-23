import cv2
import numpy as np
from flask_sqlalchemy import SQLAlchemy
import os
import random

from flask_login import current_user
from flask_login.mixins import AnonymousUserMixin


VOC_LABELS = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle",
    "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]


def process_image(
        image_id: int,
        image_path: str,
        processed_image_dir: str,
        db: SQLAlchemy,
        detected_object
) -> str:
    try:
        model_path = 'mobilenet_iter_73000.caffemodel'
        config_path = 'mobilenet_ssd_deploy.prototxt'
        net = cv2.dnn.readNetFromCaffe(config_path, model_path)

        print(image_path)
        img = cv2.imread(image_path)
        if img is None:
            print("Failed to load image")
            return ''

        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.6:
                class_id = int(detections[0, 0, i, 1])
                class_label = VOC_LABELS[class_id]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
                label = f"{class_label}: {confidence:.2f}"
                cv2.putText(img, label, (startX+5, startY + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                detected_object.object_type = class_label
                detected_object.location = f"{startX},{startY},{endX},{endY}"
                detected_object.confidence = float(confidence)

                db.session.add(detected_object)

        image_path = os.path.split(image_path)
        processed_image_path = os.path.join(
            processed_image_dir,
            f'processed_{image_path[1]}'
        )

        cv2.imwrite(filename=processed_image_path, img=img)
        db.session.commit()

        return processed_image_path

    except:
        print("Something went wrong! Image procession failed!")
        raise


def is_logged_in() -> bool:
    return not isinstance(current_user, AnonymousUserMixin)


def check_login(login_: str) -> bool:
    login_ = login_.lower()
    vocab = 'qwertyuiopasdfghjklzxcvbnm@.+-_'
    for letter in login_:
        if letter not in vocab:
            return False
    return True


def generate_filepath(folder_path: str, filename: str) -> str:
    code_ = ''.join([random.choice("abcdefghijklmnopqrstuvw123456789" if i != 5 else "ABCDEFGHIJKLMNOPQRSTUVW123456798") for i in range(8)])
    filename = filename.split('.')
    filename = f'{filename[0]}_{code_}.{filename[1]}'
    return os.path.join(folder_path, filename)