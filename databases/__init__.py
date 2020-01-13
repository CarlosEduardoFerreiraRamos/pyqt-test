from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from configuration import ConfigurationManager, ConfigProp
from .mongodb import MongoManager
from .postgres import PostgresManager

db_engine = create_engine(ConfigurationManager.get_config_value(ConfigProp.db_postgres_name()))
Base = declarative_base()