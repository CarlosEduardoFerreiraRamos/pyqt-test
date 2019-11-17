from resources.mongodb import MongoManager

class IndexListManager(MongoManager):
    def __init__(self):
        super().__init__("omt-index-list", "index-list")
        pass
