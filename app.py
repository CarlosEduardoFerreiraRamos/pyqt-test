import sys
import os
import re

from docx import Document
from waitress import serve

""" Flask moduels """
from flask import Flask
from flask_restful import Api

"""internal modules """

""" Must start first"""
from configuration import ConfigurationManager, Path

from reader import Reader
from models import Question, ConfigProp
from services import MockService, Question as QuestionService
from util import get_command_prop  

ms = MockService()
app = Flask(__name__)
api = Api(app)

api.add_resource(QuestionService, '/question')

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port, expose_tracebacks=False, url_scheme='https')