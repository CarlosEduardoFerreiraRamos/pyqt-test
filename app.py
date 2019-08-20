import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QPushButton
from PyQt5.QtGui import QPalette

def dialog():
    mbox = QMessageBox()
    mbox.setText('Anything you may want to say.')
    mbox.setDetailedText('Anything special you may want to talk about.')
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.darkBlue)
    qp.setColor(QPalette.Window, Qt.darkBlue)
    qp.setColor(QPalette.Button, Qt.darkCyan)
    app.setPalette(qp)


    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle('My python desktop app')

    label = QLabel(w)
    label.setText('Label of a label')
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('See something awesome')
    btn.move(100, 130)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())
