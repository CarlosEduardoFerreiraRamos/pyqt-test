import os
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QWidget, QMessageBox, QLabel, QPushButton, QFileDialog

from typing import Callable

from configuration import ConfigurationManager, Path

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

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self,directory=ConfigurationManager.get_default_home_dir())
        return folder_path if folder_path else '' 

    def select_file(self):
        options = QFileDialog.Options()
        path, _  = QFileDialog.getOpenFileNames(self,filter='Text files (*.docx)', directory=ConfigurationManager.get_default_home_dir(),options=options)
        return path[0] if len(path) > 0 else ''
