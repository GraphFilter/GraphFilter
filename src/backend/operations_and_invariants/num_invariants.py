import grinpy as gp
import networkx as nx
import numpy as np
import numpy.linalg as la
import scipy.sparse as ss
from src.backend.operations_and_invariants.bool_invariants import Utils


class InvariantNum:
    code = None
    dic_function = {}
    dic_translate = {}
    all = []
    name = None
    code_literal = None

    def __init__(self):
        self.all = InvariantNum.__subclasses__()
        for i, invar in enumerate(self.all):
            invar.code_literal = 'F' + str(i)
            self.dic_function[invar.code_literal] = invar.calculate

    @staticmethod
    def calculate(graph):
        pass


class ChromaticNumber(InvariantNum):
    name = "Chromatic number"
    code = '\u1d61'

    @staticmethod
    def calculate(graph):
        return gp.chromatic_number(graph)


class NumberVertices(InvariantNum):
    name = "Number of vertices"
    code = 'n'

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)


class NumberEdges(InvariantNum):
    name = "Number of edges"
    code = '\u0415'

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)


class CliqueNumber(InvariantNum):
    name = "Clique Number"
    code = '\u03c9'

    @staticmethod
    def calculate(graph):
        return gp.clique_number(graph)


class IndependenceNumber(InvariantNum):
    name = "Independence Number"
    code = '\u237a'

    @staticmethod
    def calculate(graph):
        return gp.independence_number(graph)


class DominationNumber(InvariantNum):
    name = "Domination Number"
    code = '\u0194'

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)


class TotalDominationNumber(InvariantNum):
    name = "Total Domination Number"
    code = '\u0194<sub>t</sub>'

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


class ConnectedDominationNumber(InvariantNum):
    name = "Connected Domination Number"
    code = 'd'

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
    code = '\u03bd'

    @staticmethod
    def calculate(graph):
        return gp.matching_number(graph)


class NumberComponnents(InvariantNum):
    name = "Number of components"
    code = 'w'

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)


class Valency(InvariantNum):
    name = 'Degree regularity'
    code = 'd<sub>r</sub>'

    @staticmethod
    def calculate(graph):
        deg_seq = gp.degree_sequence(graph)
        valencies = []
        for i in range(0, nx.number_of_nodes(graph)):
            if deg_seq[i] not in valencies:
                valencies.append(deg_seq[i])
        return len(valencies)


class DegreeMax(InvariantNum):
    name = "Maximum Degree"
    code = '\u0394'

    @staticmethod
    def calculate(graph):
        return np.max(gp.degree_sequence(graph))


class DegreeMin(InvariantNum):
    name = "Minimum Degree"
    code = '\u1e9f'

    @staticmethod
    def calculate(graph):
        return np.min(gp.degree_sequence(graph))


class DegreeAverage(InvariantNum):
    name = "Average Degree"
    code = 'd<sub>a</sub>'

    @staticmethod
    def calculate(graph):
        return np.average(gp.degree_sequence(graph))


class VertexCover(InvariantNum):
    name = "Vertex Cover Number"
    code = '\u03c4'

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)


class Diameter(InvariantNum):
    name = "Diameter"
    code = "diam"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return nx.diameter(graph)
        else:
            return 10 ^ 10


class Radius(InvariantNum):
    name = "Radius"
    code = "r"

    @staticmethod
    def calculate(graph):
        return nx.diameter(graph)


class Largest1EigenA(InvariantNum):
    name = "Largest A-eigenvalue"
    code = "\u03bb\u2081"

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.approx_to_int(la.eigvalsh(m)[nx.number_of_nodes(graph) - 1])


class Largest1EigenL(InvariantNum):
    name = "Largest L-eigenvalue"
    code = "\u03bc<sub>1</sub>"

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.approx_to_int(la.eigvalsh(m)[nx.number_of_nodes(graph) - 1])


class Largest1EigenQ(InvariantNum):
    name = "Largest Q-eigenvalue"
    code = "q<sub>1</sub>"

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.approx_to_int(la.eigvalsh(np.abs(m))[nx.number_of_nodes(graph) - 1])


class Largest1EigenD(InvariantNum):
    name = "Largest D-eigenvalue"
    code = "\u0398<sub>1</sub>"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])


class AlgebraicConnectivity(InvariantNum):
    name = 'Algebraic Connectivity'
    code = 'ac'

    @staticmethod
    def calculate(graph):
        m = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.approx_to_int(la.eigvalsh(m)[1])


class VertexConnectivity(InvariantNum):
    name = "Vertex Connectivity"
    code = '\u03f0'

    @staticmethod
    def calculate(graph):
        return gp.node_connectivity(graph)


class EdgeConnectivity(InvariantNum):
    name = "Edge Connectivity"
    code = '\u03bb'

    @staticmethod
    def calculate(graph):
        return nx.edge_connectivity(graph)


class WienerIndex(InvariantNum):
    name = 'Wiener Index'
    code = 'W'

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(nx.wiener_index(graph))


class EstradaIndex(InvariantNum):
    name = 'Estrada index'
    code = 'EE'

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(nx.estrada_index(graph))


class Nullity(InvariantNum):
    name = 'Nullity'
    code = '\u03b7'

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph) - la.matrix_rank(nx.adj_matrix(graph))


class NumberSpanningTree(InvariantNum):
    name = 'Number of spanning trees'
    code = '\u0288'

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
    code = '\u018a'

    @staticmethod
    def calculate(graph):
        return nx.density(graph)


if __name__ == '__main__':
    inv = InvariantNum()
    print(inv.dic_translate)
