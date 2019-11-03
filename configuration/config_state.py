class ConfigState(object):
    __config: dict
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, config):
        self.__config = config
