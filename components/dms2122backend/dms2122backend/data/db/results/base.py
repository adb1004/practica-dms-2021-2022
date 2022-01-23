from abc import ABC, abstractmethod
from typing import Dict
from sqlalchemy import Table, MetaData  
from sqlalchemy.orm import mapper 

class Base(ABC):
    
    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(cls, cls._table_definition(metadata),properties=cls._mapping_properties())
    
    @staticmethod
    def _mapping_properties() -> Dict:
        return {}  
    
    @staticmethod
    @abstractmethod
    def _table_definition(metadata: MetaData) -> Table:
        """base
        """