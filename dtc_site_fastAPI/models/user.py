from db import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, string_length=150, unique=True)
    password = Column(String, string_length=128, nullable=False)

    rel_image_feed = relationship('ImageFeed', back_populates='rel_image_feed')
