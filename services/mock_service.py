from managers import MockManager
from flask import request
from flask_restful import Resource

class MockService(object):
    def __init__(self):
        self.service: MockManager = MockManager()

    def build_questions(self, file_path: list, folder_path: str):
        self.service.config_save_forder = folder_path
        response = self.service.build_questions(file_path)
        return response
    

class Question(Resource):

    def get(self) ->  int:
        print('has being sent')
        # value =  request.form['body']
        # self.service.config_save_forder = value
        return {'body': 'teste'}, 200
        # return self.service.build_questions(file_path), 200 

