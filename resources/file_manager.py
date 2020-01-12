import os
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

CONFIG_SAVE_FOLDER = 'C:/Users/kadu_/Desktop/holder/'

class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def get_document(file_path: str) -> Document:
        try:
            return Document(file_path)
        except PackageNotFoundError as error:
            return None        
    
    @staticmethod
    def get_black_document() -> Document:
        return Document()
    
    @staticmethod
    def get_file_count() -> int:
        return len(os.listdir(CONFIG_SAVE_FOLDER))

    