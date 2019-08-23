import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QPushButton
from PyQt5.QtGui import QPalette
from reader import Reader

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
#     app = QApplication([])
#     app.setStyle('Fusion')

    create_folder('./script/')
    
    stringFile = get_file('./scripts/test.txt')
#     stringFile = get_file('./scripts/doc.docx')
    reader = Reader()
    reader.parse(stringFile)
    reader.set_values({})
    template = reader.render()
    print('template', template)

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
