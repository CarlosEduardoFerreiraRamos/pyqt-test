import pymongo

from configuration.manager import ConfigurationManager, ConfigProp

class MongoManager:
    def __init__(self, db_name, collection_name):
        self.__db_adress = ConfigurationManager.get_config_value(ConfigProp.db_name())
        self.__db_name = db_name
        self.__collection_name = collection_name
    
    def find_one(self):
        return self.__find_one()

    def find(self):
        return self.__find()

    def __find(self):
        self.__connect()
        collection = self.__get_collection()
        listed = list(collection.find())
        self.__close()
        return listed

    def __find_one(self):
        self.__connect()
        entry = self.__get_collection().find_one()
        self.__close()
        return entry

    def __get_db(self):
        return self.client[self.__db_name]

    def __get_collection(self):
        v = self.__get_db()
        print(v)
        return v[self.__collection_name]

    def __close(self) -> None:
        self.client.close()

    def __connect(self) -> None:
        self.client = pymongo.MongoClient(self.__db_adress)
