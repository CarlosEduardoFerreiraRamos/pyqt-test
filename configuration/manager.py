import shelve

from configuration.paths import Path
from configuration.config_state import ConfigState
from models import ConfigProp

class ConfigurationManager(object):
    def __init__(self):
        pass

    @staticmethod
    def set_db_config(default_config: dict) -> None:
        """ Set configuration to shelve db """
        with shelve.open(Path.config_file()) as db:
            db[ConfigProp.PATHS_DB()] = default_config
        pass

    @staticmethod
    def get_config() -> dict:
        """Access configuration from shelve db"""
        config = None
        with shelve.open(Path.config_file()) as db:
            config = db.get(ConfigProp.PATHS_DB(), None)
        return config

    @staticmethod
    def get_default_home_dir() -> str:
        return ConfigState().config.get(ConfigProp.home_path()) 

    @staticmethod
    def set_config(value: str, prop: str) -> None:
        ConfigState().config.update({prop: value})

    @staticmethod
    def get_config_value(prop: str) -> str:
        return ConfigState().config.get(prop, '')

    @staticmethod
    def set_state_config(data: dict) -> None:
        ConfigState().config = data

    @staticmethod
    def get_state_config() -> dict:
        return ConfigState().config

    @staticmethod
    def sync() -> None:
        """ Synchronize the app reference with the shelve db """
        with shelve.open(Path.config_file()) as db:
            db[ConfigProp.PATHS_DB()] = ConfigState().config
        pass