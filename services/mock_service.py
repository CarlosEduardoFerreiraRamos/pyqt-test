from flask import request
from flask_restful import Resource

from resources.index_list import IndexListManager
from managers import MockManager

class MockService(object):
    def __init__(self):
        self.service: MockManager = MockManager()

    def build_questions(self, file_path: list, folder_path: str):
        self.service.config_save_forder = folder_path
        response = self.service.build_questions(file_path)
        return response
    

class Question(Resource):

    def __init__(self):
        super().__init__()
        self.manager  = IndexListManager()

    def get(self, id=None) ->  int:
        if id is not None:
            return self.manager.find_one(id)
        else:
            return self.manager.find()

    def put(self, id) -> int:
        data = request.get_json()
        return self.manager.update(id, data)

    def post(self) -> int:
        data = request.get_json()
        return self.manager.save(data)
    
    def delete(self, id=None) -> int:
        return self.manager.delete(id)

class QuestionList(Resource):

    def __init__(self):
        super().__init__()
        self.manager  = IndexListManager()

    def get(self, id=None):
        print(id)
        if id is not None:
            return self.manager.find_one()
        else:
            return self.manager.find()
    
        
    

