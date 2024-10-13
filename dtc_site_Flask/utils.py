from flask_login import current_user
from flask_login.mixins import AnonymousUserMixin


def is_logged_in() -> bool:
    return not isinstance(current_user, AnonymousUserMixin)


def check_login(login_: str) -> bool:
    login_ = login_.lower()
    vocab = 'qwertyuiopasdfghjklzxcvbnm@.+-_'
    for letter in login_:
        if letter not in vocab:
            return False
    return True
