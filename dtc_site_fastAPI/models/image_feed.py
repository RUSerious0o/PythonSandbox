from db import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class ImageFeed(Base):
    __tablename__ = 'imagefeeds'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    processed_image = Column(String(100), nullable=True)

    rel_image_feed_feed = relationship('User', back_populates='rel_image_feed_user')
    detected_objects = relationship('DetectedObject',
                                    back_populates='image_feed',
                                    cascade='all, delete-orphan')
