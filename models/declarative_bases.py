from databases import Base
from sqlalchemy import Table, Column, String, Integer, MetaData,Date

class Entity(Base):  
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    token = Column(String)
    created = Column(Date)

