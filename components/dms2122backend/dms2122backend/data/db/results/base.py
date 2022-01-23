from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy.orm import relationship
from typing import Dict
from abc import ABC, abstractmethod

class Base(ABD):
    
    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(cls, cls._table_definition(metadata),properties=cls._mapping_properties())
    
    @staticmethod
    def _mapping_properties() -> Dict:
        return {}  
    
    @staticmethod
    @abstractmethod
    def _table_definition(metadata: MetaData) -> Table: