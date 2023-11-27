import grinpy as gp
import networkx as nx

from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import print_boolean


class BooleanStructuralInvariants:
    class Planar(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Planar")

        def calculate(self, graph):
            return nx.check_planarity(graph)[0]

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Connected(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Connected")

        def calculate(self, graph):
            return nx.is_connected(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Biconnected(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Biconnected")

        def calculate(self, graph):
            return nx.is_biconnected(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Bipartite(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Bipartite")

        def calculate(self, graph):
            return nx.is_bipartite(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Eulerian(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Eulerian")

        def calculate(self, graph):
            return nx.is_eulerian(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Chordal(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Chordal")

        def calculate(self, graph):
            return nx.is_chordal(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class TriangleFree(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Triangle-free")

        def calculate(self, graph):
            return gp.is_triangle_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class BullFree(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Bull-free")

        def calculate(self, graph):
            return gp.is_bull_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Regular(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Regular")

        def calculate(self, graph):
            return nx.is_regular(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class ClawFree(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Claw-free")

        def calculate(self, graph):
            return gp.is_claw_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Tree(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Tree")

        def calculate(self, graph):
            return nx.is_tree(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SelfComplementary(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Self-complementary")

        def calculate(self, graph):
            return nx.is_isomorphic(graph, nx.complement(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Cubic(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Cubic")

        def calculate(self, graph):
            return nx.is_k_regular(graph, k=3)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class HasBridge(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Has bridge")

        def calculate(self, graph):
            return nx.has_bridges(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Threshold(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Threshold")

        def calculate(self, graph):
            return nx.algorithms.threshold.is_threshold_graph(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)
