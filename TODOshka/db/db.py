from typing import Tuple, Sequence

from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, select, DateTime
from sqlalchemy import delete, update
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


class DB:
    __DB_URL = 'sqlite:///data.db'

    Base = declarative_base()

    class List(Base):
        __tablename__ = 'lists'

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False, unique=True)

        item = relationship('__Item', back_populates='list', cascade='all, delete', passive_deletes=True)

    class __Item(Base):
        __tablename__ = 'items'

        id = Column(Integer, primary_key=True, autoincrement=True, index=True)
        short_content = Column(String, nullable=False)
        detailed_content = Column(Text, nullable=True)
        deadline = Column(DateTime, nullable=True)
        is_completed = Column(Boolean, nullable=False, default=False)
        list_id = Column(Integer, ForeignKey('lists.id', ondelete='CASCADE'), nullable=True)
        past_usage_list_id = Column(Integer, nullable=False)

        list = relationship('List', back_populates='item')

    def __init__(self):
        self.__engine = create_engine(self.__DB_URL)
        DB.Base.metadata.create_all(self.__engine)
        self.__Session = sessionmaker(bind=self.__engine)

    def add_list(self, list_name: str):
        try:
            session = self.__Session()
            try:
                session.add_all([self.List(name=list_name)])
                session.commit()
            except:
                print(f'List with name {list_name} addition failed!')
        except:
            raise
        finally:
            session.close()

    def add_item(self, list_id: int, item_short_content: str, item_details: str, item_deadline: datetime):
        try:
            session = self.__Session()
            session.add(self.__Item(short_content=item_short_content,
                                    detailed_content=item_details,
                                    deadline=item_deadline,
                                    list_id=list_id,
                                    past_usage_list_id=list_id))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def delete_list(self, list_id: int, list_name: str = None) -> None:
        self.unbind_all_list_items(list_id)
        try:
            session = self.__Session()
            if list_name:
                session.execute(delete(self.List).where(self.List.name == list_name))
            else:
                session.execute(delete(self.List).where(self.List.id == list_id))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def get_all_lists(self):
        try:
            session = self.__Session()
            result = session.query(self.List).all()
            print(result)
        except:
            raise
        finally:
            session.close()

        return result

    def get_items(self, list_id: int):
        try:
            session = self.__Session()
            result = session.query(self.__Item).filter(self.__Item.list_id == list_id).all()
        except:
            raise
        finally:
            session.close()

        return result

    def get_list(self, list_name: str):
        try:
            session = self.__Session()
            result = session.query(self.List).filter(self.List.name == list_name).one()
        except:
            raise
        finally:
            session.close()

        return result

    def get_unique_short_items(self):
        try:
            session = self.__Session()
            # result = session.execute(select(self.__Item.short_content, self.__Item.past_usage_list_id).distinct())
            result = session.query(self.__Item).distinct()
        except:
            raise
        finally:
            session.close()

        return result

    def update_item_short_content(self, item_id: int, item_short_content: str) -> None:
        try:
            session = self.__Session()
            session.execute(update(self.__Item)
                            .where(self.__Item.id == item_id)
                            .values(short_content=item_short_content))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def update_item_details(self, item_id: int, item_details: str) -> None:
        try:
            session = self.__Session()
            session.execute(update(self.__Item)
                            .where(self.__Item.id == item_id)
                            .values(detailed_content=item_details))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def update_item_completed_status(self, item_id: int, item_completion_status: bool) -> None:
        try:
            session = self.__Session()
            session.execute(update(self.__Item)
                            .where(self.__Item.id == item_id)
                            .values(is_completed=item_completion_status))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def unbind_item(self, item_id: int) -> None:
        try:
            session = self.__Session()
            session.execute(update(self.__Item)
                            .where(self.__Item.id == item_id)
                            .values(list_id=None))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def unbind_all_list_items(self, list_id: int) -> None:
        try:
            session = self.__Session()
            session.execute(update(self.__Item)
                            .where(self.__Item.list_id == list_id)
                            .values(list_id=None))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def update_list(self, list_id: int, new_list_name: str, old_list_name: str = None) -> None:
        try:
            session = self.__Session()
            if old_list_name:
                session.execute(update(self.List)
                                .where(self.List.name == old_list_name)
                                .values(name=new_list_name))
            else:
                session.execute(update(self.List)
                                .where(self.List.id == list_id)
                                .values(name=new_list_name))
            session.commit()
        except:
            raise
        finally:
            session.close()
