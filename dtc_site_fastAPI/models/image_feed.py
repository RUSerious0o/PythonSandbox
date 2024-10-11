from db import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class ImageFeed(Base):
    __tablename__ = 'imagefeeds'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image = Column(String, nullable=False, string_length=100)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    processed_image = Column(String, string_length=100, nullable=True)

    rel_image_feed = relationship('User', back_populates='rel_image_feed')
    rel_detected_object = relationship('DetectedObject', back_populates='rel_detected_object')
