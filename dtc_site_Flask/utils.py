from flask_login import current_user
from flask_login.mixins import AnonymousUserMixin

import random
import os

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