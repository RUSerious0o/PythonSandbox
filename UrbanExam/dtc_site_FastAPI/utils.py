import cv2
import numpy as np
from typing import Annotated
from fastapi import Depends
from sqlalchemy import insert, update
from sqlalchemy.orm import Session
import os

from models import DetectedObject, ImageFeed
from db import get_db


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
        db: Annotated[Session, Depends(get_db)]
):
    try:
        model_path = 'mobilenet_iter_73000.caffemodel'
        config_path = 'mobilenet_ssd_deploy.prototxt'
        net = cv2.dnn.readNetFromCaffe(config_path, model_path)

        img = cv2.imread(image_path)
        if img is None:
            print("Failed to load image")
            return False

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

                db.execute(insert(DetectedObject).values(
                    image_feed_id=image_id,
                    object_type=class_label,
                    location=f"{startX},{startY},{endX},{endY}",
                    confidence=float(confidence)
                ))

        image_path = os.path.split(image_path)
        processed_image_path = os.path.join(
            processed_image_dir,
            f'processed_{image_path[1]}'
        )
        cv2.imwrite(filename=processed_image_path, img=img)

        db.execute(update(ImageFeed).
                   values(processed_image=processed_image_path).
                   where(ImageFeed.id == image_id))
        db.commit()

        return True

    except:
        print("Something went wrong! Image procession failed!")
        raise
