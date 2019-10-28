import shelve

from configuration.paths import Path
from models import ConfigProp

class ConfigurationManager(object):
    def __init__(self):
        pass

    @staticmethod
    def set_default_config(default_config: dict) -> None:
        with shelve.open(Path.config_file()) as db:
            db[ConfigProp.PATHS_DB()] = default_config
        pass

    @staticmethod
    def set_config(value: str, prop: str) -> None:
        with shelve.open(Path.config_file()) as db:
            data = db[ConfigProp.PATHS_DB()]
            data[prop] =  value
            db[ConfigProp.PATHS_DB()] = data
        pass

    @staticmethod
    def get_config() -> dict:
        config = None
        with shelve.open(Path.config_file()) as db:
            config = db.get(ConfigProp.PATHS_DB(), None)
        return config

    @staticmethod
    def get_config_value(prop: str) -> str:
        value = ''
        with shelve.open(Path.config_file()) as db:
            config = db[ConfigProp.PATHS_DB()]
            value = config[prop] if config is not None else ''
        return value
