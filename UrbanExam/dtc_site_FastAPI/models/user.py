from db import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    rel_image_feed_user = relationship('ImageFeed', back_populates='rel_image_feed_feed')
