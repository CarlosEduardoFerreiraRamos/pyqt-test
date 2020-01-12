from databases import Base, db_engine

from .question import Question
from .indexed_file import IndexedFile
from .declarative_bases import Entity

Base.metadata.create_all(db_engine)