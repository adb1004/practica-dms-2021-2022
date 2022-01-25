from dms2122backend.data.db.results.base import Base
from sqlalchemy import Table, ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from typing import Dict

# Class that determines how an answer db entry is going to be
class Answer(Base):

    # Constructor
    def __init__(self, user: str, qid: int, id: int):
        self.user: str = user
        self.qid: int = qid
        self.id: int = id
    
    # How the db table of an answer is going to be
    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        return Table('answers', metadata, Column('user', String(32), primary_key=True), Column('id', Integer, nullable=False), Column('qid', Integer, ForeignKey('questions.qid'), primary_key=True)) 