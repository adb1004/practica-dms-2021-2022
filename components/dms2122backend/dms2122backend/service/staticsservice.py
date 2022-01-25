from dms2122backend.data.db import Schema 
from dms2122backend.logic.logicstatistics import LogicStatistics
from typing import List, Optional, Dict
from sqlalchemy.orm.session import Session

# Class that manages the service of the statistics
class StatisticsServices():
    
    # Returns the statistics from a particular user
    @staticmethod
    def userStatistics(username: str, schema: Schema)-> Dict:
        session: Session = schema.new_session()
        o: Dict = []
        
        try:
            o = LogicStatistics.userStatistics(session, username)
        except Exception as exception: raise exception
        finally: schema.remove_session()
        
        return o

    # Returns the statistics from all the users
    @staticmethod
    def usersStatistics(schema: Schema)-> List[Dict]:
        session: Session = schema.new_session()
        o: List[Dict] = []
        
        try:
            o = LogicStatistics.usersStatistics(session)
        except Exception as exception: raise exception
        finally: schema.remove_session()
        
        return o

    # Returns the statistics from all the questions
    @staticmethod
    def questionsStatistics(schema: Schema) -> List[Dict]:
        session: Session = schema.new_session()
        o: List[Dict] = []
        
        try:
            o = LogicStatistics.questionsStatistics(session)
        except Exception as exception: raise exception
        finally: schema.remove_session()
        
        return o 