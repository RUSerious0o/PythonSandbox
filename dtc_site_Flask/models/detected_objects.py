from main import db


class DetectedObject(db.Model):
    __tablename__ = 'detectedobjects'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    object_type = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    image_feed_id = db.Column(db.BigInteger, db.ForeignKey('imagefeeds.id'), nullable=False)

    rel_detected_object_obj = db.relationship('ImageFeed', back_populates='rel_detected_object_feed')
