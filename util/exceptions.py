class NoEnviromentException(Exception):
    def __init__(self, message):
        super(NoEnviromentException, self).__init__(message)
