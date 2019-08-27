import sys
import os
import re

from docx import Document


"""PyQt modules """
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QPushButton
from PyQt5.QtGui import QPalette

"""intern modules """
from reader import Reader
from models.question import Question
from services import MockService

SAVE_FOLDER = 'C:/Users/kadu_/Desktop/holder/'
TARGET_FILE = 'C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE.docx'

def create_folder(folderPath):
        os.makedirs(folderPath, exist_ok=True)

def get_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return file.read()

def dialog():
    mbox = QMessageBox()
    mbox.setText('Anything you may want to say.')
    mbox.setDetailedText('Anything special you may want to talk about.')
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

if __name__ == "__main__":
    create_folder('./script/')

    ms = MockService()

    ms.build_questions(TARGET_FILE)


#     app = QApplication([])
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
