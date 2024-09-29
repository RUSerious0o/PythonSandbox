from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(url='sqlite:///taskmanager.db', echo=True)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
