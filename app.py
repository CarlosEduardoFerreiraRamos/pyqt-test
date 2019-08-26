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

def find_questions(paragraphs):
    questions = []
    for index, paragraph in enumerate(paragraphs):

        is_list = paragraph.style.name == 'List Paragraph'
        has_question_number = re.match('^[0-9]\.', paragraph.text)

        if is_list or has_question_number:

            leng = len(questions)
            if leng != 0:
                questions[leng -1].end = index -1

            q = Question()
            q.start = index
            questions.append(q)
    
    questions[len(questions) - 1].end = len(paragraphs) -1
    return questions
                


if __name__ == "__main__":
#     app = QApplication([])
#     app.setStyle('Fusion')

    create_folder('./script/')    
    stringFile = get_file('./scripts/test.txt')

# C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE
    doc = Document('C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE.docx')
#     stringFile = get_file('./scripts/doc.docx')
#     reader = Reader()
#     reader.parse(stringFile)
#     reader.set_values({})
#     template = reader.render()
#     print('template', template)
    for para in doc.paragraphs:
        if para.text:
            print(para.text)
        else:
            print('')

    answers = find_questions(doc.paragraphs)
    for item in answers:
        print('questions: ', item.start, item.end)

    parag = doc.paragraphs[10]
    print('parag.alignment', parag.alignment)
    print('paragraph_format.first_line_indent', parag.paragraph_format.first_line_indent)
    print('paragraph_format.left_indent', parag.paragraph_format.left_indent)
    
    print('style.type.base_style', parag.style.name)
    print('style.type', parag.style.type)
    print('text', parag.text)

    """
    parag.alignment JUSTIFY (3)
    paragraph_format.first_line_indent -180340
    paragraph_format.left_indent 180340
    style.type.base_style List Paragraph
    style.type PARAGRAPH (1)
    text A partir da leitura do texto, analise as afirmações: (1,0)
    """

"""
C:/Users/kadu_/Desktop/REC PT 2BI 2SERIE
process
EXPLORATION
        steps:
                1 -  find blocks, find questions;
                2 -  classify blocks, classify questions;
                3 -  save data.

EDITION
        steps:
                1 -  selection of target block;
                2 -  any edition;
                3 -  creation of new blocks every new edition.

WRITING
        steps:
                1 -  choose blocks to make test;
                2 -  choose randomization options;
                3 -  write n number of tests. 
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
