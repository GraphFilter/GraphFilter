from typing import Dict, List
from source.domain.entities.invariants import Invariant
from source.domain.filter import GenericFilter


class Parameters: 
    def __init__(self, name: str, method: GenericFilter, equation: str, conditions: Dict[Invariant, bool], description: str, files: List[str], location: str):
        self.name = name
        self.method = method
        self.equation = equation
        self.conditions = conditions
        self.description = description
        self.files = files
        self.location = location