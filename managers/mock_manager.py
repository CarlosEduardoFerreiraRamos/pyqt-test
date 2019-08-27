import re

from models import Question
from managers import FileManager

CONFIG_SAVE_FOLDER = 'C:/Users/kadu_/Desktop/holder/'
CONFIG_REPLACE_FILES = True

class MockManager(object):

    def build_questions(self, file_path: str) -> int:
        document = FileManager.get_document(file_path)
        questions_found: int
        if document is not None:
            selected_paragraphs = self.__find_questions(document.paragraphs)
            paragraphs = []
            for selected in selected_paragraphs:
                paragraphs.append(self.__extract_question(document, selected))
            questions_found = len(paragraphs)
            try:
                self.__write_files(paragraphs)
            except NameError as error:
                print(error)
                return None
        return questions_found or None

    def __write_files(self, questions: list) -> None:
        for index, question in enumerate(questions):
            count = str(index if CONFIG_REPLACE_FILES else FileManager.get_file_count())
            document = FileManager.get_black_document()
            for paragraph in question:                
                document.add_paragraph(paragraph.text, paragraph.style)
            foder_path = ''.join([CONFIG_SAVE_FOLDER,'question_',count,'.docx'])
            document.save(foder_path)

    def __find_questions(self, paragraphs: list) -> list:
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
        questions[len(questions) - 1].end = len(paragraphs)
        return questions
                    
    def __extract_question(self, doc, question: Question) -> list:
        questions_paragraphs = []
        for index in range(question.start, question.end):
            questions_paragraphs.append(doc.paragraphs[index])
        return questions_paragraphs
    
    