from managers import MockManager

class MockService(object):
    def __init__(self):
        self.service: MockManager = MockManager()

    def build_questions(self, file_path: list, folder_path: str):
        self.service.config_save_forder = folder_path
        response = self.service.build_questions(file_path)
        return response

