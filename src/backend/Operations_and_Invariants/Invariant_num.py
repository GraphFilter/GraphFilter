import grinpy as gp
import networkx as nx
import numpy as np
import numpy.linalg as la
import scipy.sparse as ss
from Operations_and_Invariants.Invariant_bool import Utils


class Invariant_num:
    calculate = None
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        self.all = Invariant_num.__subclasses__()
        for inv in self.all:
            for j in range(0, len(inv.code)):
                self.dic_function[inv.code[j]] = inv.calculate

    name = None

    @staticmethod
    def Calculate(graph):
        pass


class Chromatic_number(Invariant_num):
    name = "Chromatic number"
    code = ['chi']

    @staticmethod
    def calculate(graph):
        return gp.chromatic_number(graph)


class Number_of_vertices(Invariant_num):
    name = "Number of vertices"
    code = ['n']

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)


class Number_of_edges(Invariant_num):
    name = "Number of edges"
    code = ['m']

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)


class Clique_Number(Invariant_num):
    name = "Clique Number"
    code = ['omega']

    @staticmethod
    def calculate(graph):
        return gp.clique_number(graph)


class Independence_Number(Invariant_num):
    name = "Independence Number"
    code = ['alpha']

    @staticmethod
    def calculate(graph):
        return gp.independence_number(graph)


class Domination_Number(Invariant_num):
    name = "Domination Number"
    code = ['gamma']

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)


class Total_Domination_Number(Invariant_num):
    name = "Total Domination Number"
    code = ['gammat']

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


class Connected_domination_number(Invariant_num):
    name = "Connected Domination Number"
    code = ['d']

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


'''
class Independent_domination_number(Invariant_num):
    name = "Independent Domination Number"
    code = ['idom']

    @staticmethod
    def calculate(graph):
        return gp.independent_domination_number(graph)


class Power_Domination_Number(Invariant_num):
    name = "Power Domination Number"
    code = ['pdom']

    @staticmethod
    def calculate(graph):
        return gp.power_domination_number(graph)


class Zero_Forcing_Number(Invariant_num):
    name = "Zero Forcing Number"
    code = ['zeroForcing']

    @staticmethod
    def calculate(graph):
        return gp.zero_forcing_number(graph)


class Total_Zero_Forcing_Number(Invariant_num):
    name = "Total Zero Forcing Number"
    code = ['tZeroForcing']

    @staticmethod
    def calculate(graph):
        return gp.total_zero_forcing_number(graph)


class Connected_Zero_forcing_number(Invariant_num):
    name = "Connected zero Forcing Number"
    code = ['cZeroForcing']

    @staticmethod
    def calculate(graph):
        return gp.connected_zero_forcing_number(graph)
'''


class MatchingNumber(Invariant_num):
    name = "Matching Number"
    code = ['match', 'nu']

    @staticmethod
    def calculate(graph):
        return gp.matching_number(graph)


class Vertex_Connectivity(Invariant_num):
    name = "Vertex Connectivity"
    code = ['kappa']

    @staticmethod
    def calculate(graph):
        return gp.node_connectivity(graph)


class Edge_Connectivity(Invariant_num):
    name = "Edge Connectivity"
    code = ['econ']

    @staticmethod
    def calculate(graph):
        return nx.edge_connectivity(graph)


class Number_Componnents(Invariant_num):
    name = "Number of componnents"
    code = ['w']

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)


class Valency(Invariant_num):
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


class Degree_Max(Invariant_num):
    name = "Maximum Degree"
    code = ['Delta']

    @staticmethod
    def calculate(graph):
        return np.max(gp.degree_sequence(graph))


class Degree_Min(Invariant_num):
    name = "Minimum Degree"
    code = ['delta']

    @staticmethod
    def calculate(graph):
        return np.min(gp.degree_sequence(graph))


class Degree_Avg(Invariant_num):
    name = "Average Degree"
    code = ['avgDegree']

    @staticmethod
    def calculate(graph):
        return np.average(gp.degree_sequence(graph))


class Vertex_Cover(Invariant_num):
    name = "Vertex Cover Number"
    code = ['tau']

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)


class Diameter(Invariant_num):
    name = "Diameter"
    code = ["diam"]

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return nx.diameter(graph)
        else:
            return 10^10


class Radius(Invariant_num):
    name = "Radius"
    code = ["r"]

    @staticmethod
    def calculate(graph):
        return nx.diameter(graph)


class Largest_1_Eigen_A(Invariant_num):
    name = "Largest A-eigenvalue"
    code = ["eigen1A"]

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.Approx_to_int(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])

class Largest_1_Eigen_L(Invariant_num):
    name = "Largest L-eigenvalue"
    code = ["eigen1L"]

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Approx_to_int(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class Largest_1_Eigen_Q(Invariant_num):
    name = "Largest Q-eigenvalue"
    code = ["eigen1Q"]

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.Approx_to_int(la.eigvalsh(np.abs(matrix))[nx.number_of_nodes(graph) - 1])


class Largest_1_Eigen_D(Invariant_num):
    name = "Largest D-eigenvalue"
    code = ["eigen1D"]

    @staticmethod
    def calculate(graph):
        return Utils.Approx_to_int(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])


class AlgebraicConnectivity(Invariant_num):
    name = 'Algebraic Connectivity'
    code = ['a']

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Approx_to_int(la.eigvalsh(matrix)[1])


class WienerIndex(Invariant_num):
    name = 'Wiener Index'
    code = ['wiener']

    @staticmethod
    def calculate(graph):
        return Utils.Approx_to_int(nx.wiener_index(graph))


class EstradaIndex(Invariant_num):
    name = 'Estrada index'
    code = ['estrada']

    @staticmethod
    def calculate(graph):
        return Utils.Approx_to_int(nx.estrada_index(graph))


class Nullity(Invariant_num):
    name = 'Nullity'
    code = ['null']

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph) - la.matrix_rank(nx.adj_matrix(graph))


class NumberOfSpanningTree(Invariant_num):
    name = 'Number of spanning trees'
    code = ['t']

    @staticmethod
    def submatrix(matrix):
        n = matrix.shape[0]
        new = np.zeros((n-1, n-1))
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                new[i, j] = matrix[i + 1, j + 1]
        return new

    @staticmethod
    def calculate(graph):
        return la.det(NumberOfSpanningTree.submatrix(nx.laplacian_matrix(graph)))


class Density(Invariant_num):
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
