import networkx as nx
import numpy as np
import numpy.linalg as la
import grinpy as gp

from source.domain.entities.functions import Function
from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants.utils import print_numeric, print_set, approx_to_int
from source.domain.entities.invariants import Invariant


class NumericStructuralInvariants:
    class NumberVertices(Function, Invariant):

        def __init__(self):
            super().__init__('n')

        def calculate(self, graph):
            return nx.number_of_nodes(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class NumberEdges(Function, Invariant):

        def __init__(self):
            super().__init__('\u0415')

        def calculate(self, graph):
            return nx.number_of_edges(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class CliqueNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u03c9')

        def calculate(self, graph):
            return len(set(nx.max_weight_clique(graph, weight=None)[0]))

        def print(self, graph, precision):
            return print_set(set(nx.max_weight_clique(graph, weight=None)[0]), precision)

    class IndependenceNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u237a')

        def calculate(self, graph):
            return NumericStructuralInvariants.CliqueNumber().calculate(nx.complement(graph))

        def print(self, graph, precision):
            return NumericStructuralInvariants.CliqueNumber().print(nx.complement(graph), precision)

    class DominationNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u0194')

        def calculate(self, graph):
            return gp.domination_number(graph)

        def print(self, graph, precision):
            return print_numeric(gp.domination_number(graph), precision)

    class ChromaticNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u03c7')

        def calculate(self, graph):
            number_of_nodes = len(graph.nodes())
            number_of_edges = len(graph.edges())
            if number_of_edges == 0:
                return 1
            if number_of_edges == number_of_nodes * (number_of_nodes - 1) / 2:
                return number_of_nodes
            if number_of_edges == (number_of_nodes * (number_of_nodes - 1) / 2) - 1:
                return number_of_nodes - 1
            if nx.is_bipartite(graph):
                return 2

            strategies = [max(nx.greedy_color(graph, strategy='DSATUR').values()),
                          max(nx.greedy_color(graph, strategy='largest_first', interchange=True).values()),
                          max(nx.greedy_color(graph, strategy='smallest_last', interchange=True).values()),
                          max(nx.greedy_color(graph, strategy='random_sequential', interchange=True).values())
                          ]

            return round(min(strategies) + 1)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class GirthNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u0261')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return len(nx.minimum_cycle_basis(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MatchingNumber(Function, Invariant):

        def __init__(self):
            super().__init__('\u03bd')

        def calculate(self, graph):
            return NumericStructuralInvariants.IndependenceNumber().calculate(nx.line_graph(graph))

        def print(self, graph, precision):
            return NumericStructuralInvariants.IndependenceNumber().print(nx.line_graph(graph), precision)

    class NumberComponents(Function, Invariant):

        def __init__(self):
            super().__init__('w')

        def calculate(self, graph):
            return nx.number_connected_components(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Valency(Function, Invariant):

        def __init__(self):
            super().__init__('d\u1d63')

        def calculate(self, graph):
            deg_seq = gp.degree_sequence(graph)
            valencies = []
            for i in range(0, nx.number_of_nodes(graph)):
                if deg_seq[i] not in valencies:
                    valencies.append(deg_seq[i])
            return len(valencies)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeMax(Function, Invariant):

        def __init__(self):
            super().__init__('\u0394')

        def calculate(self, graph):
            return max(gp.degree_sequence(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeMin(Function, Invariant):

        def __init__(self):
            super().__init__('\u1e9f')

        def calculate(self, graph):
            return min(gp.degree_sequence(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeAverage(Function, Invariant):

        def __init__(self):
            super().__init__('d\u2090')

        def calculate(self, graph):
            sequence = gp.degree_sequence(graph)
            return sum(sequence) / len(sequence)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class VertexCover(Function, Invariant):

        def __init__(self):
            super().__init__('\u03c4')

        def calculate(self, graph):
            return gp.vertex_cover_number(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Diameter(Function, Invariant):

        def __init__(self):
            super().__init__("diam")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return nx.diameter(graph)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Radius(Function, Invariant):

        def __init__(self):
            super().__init__("r")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return nx.radius(graph)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class KirchhoffIndex(Function, Invariant):

        def __init__(self):
            super().__init__('Kf')

        def calculate(self, graph):
            if nx.is_connected(graph):
                l_eigen = MatrixInvariants.SpectrumL().calculate(graph=graph)
                return nx.number_of_nodes(graph) * sum(1 / x for x in l_eigen[1:])
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeKirchhoffIndex(Function, Invariant):

        def __init__(self):
            super().__init__('K`f')

        def calculate(self, graph):
            if nx.is_connected(graph):
                n_eigen = MatrixInvariants.SpectrumN().calculate(graph)
                return 2 * nx.number_of_edges(graph) * sum(1 / x for x in n_eigen[1:])
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RandicIndex(Function, Invariant):

        def __init__(self):
            super().__init__("Ri")

        def calculate(self, graph):
            randic = MatrixInvariants.MatrixR().calculate(graph)
            s = 0
            size = nx.number_of_nodes(graph)
            for i in range(size):
                for j in range(i + 1, size):
                    s += randic[i][j]
            return s

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class NumberSpanningTree(Function, Invariant):

        def __init__(self):
            super().__init__('\u0288')

        @staticmethod
        def submatrix(m):
            n = m.shape[0]
            new = np.zeros((n - 1, n - 1))
            for i in range(0, n - 1):
                for j in range(0, n - 1):
                    new[i, j] = m[i + 1, j + 1]
            return new

        def calculate(self, graph):
            return int(la.det(self.submatrix(nx.laplacian_matrix(graph))))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Density(Function, Invariant):

        def __init__(self):
            super().__init__('\u018a')

        def calculate(self, graph):
            return nx.density(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class VertexConnectivity(Function, Invariant):

        def __init__(self):
            super().__init__('\u03f0')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return gp.node_connectivity(graph)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EdgeConnectivity(Function, Invariant):

        def __init__(self):
            super().__init__('\u03bb')

        def calculate(self, graph):
            return nx.edge_connectivity(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class ChromaticIndex(Function, Invariant):

        def __init__(self):
            super().__init__("\u03c7'")

        def calculate(self, graph):
            return NumericStructuralInvariants.ChromaticNumber().calculate(nx.line_graph(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MinimumEdgeCover(Function, Invariant):

        def __init__(self):
            super().__init__('mec')

        def calculate(self, graph):
            if nx.number_of_isolates(graph) < 1 < nx.number_of_nodes(graph):
                return len(nx.algorithms.covering.min_edge_cover(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            if nx.number_of_isolates(graph) < 1:
                return print_set(nx.algorithms.covering.min_edge_cover(graph), precision)
            else:
                return "Graph has isolate vertice."

    class NumberOfTriangles(Function, Invariant):

        def __init__(self):
            super().__init__('\u03A4')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1 and nx.number_of_edges(graph) > 1:
                return int(sum(nx.algorithms.cluster.triangles(graph).values()) / 3)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class WienerIndex(Function, Invariant):

        def __init__(self):
            super().__init__('W')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(nx.wiener_index(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)
