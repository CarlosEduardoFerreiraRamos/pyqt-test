import pymongo
# self.__db.adress = "mongodb+srv://carlos_ramos:{}@omt-index-list-nzg4v.mongodb.net/omt-index-list?retryWrites=true&w=majority".format("HVmachine85")
class MongoManager:
    def __init__(self, db_name, collection_name):
        self.__db_adress = "localhost:27017"
        self.__index_list_db_name = db_name
        self.__index_list_name = collection_name
    
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
        self.client[self.__index_list_db_name]

    def __get_collection(self):
        return self.__get_db(self.__index_list_db_name)
