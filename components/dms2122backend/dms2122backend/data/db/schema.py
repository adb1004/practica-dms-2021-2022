from dms2122backend.data.config import BackendConfiguration
from dms2122backend.data.db.results import Answer, Question
from sqlalchemy import create_engine, event  
from sqlalchemy.engine import Engine  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, scoped_session  
from sqlalchemy.orm.session import Session 

@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record): 
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    cursor.close()

class Schema():
    def __init__(self, config: BackendConfiguration):
        if config.get_db_connection_string() is None: raise RuntimeError('`db_connection_string` needs to have a value')
        self.__declarative_base = declarative_base()
        db_connection_string: str = config.get_db_connection_string() or ''
        self.__create_engine = create_engine(db_connection_string)
        self.__session_maker = scoped_session(sessionmaker(bind=self.__create_engine))

        Question.map(self.__declarative_base.metadata)
        Answer.map(self.__declarative_base.metadata)
        self.__declarative_base.metadata.create_all(self.__create_engine)
    
    def new_session(self) -> Session:
        return self.__session_maker()

    def remove_session(self) -> None:
        self.__session_maker.remove()