from sqlalchemy.orm import sessionmaker
from typing import  List

from databases import PostgresManager,db_engine
from models import Entity

class EntityManager(PostgresManager):
    def __init__(self):
        super().__init__(sessionmaker(db_engine), Entity)
        pass

    # def find_one(self, id: str) ->  dict:
    #     result = super().find_one(id)
    #     if result is not None:
    #         return result.name 
    #     return result

    # def find(self) -> List:
    #     result = super().find()
    #     if result is not None:
    #         return list(map( lambda e: e.name, result)) 
    #     return result

