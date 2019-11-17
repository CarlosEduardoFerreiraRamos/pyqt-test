from configuration.paths import Path
from configuration.config_state import ConfigState
from models import ConfigProp

class ConfigurationManager(object):
    def __init__(self):
        pass

    @staticmethod
    def get_default_home_dir() -> str:
        return ConfigState().config.get(ConfigProp.home_path()) 

    @staticmethod
    def set_config(value: str, prop: str) -> None:
        ConfigState().config.update({prop: value})

    @staticmethod
    def get_config_value(prop: str) -> list:
        return ConfigState().config.get(prop, [])

    @staticmethod
    def set_state_config(data: dict) -> None:
        ConfigState().config = data

    @staticmethod
    def get_state_config() -> dict:
        return ConfigState().config