import json

from configuration.manager import ConfigurationManager
from configuration.paths import Path

db_configuration = ConfigurationManager.get_config()
print('config', db_configuration)
if db_configuration is None:
    with open(Path.json_configuration()) as d_config:
        data = json.load(d_config)
        ConfigurationManager.set_default_config(data)


