import pymongo
# self.__db.adress = "mongodb+srv://carlos_ramos:{}@omt-index-list-nzg4v.mongodb.net/omt-index-list?retryWrites=true&w=majority".format("HVmachine85")
class IndexListManager(object):
    def __init__(self):
        self.__db_adress = "localhost:27017"
        self.__index_list_db_name = "omt-index-list"
        self.__index_list_name = "index-list"
        pass

    def get_one(self, paramns):
        self.__connect()
        entry = collection = self.__get_list()
        self.__close()
        return entry

    def get_all(self):
        self.__connect()
        collection = self.__get_list()
        lited_index = list(collection.find())
        self.__close()
        return lited_index

    def __get_list(self) -> None:
        dabase = self.__get_db(self.__index_list_db_name)
        print(dabase[self.__index_list_name])
        return dabase[self.__index_list_name]

    def __get_db(self, db_name):
        return self.client[db_name]

    def __close(self) -> None:
        self.client.close()

    def __connect(self) -> None:
        self.client = pymongo.MongoClient(self.__db_adress)

print("DONE")

manager  = IndexListManager()