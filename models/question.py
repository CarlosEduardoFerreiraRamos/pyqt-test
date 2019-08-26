class Question(object):
    def __init__ (self):
        self.start = None
        self.end = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    def has_close(self):
        self.start != None