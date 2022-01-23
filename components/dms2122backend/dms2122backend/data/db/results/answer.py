from dms2122backend.data.db.results.base import Base
from sqlalchemy import Table, ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from typing import Dict

class Answer(Base):

    def __init__(self, user: str, qid: int, id: int):
        #Constructor
        self.user: str = user
        self.qid: int = qid
        self.id: int = id
    
    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
         return Table(
            'answers',
            metadata,
            Column('user', String(32), ForeignKey('user.username'), primary_key=True),
            Column('qid', Integer, ForeignKey('questions.qid'), primaryKey=True),
            Column('id', Integer, nullable=False)
        ) 