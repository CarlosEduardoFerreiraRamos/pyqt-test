import json
import os
from pathlib import Path as homePath

from configuration.manager import ConfigurationManager
from configuration.paths import Path
from configuration.config_state import ConfigState
from models import ConfigProp

db_configuration = ConfigurationManager.get_config()

if db_configuration is None:
    with open(Path.json_configuration()) as d_config:
        data = json.load(d_config)
        data[ConfigProp.home_path()] = os.getenv('HOME') 
        ConfigurationManager.set_db_config(data)
        ConfigurationManager.set_state_config(data)
else:
    ConfigurationManager.set_state_config(db_configuration)

print(ConfigState().config)

