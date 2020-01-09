from flask_restful import Resource
from flask import request

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