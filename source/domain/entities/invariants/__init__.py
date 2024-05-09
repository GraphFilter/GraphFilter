from abc import ABC, abstractmethod
from source.domain.entities.calculators import Calculator


class Invariant(Calculator, ABC):
    def __init__(self, name: str = None, code: str = None):
        super().__init__(name, code)

    @abstractmethod
    def calculate(self, graph):
        pass

    @abstractmethod
    def print(self, graph, precision):
        pass
