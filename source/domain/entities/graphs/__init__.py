import networkx as nx
import numpy as np

from source.domain.entities.operators import Operator
from source.domain.entities.calculators import Calculator

DOMAINS = {"G": nx.path_graph(2), "g": nx.path_graph(2)}
CONSTANTS = {"Pi Number": np.pi}


class Graphs:
    class Graph(Operator, Calculator):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__("G")

        def calculate(self, graph):
            return graph
