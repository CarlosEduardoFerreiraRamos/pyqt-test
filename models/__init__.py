from .question import Question
from .config import ConfigProp
from .indexed_file import IndexedFile
from .declarative_bases import Entity

from resources import Base, db_engine

Base.metadata.create_all(db_engine)