from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(url='sqlite:///detection_site.db', echo=True)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
