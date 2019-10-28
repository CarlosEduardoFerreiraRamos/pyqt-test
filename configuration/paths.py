class Path(object):
    pass

    @staticmethod
    def configuration():
        return './configuration'

    @staticmethod
    def assets():
        return './assets'

    @staticmethod
    def data_base():
        return '{}/data_base'.format(Path.assets())

    @staticmethod
    def json_configuration():
        return '{}/default_config.json'.format(Path.configuration())

    @staticmethod
    def config_file():
        return '{}/config_user.db'.format(Path.data_base())