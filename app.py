import sys
import os
import re

from docx import Document

"""PyQt modules """
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QWidget, QMessageBox, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPalette

"""intern modules """
from reader import Reader
from models import Question, ConfigProp
from services import MockService
from configuration import ConfigurationManager, Path
from widget import MainWidget

paths = {
    ConfigProp.FILE_PROP(): '',
    ConfigProp.FOLDER_PROP(): ''
}

SAVE_FOLDER = 'C:/Users/kadu_/Desktop/holder/'
TARGET_FILE = 'C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE.docx'

ms = MockService()

def create_folder(folderPath):
        os.makedirs(folderPath, exist_ok=True)

def get_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return file.read()

def set_default_values():
    paths.update({
        ConfigProp.FILE_PROP(): ConfigurationManager.get_config_value(ConfigProp.FILE_PROP()),
        ConfigProp.FOLDER_PROP(): ConfigurationManager.get_config_value(ConfigProp.FOLDER_PROP())
    })
    print(paths)
    pass


def select_folder():
    folder_path = QFileDialog.getExistingDirectory()
    return folder_path if folder_path else '' 

def select_file():
    options = QFileDialog.Options()
    path, _  = QFileDialog.getOpenFileNames(filter='Text files (*.docx)',options=options)
    return path[0] if len(path) > 0 else ''

def set_path(path, labelWidget, prop_name):
    paths.update({prop_name: path})
    labelWidget.setText(paths.get(prop_name))
    labelWidget.show()
    ConfigurationManager.set_config(path,prop_name)

def manage_process_btn_access():
    if paths.get(ConfigProp.FILE_PROP()) and paths.get(ConfigProp.FOLDER_PROP()):
        ms.build_questions(paths.get(ConfigProp.FILE_PROP()), paths.get(ConfigProp.FOLDER_PROP()))
    else:
        show_mensage_box()
    
def show_mensage_box():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Both target file and folder must be selected to execute the process!")
    msgBox.setWindowTitle("Path Missing")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


if __name__ == "__main__":
#     create_folder('./script/')

    app = QApplication(sys.argv)
    w = MainWidget()
    w.func = lambda: print('being close')

    set_default_values()

    # options = QFileDialog.Options()
    # QFileDialog.getOpenFileNames()

    lProceed = QLineEdit(w)
    lProceed.move(220,200)
    lProceed.resize(280,38)
    lProceed.setDisabled(True)
    lProceed.show()

    btnProceed = QPushButton(w)
    btnProceed.setText('Proceed')
    btnProceed.show()
    btnProceed.move(110,200)
    btnProceed.clicked.connect(lambda: manage_process_btn_access())

    lFile = QLineEdit(w)
    lFile.move(220,150)
    lFile.resize(280,38)
    lFile.setText(paths.get(ConfigProp.FILE_PROP()))
    lFile.setDisabled(True)
    lFile.show()

    btnFile = QPushButton(w)
    btnFile.setText('Open File')
    btnFile.show()
    btnFile.move(110, 150)
    btnFile.clicked.connect(lambda: set_path(select_file(), lFile, ConfigProp.FILE_PROP()))

    lFolder = QLineEdit(w)
    lFolder.move(220,100)
    lFolder.resize(280,38)
    lFolder.setText(paths.get(ConfigProp.FOLDER_PROP()))
    lFolder.setDisabled(True)
    lFolder.show()

    btnFolder = QPushButton(w)
    btnFolder.setText('Select Folder')
    btnFolder.show()
    btnFolder.move( 110,100)
    btnFolder.clicked.connect(lambda: set_path(select_folder(), lFolder, ConfigProp.FOLDER_PROP()))

    w.show()
    sys.exit(app.exec_())

#     app.setStyle('Fusion')
#     stringFile = get_file('./scripts/test.txt')
#     stringFile = get_file('./scripts/doc.docx')
#     reader = Reader()
#     reader.parse(stringFile)
#     reader.set_values({})
#     template = reader.render()
#     print('template', template)

    # parag = doc.paragraphs[10]
    # print('parag.alignment', parag.alignment)
    # print('paragraph_format.first_line_indent', parag.paragraph_format.first_line_indent)
    # print('paragraph_format.left_indent', parag.paragraph_format.left_indent)
    
    # print('style.type.base_style', parag.style.name)
    # print('style.type', parag.style.type)
    # print('text', parag.text)



    """
    parag.alignment JUSTIFY (3)
    paragraph_format.first_line_indent -180340
    paragraph_format.left_indent 180340
    style.type.base_style List Paragraph
    style.type PARAGRAPH (1)
    text A partir da leitura do texto, analise as afirmações: (1,0)
    """

"""
pyqt segment
"""
#     print(dir(parag))
#     for d in dir(parag):    
#         print(d, para.)
                    
#     print('doc', doc.paragraphs)


#     qp = QPalette()
#     qp.setColor(QPalette.ButtonText, Qt.darkBlue)
#     qp.setColor(QPalette.Window, Qt.darkBlue)
#     qp.setColor(QPalette.Button, Qt.darkCyan)
#     app.setPalette(qp)


#     w = QWidget()
#     w.resize(300, 300)
#     w.setWindowTitle('My python desktop app')

#     label = QLabel(w)
#     label.setText('Label of a label')
#     label.move(100,130)
#     label.show()

#     btn = QPushButton(w)
#     btn.setText('See something awesome')
#     btn.move(100, 130)
#     btn.show()
#     btn.clicked.connect(dialog)

#     w.show()
#     sys.exit(app.exec_())
