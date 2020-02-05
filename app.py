import sys
import os
import re
import json

from docx import Document
from waitress import serve

""" Flask moduels """
from flask import Flask, make_response, request
from flask.json import JSONEncoder, JSONDecoder
from flask_restful import Api

"""internal modules """

""" Must start first"""
import configuration
import databases
import auth
import models
import resources

from auth import auth_user
from services import MockService, Question as QuestionService, QuestionList,EntityService
from util import get_command_prop  

ms = MockService()
app = Flask(__name__)
api = Api(app)

# TODO: JSON encoder and encoder setting
# class CustomJSONEncoder(JSONEncoder):
#     """ Do nothing custom json encoder """
#     def __init__(self, *args, **kargs):
#         super()

#     def default(self, obj):
#         print(' JSONEncoder',obj)
#         return super().default(obj)


# class CustomJSONDecoder(JSONDecoder):
#     """ Do nothing custom json decoder """

#     def decode(self, d):
#         print(' JSONDecoder',d)
#         return super().decode(d)

# app.json_encoder = CustomJSONEncoder
# app.json_decoder = CustomJSONDecoder 

# @app.url_defaults
# def add_language_code(*args):
#     print(' url_defaults',args)

# @app.url_value_preprocessor
# def pull_lang_code(*args):
#     print(' url_value_preprocessor',args)

@app.before_request
def protect():
    token = request.headers.get('Authorization', ' ').split(' ')[1]
    user = auth_user(token)
    print('user',user)
    if user is None:
        return make_response({'auth_error': 'auth fail'},401)
    pass


@api.representation('application/json')
def output_json(data, code, headers=None):
    print('in  output_json',data, code, headers)
    resp = make_response(json.dumps(data, indent=4, sort_keys=True, default=str), code)
    resp.headers.extend(headers or {})
    return resp

api.add_resource(QuestionService, '/','/question','/question/<string:id>' )
api.add_resource(QuestionList,'/list', '/list/<int:id>')
api.add_resource(EntityService,'/auth', '/auth/<int:id>')

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port, expose_tracebacks=False, url_scheme='https')