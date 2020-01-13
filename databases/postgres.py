
from sqlalchemy.orm import sessionmaker, Session, Query
from typing import  List
import datetime

# from sqlalchemy import Table, Column, String, Integer, MetaData,Date
# from sqlalchemy.ext.declarative import declarative_base  
# from sqlalchemy import create_engine  
"""
db_string = 'postgresql+psycopg2://postgres:root@localhost/'
# db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"


db = create_engine(db_string) 


base = declarative_base()

class Entity(base):  
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    token = Column(String)
    created = Column(Date)

s: Session = sessionmaker(db)
session = s()


first = Entity( name='adminTwo', email='admin@gmail', password="123")


session.add(first)
session.commit()

base.metadata.create_all(db)
session.query(Entity)
for e in session.query(Entity):
    print(e.name)
"""

class PostgresManager:

    def __init__(self, db_sessionmaker, orm):
        self.__sessionmaker = db_sessionmaker
        self.__orm = orm
        self.session: Session

    def find_one(self, id: str) ->  dict:
        return self.__find_one(id)

    def find(self) -> List:
        return self.__find()

    def save(self, doc: dict) -> str:
        return self.__save(doc)

    def update(self, id, doc: dict) -> bool:
        return self.__update(id, doc)

    def delete(self, id) -> bool:
        return self.__delete(id)

    def generate_id(self, doc={}):
        return ObjectId()

    def generate_date(self):
        return datetime.datetime.utcnow()

    def treat_id(self, id: str):
        return re.compile(id)

    def __find(self) -> List:
        self.__connect()
        listed = self.__query().all()
        # temporary treatment - start
        if listed is not None:
            listed = list(map(lambda e: e.__dict__, listed))
        # end
        self.__close()
        return listed

    def __find_one(self, id: str) -> dict:
        self.__connect()
        entity = self.__query().filter(self.__orm.id == id).first()
        # temporary treatment - start
        if entity is not None:
            entity = entity.__dict__ 
        # end
        self.__close()
        return entity

    def __delete(self, id: str) -> bool:
        self.__connect()
        result = self.__query().filter(self.__orm.id == id).delete()
        self.__close()
        return result is not 0

    def __update(self, id: str, doc: dict) -> bool:
        self.__connect()
        result = self.__query().filter(self.__orm.id == id).update(doc)
        self.__close()
        return result is not 0

    def __save(self, doc: dict) -> str:
        doc.update({'created': self.generate_date()})
        orm_doc = self.__orm(**doc)
        self.__connect()
        self.__get_session().add(orm_doc)
        # temporary treatment - start
        self.session.commit()
        result = orm_doc.id 
        # end
        self.__close()
        return result

    def __get_session(self) -> Session:
        return self.session

    def __query(self) -> Query:
        return self.__get_session().query(self.__orm)

    def __close(self) -> None:
        self.session.commit()
        self.session.close()

    def __connect(self) -> None:
        self.session = self.__sessionmaker()


