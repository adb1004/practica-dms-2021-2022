from abc import ABC, abstractmethod
from typing import Dict
from sqlalchemy import Table, MetaData  
from sqlalchemy.orm import mapper 

# Base from all the db entries
class Base(ABC):
    
    # Maps the user db entries to objects
    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(cls, cls._table_definition(metadata),properties=cls._mapping_properties())
    
    # Properties of the map
    @staticmethod
    def _mapping_properties() -> Dict:
        return {}  
    
    # Sets a table
    @staticmethod
    @abstractmethod
    def _table_definition(metadata: MetaData) -> Table:
        """base
        """