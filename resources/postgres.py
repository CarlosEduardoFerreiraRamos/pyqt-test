
from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Numeric
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

from configuration.manager import ConfigurationManager, ConfigProp


db_string = 'postgresql+psycopg2://postgres:root@localhost/'
# db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"


db = create_engine(db_string)  
base = declarative_base()

class Entity(base):  
    __tablename__ = 'entity'

    id = Column(Numeric, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    token = Column(String)

Session = sessionmaker(db)  
session = Session()


first = Entity(id=10, name='admin', email='admin@gmail', password="123")

session.add(first)
session.commit()

base.metadata.create_all(db)
session.query(Entity)
for e in session.query(Entity):
    print(e.name)


class PostgresManager:

    def __init__(self, db_name, collection_name):
        self.__db_adress = ConfigurationManager.get_config_value(ConfigProp.db_name())
        self.__db_name = db_name
        self.__collection_name = collection_name

