import sys
import os
import re
import json

from docx import Document
from waitress import serve

""" Flask moduels """
from flask import Flask, make_response
from flask_restful import Api

"""internal modules """

""" Must start first"""
from configuration import ConfigurationManager, Path

from reader import Reader
from models import Question, ConfigProp
from services import MockService, Question as QuestionService, QuestionList
from util import get_command_prop  

ms = MockService()
app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    print('in  output_json',data, code, headers)
    resp = make_response(json.dumps(data, indent=4, sort_keys=True, default=str), code)
    resp.headers.extend(headers or {})
    return resp

api.add_resource(QuestionService, '/','/question')
api.add_resource(QuestionList,'/list', '/list/<int:id>')

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port, expose_tracebacks=False, url_scheme='https')