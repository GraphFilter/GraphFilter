import networkx as nx
import numpy as np
import numpy.linalg as la
import grinpy as gp

from source.domain.entities import MatrixInvariants
from source.domain.objects.function_object import FunctionObject
from source.domain.entities.invariants.utils import print_numeric, print_set, approx_to_int
from source.domain.entities.invariants import Invariant


class NumericStructuralInvariants:
    class NumberVertices(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Number of vertices", code='n')

        def calculate(self, graph):
            return nx.number_of_nodes(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class NumberEdges(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Number of edges", code='\u0415')

        def calculate(self, graph):
            return nx.number_of_edges(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class CliqueNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Clique number", code='\u03c9')

        def calculate(self, graph):
            return len(set(nx.max_weight_clique(graph, weight=None)[0]))

        def print(self, graph, precision):
            return print_set(set(nx.max_weight_clique(graph, weight=None)[0]), precision)

    class IndependenceNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Independence number", code='\u237a')

        def calculate(self, graph):
            return NumericStructuralInvariants.CliqueNumber().calculate(nx.complement(graph))

        def print(self, graph, precision):
            return NumericStructuralInvariants.CliqueNumber().print(nx.complement(graph), precision)

    class DominationNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Domination number", code='\u0194')

        def calculate(self, graph):
            return gp.domination_number(graph)

        def print(self, graph, precision):
            return print_numeric(gp.domination_number(graph), precision)

    class ChromaticNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Chromatic number (estimated)", code='\u03c7')

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

    class GirthNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Girth", code='\u0261')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return len(nx.minimum_cycle_basis(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MatchingNumber(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Matching number", code='\u03bd')

        def calculate(self, graph):
            return NumericStructuralInvariants.IndependenceNumber().calculate(nx.line_graph(graph))

        def print(self, graph, precision):
            return NumericStructuralInvariants.IndependenceNumber().print(nx.line_graph(graph), precision)

    class NumberComponents(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Number of components", code='w')

        def calculate(self, graph):
            return nx.number_connected_components(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Valency(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Degree regularity', code='d\u1d63')

        def calculate(self, graph):
            deg_seq = gp.degree_sequence(graph)
            valencies = []
            for i in range(0, nx.number_of_nodes(graph)):
                if deg_seq[i] not in valencies:
                    valencies.append(deg_seq[i])
            return len(valencies)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeMax(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Maximum degree", code='\u0394')

        def calculate(self, graph):
            return max(gp.degree_sequence(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeMin(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Minimum degree", code='\u1e9f')

        def calculate(self, graph):
            return min(gp.degree_sequence(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeAverage(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Average degree", code='d\u2090')

        def calculate(self, graph):
            sequence = gp.degree_sequence(graph)
            return sum(sequence) / len(sequence)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class VertexCover(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Vertex cover number", code='\u03c4')

        def calculate(self, graph):
            return gp.vertex_cover_number(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Diameter(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Diameter", code="diam")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return nx.diameter(graph)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Radius(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Radius", code="r")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return nx.radius(graph)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class KirchhoffIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Kirchhoff Index', code='Kf')

        def calculate(self, graph):
            if nx.is_connected(graph):
                l_eigen = MatrixInvariants.LaplacianSpectrum.calculate(graph)
                return nx.number_of_nodes(graph) * sum(1 / x for x in l_eigen[1:])
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DegreeKirchhoffIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Degree Kirchhoff Index', code='K`f')

        def calculate(self, graph):
            if nx.is_connected(graph):
                n_eigen = MatrixInvariants.NormalizedLaplacianSpectrum.calculate(graph)
                return 2 * nx.number_of_edges(graph) * sum(1 / x for x in n_eigen[1:])
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RandicIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Randic Index', code="Ri")

        def calculate(self, graph):
            randic = MatrixInvariants.RandicMatrix.calculate(graph)
            s = 0
            size = nx.number_of_nodes(graph)
            for i in range(size):
                for j in range(i + 1, size):
                    s += randic[i][j]
            return s

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class NumberSpanningTree(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Number of spanning trees', code='\u0288')

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

    class Density(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Density', code='\u018a')

        def calculate(self, graph):
            return nx.density(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class VertexConnectivity(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Vertex connectivity", code='\u03f0')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return gp.node_connectivity(graph)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EdgeConnectivity(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Edge connectivity", code='\u03bb')

        def calculate(self, graph):
            return nx.edge_connectivity(graph)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class ChromaticIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Chromatic Index (estimated)", code="\u03c7'")

        def calculate(self, graph):
            return NumericStructuralInvariants.ChromaticNumber().calculate(nx.line_graph(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MinimumEdgeCover(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Minimum edge cover number", code='mec')

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

    class NumberOfTriangles(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Number of triangles", code='\u03A4')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1 and nx.number_of_edges(graph) > 1:
                return int(sum(nx.algorithms.cluster.triangles(graph).values()) / 3)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class WienerIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Wiener index', code='W')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(nx.wiener_index(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)
