import json
import os
from pathlib import Path as homePath
import logging

from configuration.manager import ConfigurationManager
from configuration.paths import Path
from configuration.config_state import ConfigState
from models import ConfigProp
from util import get_command_prop, NoEnviromentException

logging.basicConfig(level=logging.DEBUG)

is_prod = get_command_prop('--PROD') is not None
config_path = Path.prod_configuration() if is_prod else Path.json_configuration()

mongo_key = os.environ.get('MONGO_ATLAS_KEY', None)
mongo_user = os.environ.get('MONGO_ATLAS_USER', None)

if is_prod is True and (mongo_key is None or mongo_user is None):
    error_mensage = "No eviroment variable {}".format('MONGO_ATLAS_KEY' if mongo_user is not None else 'MONGO_ATLAS_USER')
    raise NoEnviromentException(error_mensage)

with open(config_path) as d_config:
    data = json.load(d_config)

    if is_prod:
        data[ConfigProp.db_name()] = data[ConfigProp.db_name()].format(mongo_user,mongo_key) 
    
    ConfigurationManager.set_state_config(data)

print(ConfigState().config)

