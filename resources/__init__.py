from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from configuration.manager import ConfigurationManager, ConfigProp

from resources.index_list import IndexListManager
from resources.mongodb import MongoManager
from resources.postgres import PostgresManager


db_engine = create_engine(ConfigurationManager.get_config_value(ConfigProp.db_postgres_name())) 
Base = declarative_base()
