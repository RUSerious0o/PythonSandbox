from main import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    rel_image_feed_user = db.relationship('ImageFeed', back_populates='rel_image_feed_feed')