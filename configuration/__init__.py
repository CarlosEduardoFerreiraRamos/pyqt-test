import json
import os
from pathlib import Path as homePath
import logging

from configuration.manager import ConfigurationManager
from configuration.paths import Path
from configuration.config_state import ConfigState
from models import ConfigProp
from util import get_command_prop

logging.basicConfig(level=logging.DEBUG)

is_prod = get_command_prop('--PROD') is not None
config_path = Path.prod_configuration() if is_prod else Path.json_configuration()

with open(config_path) as d_config:
    data = json.load(d_config)

    if is_prod:
        data[ConfigProp.db_name()] = data[ConfigProp.db_name()].format("HVmachine85") 
    
    ConfigurationManager.set_state_config(data)

print(ConfigState().config)

