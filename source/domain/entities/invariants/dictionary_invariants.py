import networkx as nx

from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants.utils import print_dict


class DictionaryInvariants:
    class DegreeCentrality(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return dict(sorted(nx.degree_centrality(graph).items(), key=lambda x: x[1]))

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class EigenvectorCentrality(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            try:
                return dict(sorted(nx.eigenvector_centrality_numpy(graph).items(), key=lambda x: x[1]))
            except TypeError:
                return dict(sorted(nx.eigenvector_centrality(graph).items(), key=lambda x: x[1]))

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class ClosenessCentrality(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return dict(sorted(nx.closeness_centrality(graph).items(), key=lambda x: x[1]))

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class BetweennessCentrality(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return dict(sorted(nx.betweenness_centrality(graph).items(), key=lambda x: x[1]))

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class HarmonicCentrality(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return dict(sorted(nx.harmonic_centrality(graph).items(), key=lambda x: x[1]))

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class Transmission(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                dist_matrix = MatrixInvariants.DistanceMatrix().calculate(graph)
                trans = {}
                for i in range(0, dist_matrix.shape[0]):
                    trans[i] = sum(dist_matrix[:, i])
                return trans
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)

    class CoreNumber(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.core_number(graph)

        def print(self, graph, precision):
            return print_dict(self.calculate(graph), precision)
