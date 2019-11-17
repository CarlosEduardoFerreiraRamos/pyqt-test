import sys
import os
import re

from docx import Document

from waitress import serve

""" Flask moduels """
from flask import Flask
from flask_restful import Api


"""PyQt modules """
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QWidget, QMessageBox, QLabel, QPushButton, QFileDialog
# from PyQt5.QtGui import QPalette

"""intern modules """
from reader import Reader
from models import Question, ConfigProp
from services import MockService, Question as QuestionService
# from configuration import ConfigurationManager, Path
# from widget import MainWidget
from util import get_command_prop  

SAVE_FOLDER = 'C:/Users/kadu_/Desktop/holder/'
TARGET_FILE = 'C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE.docx'

ms = MockService()
app = Flask(__name__)
api = Api(app)

api.add_resource(QuestionService, '/question')

def create_folder(folderPath):
        os.makedirs(folderPath, exist_ok=True)

def get_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return file.read()

def set_default_values():
    pass

def build_web_ui():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(QuestionService, '/question')

    app.run(debug=True)



if __name__ == "__main__":
    # app.run(debug=True)
    port = os.environ.get('PORT', 5000)
    print(port, 'is port')
    serve(app, host='0.0.0.0', port=port, expose_tracebacks=False, url_scheme='https')