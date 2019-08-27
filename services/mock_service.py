from managers import MockManager

class MockService(object):
    def __init__(self):
        self.service: MockManager = MockManager()

    def build_questions(self, file_path: str):
        response = self.service.build_questions(file_path)

