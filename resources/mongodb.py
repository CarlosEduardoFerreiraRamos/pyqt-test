import pymongo
import json
import datetime

from typing import  List
from pymongo.database import Database
from pymongo.collection import Collection

from bson import json_util
from bson.objectid import ObjectId


from models.indexed_file import IndexedFile
from configuration.manager import ConfigurationManager, ConfigProp

class MongoManager:
    def __init__(self, db_name, collection_name):
        self.__db_adress = ConfigurationManager.get_config_value(ConfigProp.db_name())
        self.__db_name = db_name
        self.__collection_name = collection_name

    def find_one(self) ->  dict:
        return self.__find_one()

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

    def __find(self) -> List:
        self.__connect()
        collection = self.__get_collection()
        listed = list(collection.find())
        self.__close()
        return listed

    def __find_one(self) -> dict:
        self.__connect()
        entry = self.__get_collection().find_one()
        self.__close()
        return entry

    def __delete(self, id) -> bool:
        self.__connect()
        result = self.__get_collection().delete_one({'_id': str(ObjectId(id))})
        self.__close()
        return result.deleted_count is not 0

    def __update(self, id, doc: dict) -> bool:
        self.__connect()
        result = self.__get_collection().update_one({'_id':str(ObjectId(id))}, {'$set': doc})
        self.__close()
        return result.modified_count is not 0

    def __save(self, doc: dict) -> str:
        doc.update({'_id': self.generate_id(doc), 'created': self.generate_date()})
        self.__connect()
        result = self.__get_collection().insert_one(doc)
        self.__close()
        return result.inserted_id

    def __get_db(self) -> Database:
        return self.client[self.__db_name]

    def __get_collection(self) -> Collection:
        return self.__get_db()[self.__collection_name]

    def __close(self) -> None:
        self.client.close()

    def __connect(self) -> None:
        self.client = pymongo.MongoClient(self.__db_adress)
