from db import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, BigInteger
from sqlalchemy.orm import relationship


class DetectedObject(Base):
    __tablename__ = 'detectedobjects'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    object_type = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=False)
    location = Column(String(255), nullable=False)
    image_feed_id = Column(BigInteger, ForeignKey('imagefeeds.id'), nullable=False)

    rel_detected_object_obj = relationship('ImageFeed', back_populates='rel_detected_object_feed')
