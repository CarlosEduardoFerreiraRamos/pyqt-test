import shelve

from configuration import Path

CONFIG_FILE = './config_user.db'
CONFIG_PROP = 'user_config'

class ConfigurationManager(object):
    def __init__(self):
        pass

    @staticmethod
    def set_default_config(default_config: dict) -> None:
        with shelve.open(Path.config_file()) as db:
            db[CONFIG_PROP] = default_config
        pass

    @staticmethod
    def set_config(value: str, prop: str) -> None:
        pass

    @staticmethod
    def get_config() -> dict:
        config = None
        with shelve.open(Path.config_file()) as db:
            config = db[CONFIG_PROP]
        return config

    @staticmethod
    def get_config_value(prop: str) -> str:
        value = ''
        with shelve.open(Path.config_file()) as db:
            config = db[CONFIG_PROP]
            value = config[prop] if config is not None else ''
        return value
