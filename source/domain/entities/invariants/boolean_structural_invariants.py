import grinpy as gp
import networkx as nx

from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import print_boolean


class BooleanStructuralInvariants:
    class Planar(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.check_planarity(graph)[0]

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Connected(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_connected(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Biconnected(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_biconnected(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Bipartite(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_bipartite(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Eulerian(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_eulerian(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Chordal(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_chordal(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class TriangleFree(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return gp.is_triangle_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class BullFree(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return gp.is_bull_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Regular(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_regular(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class ClawFree(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return gp.is_claw_free(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Tree(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_tree(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SelfComplementary(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_isomorphic(graph, nx.complement(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Cubic(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.is_k_regular(graph, k=3)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class HasBridge(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.has_bridges(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class Threshold(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.algorithms.threshold.is_threshold_graph(graph)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)
