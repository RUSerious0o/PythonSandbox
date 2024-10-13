from main import db


class ImageFeed(db.Model):
    __tablename__ = 'imagefeeds'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    image = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    processed_image = db.Column(db.String(100), nullable=True)

    rel_image_feed_feed = db.relationship('User', back_populates='rel_image_feed_user')
    rel_detected_object_feed = db.relationship('DetectedObject', back_populates='rel_detected_object_obj')
