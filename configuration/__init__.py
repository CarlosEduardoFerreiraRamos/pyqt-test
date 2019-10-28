import json
from pathlib import Path as homePath

from configuration.manager import ConfigurationManager
from configuration.paths import Path
from models import ConfigProp

db_configuration = ConfigurationManager.get_config()

if db_configuration is None:
    with open(Path.json_configuration()) as d_config:
        data = json.load(d_config)
        data[ConfigProp.home_path()] = homePath.home() 
        ConfigurationManager.set_default_config(data)


