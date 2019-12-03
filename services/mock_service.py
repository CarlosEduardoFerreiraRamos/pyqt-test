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
            return self.manager.find_one()
        else:
            return self.manager.find()

    def put(self, id) -> int:
        print(request.form.get('data'))
        return {'value': 'updated'}, 200

    def post(self) -> int:
        print(request.form.get('data'))
        return {'value', 'created'}, 200
    
    def delete(self, id) -> int:
        print(request.form.get('data'))
        return {'value': 'deleted'}, 200
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
    
        
    

