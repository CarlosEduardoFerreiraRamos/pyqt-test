from flask_restful import Resource
from flask import request

from resources import EntityManager

class User(Resource):

    def __init__(self):
        super().__init__()
        self.manager  = None
    
    def get(self,id=None):
        pass

    def put(self, id):
        data = request.get_json()
        pass

    def delete(self,id):
        pass

    def post(self):
        data = request.get_json()
    
class EntityService(Resource):
    def __init__(self):
        super().__init__()
        self.manager = EntityManager()
    
    def get(self,id=None):
        if id is not None:
            return self.manager.find_one(id)
        else:
            return self.manager.find()

    def put(self, id):
        data = request.get_json()
        return self.manager.update(id, data)

    def delete(self,id):
        return self.manager.delete(id)

    def post(self):
        data = request.get_json()
        return self.manager.save(data)

