import shelve

from configuration.paths import Path

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
        with shelve.open(Path.config_file()) as db:
            data = db[CONFIG_PROP]
            data[prop] =  value
            db[CONFIG_PROP] = data
            db.close()
        pass

    @staticmethod
    def get_config() -> dict:
        config = None
        with shelve.open(Path.config_file()) as db:
            config = db.get(CONFIG_PROP, None)
        return config

    @staticmethod
    def get_config_value(prop: str) -> str:
        value = ''
        with shelve.open(Path.config_file()) as db:
            config = db[CONFIG_PROP]
            value = config[prop] if config is not None else ''
        return value
