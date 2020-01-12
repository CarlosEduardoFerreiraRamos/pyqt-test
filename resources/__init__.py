from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from configuration import ConfigurationManager, ConfigProp

from resources.mongodb import MongoManager
from resources.postgres import PostgresManager

from resources.index_list import IndexListManager


db_engine = create_engine(ConfigurationManager.get_config_value(ConfigProp.db_postgres_name())) 
Base = declarative_base()
