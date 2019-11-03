
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QWidget, QMessageBox, QLabel, QPushButton, QFileDialog
from typing import Callable

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(600, 600)
        self.setWindowTitle('File Manager')
        self.func = None

    def closeEvent(self, event):
        if self.func is not None:
            self.func() 
        event.accept()
