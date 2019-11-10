import sys
import os
import re

from docx import Document

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
from configuration import ConfigurationManager, Path
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

def set_file_path(path, labelWidget, prop_name):
    if path:
        ConfigurationManager.set_config(path,prop_name)
        labelWidget.setText(path[0])
        labelWidget.show()
    else:
        pass

def set_folder_path(path, labelWidget, prop_name):
    if path:
        ConfigurationManager.set_config(path,prop_name)
        labelWidget.setText(path)
        labelWidget.show()
    else:
        pass

# def manage_process_btn_access():
#     file_path = ConfigurationManager.get_config_value(ConfigProp.FILE_PROP())
#     folder_path = ConfigurationManager.get_config_value(ConfigProp.FOLDER_PROP())
#     if file_path and folder_path:
#         response = ms.build_questions(file_path, folder_path)
#         print('return', response)
#     else:
#         show_mensage_box()
    
# def show_mensage_box():
#     msgBox = QMessageBox()
#     msgBox.setIcon(QMessageBox.Information)
#     msgBox.setText("Both target file and folder must be selected to execute the process!")
#     msgBox.setWindowTitle("Path Missing")
#     msgBox.setStandardButtons(QMessageBox.Ok)
#     msgBox.exec()

def build_web_ui():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(QuestionService, '/question')

    app.run(debug=True)    


# def build_desktop_ui():
#     app = QApplication(sys.argv)
#     w = MainWidget()
#     w.func = lambda: ConfigurationManager.sync()

#     set_default_values()

#     lProceed = QLineEdit(w)
#     lProceed.move(220,200)
#     lProceed.resize(280,38)
#     lProceed.setDisabled(True)
#     lProceed.show()

#     btnProceed = QPushButton(w)
#     btnProceed.setText('Proceed')
#     btnProceed.show()
#     btnProceed.move(110,200)
#     btnProceed.clicked.connect(lambda: manage_process_btn_access())

#     lFile = QLineEdit(w)
#     lFile.move(220,150)
#     lFile.resize(280,38)
#     lFile.setText(ConfigurationManager.get_config_value(ConfigProp.FILE_PROP())[0])
#     lFile.setDisabled(True)
#     lFile.show()

#     btnFile = QPushButton(w)
#     btnFile.setText('Open File')
#     btnFile.show()
#     btnFile.move(110, 150)
#     btnFile.clicked.connect(lambda: set_file_path(w.select_file(), lFile, ConfigProp.FILE_PROP()))

#     lFolder = QLineEdit(w)
#     lFolder.move(220,100)
#     lFolder.resize(280,38)
#     lFolder.setText(ConfigurationManager.get_config_value(ConfigProp.FOLDER_PROP()))
#     lFolder.setDisabled(True)
#     lFolder.show()

#     btnFolder = QPushButton(w)
#     btnFolder.setText('Select Folder')
#     btnFolder.show()
#     btnFolder.move( 110,100)
#     btnFolder.clicked.connect(lambda: set_folder_path(w.select_folder(), lFolder, ConfigProp.FOLDER_PROP()))

#     w.show()
#     sys.exit(app.exec_())



if __name__ == "__main__":
    app.run(debug=True)