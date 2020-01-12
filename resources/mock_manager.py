import re

from models.question import Question
from .file_manager import FileManager

class MockManager(object):
    def __init__(self):
        super().__init__()
        self.config_save_forder = 'C:/Users/kadu_/Desktop/holder/'
        self.CONFIG_REPLACE_FILES = True

    def build_questions(self, file_paths: list) -> int:
        self.config_save_forder
        questions_found = 0
        paragraphs = []
        documents = []

        documents = list(map( lambda path: FileManager.get_document(path),file_paths))
            
        if len(documents) > 0:
            for document in documents: 
                selected_paragraphs = self.__find_questions(document.paragraphs)
                for selected in selected_paragraphs:
                    paragraphs.append(self.__extract_question(document, selected))
                questions_found = len(paragraphs)
        
        try:
            self.__write_files(paragraphs)
            return questions_found or None
        except NameError as error:
            print(error)
            return None

    def __write_files(self, questions: list) -> None:
        for index, question in enumerate(questions):
            count = str(index if self.CONFIG_REPLACE_FILES else FileManager.get_file_count())
            document = FileManager.get_black_document()
            for paragraph in question:                
                document.add_paragraph(paragraph.text, paragraph.style)
            foder_path = ''.join([self.config_save_forder,'/question_',count,'.docx'])
            document.save(foder_path)

    def __find_questions(self, paragraphs: list) -> list:
        questions = []
        for index, paragraph in enumerate(paragraphs):

            is_list = paragraph.style.name == 'List Paragraph'
            has_question_number = re.match('^[0-9]\.', paragraph.text)
            has_start = re.search('@start',paragraph.text)

            if is_list or has_question_number or has_start:
                leng = len(questions)
                if leng != 0:
                    questions[leng -1].end = index -1
                q = Question()
                q.start = index
                questions.append(q)
                self.__format_paragraphs(paragraph, len(questions))
        questions[len(questions) - 1].end = len(paragraphs)
        return questions
                    
    def __extract_question(self, doc, question: Question) -> list:
        questions_paragraphs = []
        for index in range(question.start, question.end):
            questions_paragraphs.append(doc.paragraphs[index])
        return questions_paragraphs
    
    def __format_paragraphs(self,paragraph, length: int) -> None:
        if re.search('@start',paragraph.text) is not None:
            paragraph.clear()
            paragraph.add_run('{} )'.format(length))
        pass
    