import json
import os
from pathlib import Path as homePath
import logging

from configuration.manager import ConfigurationManager
from configuration.paths import Path
from configuration.config_state import ConfigState
from configuration.config import ConfigProp
from util import get_command_prop, NoEnviromentException

logging.basicConfig(level=logging.DEBUG)

is_prod = get_command_prop('--PROD') is not None
config_path = Path.prod_configuration() if is_prod else Path.json_configuration()

mongo_key = os.environ.get('MONGO_ATLAS_KEY', None)
mongo_user = os.environ.get('MONGO_ATLAS_USER', None)

postgres_url = os.environ.get('HEROKU_POSTGRES_URL', None)

if is_prod is True and (mongo_key is None or mongo_user is None):
    raise NoEnviromentException("No eviroment variable {}".format('MONGO_ATLAS_KEY' if mongo_user is not None else 'MONGO_ATLAS_USER'))

if is_prod is True and (postgres_url is None):
    raise NoEnviromentException("No eviroment variable {}".format('HEROKU_POSTGRES_URL'))

with open(config_path) as d_config:
    data = json.load(d_config)

    if is_prod:
        data[ConfigProp.db_name()] = data[ConfigProp.db_name()].format(mongo_user,mongo_key) 
        data[ConfigProp.db_postgres_name()] = data[ConfigProp.db_postgres_name()].format(postgres_url)

    ConfigurationManager.set_state_config(data)

print(ConfigState().config)

