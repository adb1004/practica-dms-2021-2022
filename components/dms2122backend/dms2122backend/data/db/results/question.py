from dms2122backend.data.db.results.base import Base
from dms2122backend.data.db.results.answer import Answer
from sqlalchemy import Table, Column, Integer, Float,String, MetaData
from sqlalchemy.orm import relationship
from typing import Dict

class Question(Base):

    def __init__(self, title:str, desc:str, c_1:str, c_2:str, c_3:str, c_4:str, c_right:int, puntuation: float, penalization: float):
        #Constructor
        self.title: str = title
        self.desc: str = desc
        self.c_1: str = c_1
        self.c_2: str = c_2
        self.c_3: str = c_3
        self.c_4: str = c_4
        self.c_right: int = c_right
        self.puntuation: float = puntuation
        self.penalization: float = penalization

    @staticmethod
    def _mapping_properties() -> Dict:
        return { 'questions': relationship(Answer, backref='question')}
    
    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        return Table(
            'questions',
            metadata,
            Column('qid', Integer, autoincrement= 'auto', primary_key=True),
            Column('title', String(64), nullable=False), Column('desc', String(512), nullable=False),
            Column('c_1', String(64), nullable=False), Column('c_2', String(64), nullable=False), Column('c_3', String(64), nullable=False), Column('c_4', String(64), nullable=False),
            Column('c_right', Integer, nullable=False), Column('puntuation', Float(2,2), nullable=False), Column('penalization', Float(2,2), nullable=False)
        )