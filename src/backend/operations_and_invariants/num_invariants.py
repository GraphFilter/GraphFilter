import grinpy as gp
import networkx as nx
import numpy as np
import numpy.linalg as la
import scipy.sparse as ss
from operations_and_invariants.bool_invariants import Utils


class InvariantNum:
    calculate = None
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        self.all = InvariantNum.__subclasses__()
        for inv in self.all:
            for j in range(0, len(inv.code)):
                self.dic_function[inv.code[j]] = inv.calculate

    name = None

    @staticmethod
    def calculate(graph):
        pass


class ChromaticNumber(InvariantNum):
    name = "Chromatic number"
    code = ['chi']

    @staticmethod
    def calculate(graph):
        return gp.chromatic_number(graph)


class NumberVertices(InvariantNum):
    name = "Number of vertices"
    code = ['n']

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)


class NumberEdges(InvariantNum):
    name = "Number of edges"
    code = ['m']

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)


class CliqueNumber(InvariantNum):
    name = "Clique Number"
    code = ['omega']

    @staticmethod
    def calculate(graph):
        return gp.clique_number(graph)


class IndependenceNumber(InvariantNum):
    name = "Independence Number"
    code = ['alpha']

    @staticmethod
    def calculate(graph):
        return gp.independence_number(graph)


class DominationNumber(InvariantNum):
    name = "Domination Number"
    code = ['gamma']

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)


class TotalDominationNumber(InvariantNum):
    name = "Total Domination Number"
    code = ['gamma']

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


class ConnectedDominationNumber(InvariantNum):
    name = "Connected Domination Number"
    code = ['d']

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


# NOTE: Analyze whether it will be relevant
# class IndependentDominationNumber(Invariant_num):
#     name = "Independent Domination Number"
#     code = ['idom']
#
#     @staticmethod
#     def calculate(graph):
#         return gp.independent_domination_number(graph)
#
#
# class PowerDominationNumber(Invariant_num):
#     name = "Power Domination Number"
#     code = ['pdom']
#
#     @staticmethod
#     def calculate(graph):
#         return gp.power_domination_number(graph)
#
#
# class ZeroForcingNumber(Invariant_num):
#     name = "Zero Forcing Number"
#     code = ['zeroForcing']
#
#     @staticmethod
#     def calculate(graph):
#         return gp.zero_forcing_number(graph)
#
#
# class TotalZeroForcingNumber(Invariant_num):
#     name = "Total Zero Forcing Number"
#     code = ['tZeroForcing']
#
#     @staticmethod
#     def calculate(graph):
#         return gp.total_zero_forcing_number(graph)
#
#
# class ConnectedZeroForcingNumber(Invariant_num):
#     name = "Connected zero Forcing Number"
#     code = ['cZeroForcing']
#
#     @staticmethod
#     def calculate(graph):
#         return gp.connected_zero_forcing_number(graph)


class MatchingNumber(InvariantNum):
    name = "Matching Number"
    code = ['match', 'nu']

    @staticmethod
    def calculate(graph):
        return gp.matching_number(graph)


class VertexConnectivity(InvariantNum):
    name = "Vertex Connectivity"
    code = ['kappa']

    @staticmethod
    def calculate(graph):
        return gp.node_connectivity(graph)


class EdgeConnectivity(InvariantNum):
    name = "Edge Connectivity"
    code = ['econ']

    @staticmethod
    def calculate(graph):
        return nx.edge_connectivity(graph)


class NumberComponnents(InvariantNum):
    name = "Number of componnents"
    code = ['w']

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)


class Valency(InvariantNum):
    name = 'Valency'
    code = ['val']

    @staticmethod
    def calculate(graph):
        degSeq = gp.degree_sequence(graph)
        valencies = []
        for i in range(0, nx.number_of_nodes(graph)):
            if degSeq[i] not in valencies:
                valencies.append(degSeq[i])
        return len(valencies)


class DegreeMax(InvariantNum):
    name = "Maximum Degree"
    code = ['Delta']

    @staticmethod
    def calculate(graph):
        return np.max(gp.degree_sequence(graph))


class DegreeMin(InvariantNum):
    name = "Minimum Degree"
    code = ['delta']

    @staticmethod
    def calculate(graph):
        return np.min(gp.degree_sequence(graph))


class DegreeAverage(InvariantNum):
    name = "Average Degree"
    code = ['avgDegree']

    @staticmethod
    def calculate(graph):
        return np.average(gp.degree_sequence(graph))


class VertexCover(InvariantNum):
    name = "Vertex Cover Number"
    code = ['tau']

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)


class Diameter(InvariantNum):
    name = "Diameter"
    code = ["diam"]

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return nx.diameter(graph)
        else:
            return 10 ^ 10


class Radius(InvariantNum):
    name = "Radius"
    code = ["r"]

    @staticmethod
    def calculate(graph):
        return nx.diameter(graph)


class Largest1EigenA(InvariantNum):
    name = "Largest A-eigenvalue"
    code = ["eigen1A"]

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.ApproxToInt(la.eigvalsh(m)[nx.number_of_nodes(graph) - 1])


class Largest1EigenL(InvariantNum):
    name = "Largest L-eigenvalue"
    code = ["eigen1L"]

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.ApproxToInt(la.eigvalsh(m)[nx.number_of_nodes(graph) - 1])


class Largest1EigenQ(InvariantNum):
    name = "Largest Q-eigenvalue"
    code = ["eigen1Q"]

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.ApproxToInt(la.eigvalsh(np.abs(m))[nx.number_of_nodes(graph) - 1])


class Largest1EigenD(InvariantNum):
    name = "Largest D-eigenvalue"
    code = ["eigen1D"]

    @staticmethod
    def calculate(graph):
        return Utils.ApproxToInt(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])


class AlgebraicConnectivity(InvariantNum):
    name = 'Algebraic Connectivity'
    code = ['a']

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.ApproxToInt(la.eigvalsh(m)[1])


class WienerIndex(InvariantNum):
    name = 'Wiener Index'
    code = ['wiener']

    @staticmethod
    def calculate(graph):
        return Utils.ApproxToInt(nx.wiener_index(graph))


class EstradaIndex(InvariantNum):
    name = 'Estrada index'
    code = ['estrada']

    @staticmethod
    def calculate(graph):
        return Utils.ApproxToInt(nx.estrada_index(graph))


class Nullity(InvariantNum):
    name = 'Nullity'
    code = ['null']

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph) - la.matrix_rank(nx.adj_matrix(graph))


class NumberSpanningTree(InvariantNum):
    name = 'Number of spanning trees'
    code = ['t']

    @staticmethod
    def submatrix(m):
        n = m.shape[0]
        new = np.zeros((n - 1, n - 1))
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                new[i, j] = m[i + 1, j + 1]
        return new

    @staticmethod
    def calculate(graph):
        return la.det(NumberSpanningTree.submatrix(nx.laplacian_matrix(graph)))


class Density(InvariantNum):
    name = 'Density'
    code = ['den']

    @staticmethod
    def calculate(graph):
        return nx.density(graph)


if __name__ == '__main__':
    a = np.arange(16).reshape(4, 4)
    a = np.delete(a, 0, 0)
    matrix = np.delete(a, 0, 1)
    print(a)
