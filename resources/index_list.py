from resources.mongodb import MongoManager

class IndexListManager(MongoManager):
    def __init__(self):
        super().__init__("omt-index-list", "index-list")
        pass

    def generate_id(self, doc={}):
        joint_string = ':'
        indexes = doc.get('indexes', '')
        return '{}:{}'.format(super().generate_id(),joint_string.join(indexes)) 