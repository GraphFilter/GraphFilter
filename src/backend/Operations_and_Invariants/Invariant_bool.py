import networkx as nx
import grinpy as gp
import numpy.linalg as la
import numpy as np
import scipy.sparse as ss


class Invariant_bool:

    def __init__(self):
        self.all = Invariant_bool.__subclasses__()

    name = None
    link = None
    implement = None
    error = 0.00001

    @staticmethod
    def calculate(**kwargs):
        pass


class planar(Invariant_bool):
    name = "planar"

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)[0]


class connected(Invariant_bool):
    name = "connected"

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)


class biconnected(Invariant_bool):
    name = "biconnected"

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)


class bipartite(Invariant_bool):
    name = 'bipartite'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)


class eulerian(Invariant_bool):
    name = 'Eulerian'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)


class chordal(Invariant_bool):
    name = 'Chordal'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal(graph)


class triangle_free(Invariant_bool):
    name = 'Triangle-free'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)


class regular(Invariant_bool):
    name = 'Regular'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)


class clawfree(Invariant_bool):
    name = 'Claw-free'

    @staticmethod
    def calculate(graph):
        return gp.is_claw_free(graph)


class tree(Invariant_bool):
    name = 'Tree'

    @staticmethod
    def calculate(graph):
        return nx.is_tree(graph)


class k_Regular(Invariant_bool):
    name = 'k-regular'

    @staticmethod
    def calculate(graph, k):
        return gp.is_k_regular(graph, k=k)


class some_Aeigen_integer(Invariant_bool):
    name = 'Some A-eigenvalue integer'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.Is_there_a_integer(la.eigvalsh(matrix))


class some_Leigen_integer(Invariant_bool):
    name = "Some L-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Is_there_a_integer(la.eigvalsh(matrix))


class some_Qeigen_integer(Invariant_bool):
    name = "Some Q-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.Is_there_a_integer(la.eigvalsh(matrix))


class Some_Deigen_integer(Invariant_bool):
    name = "Some D-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        return Utils.Is_there_a_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class A_integral(Invariant_bool):
    name = "A-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.Integral(la.eigvalsh(matrix))


class L_integral(Invariant_bool):
    name = "L-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Integral(la.eigvalsh(matrix))


class Q_integral(Invariant_bool):
    name = "Q-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.Integral(la.eigvalsh(matrix))


class D_integral(Invariant_bool):
    name = "D-integral"

    @staticmethod
    def calculate(graph):
        return Utils.Integral(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class Largest_Aeigen_integer(Invariant_bool):
    name = "Largest A-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.Is_a_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class Largest_Leigen_integer(Invariant_bool):
    name = "Largest L-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Is_a_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class Largest_Qeigen_integer(Invariant_bool):
    name = "Largest Q-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.Is_a_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class Largest_Deigen_integer(Invariant_bool):
    name = "Largest D-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        return Utils.Is_a_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])


class Utils:

    @staticmethod
    def Approx_to_int(number, error=0.00001):
        if abs(round(number) - number) <= error:
            return float(round(number))
        else:
            return number

    @staticmethod
    def Is_there_a_integer(list):
        for number in list:
            if Utils.Approx_to_int(number).is_integer():
                return True
        return False

    @staticmethod
    def Is_a_integer(number):
        return Utils.Approx_to_int(number).is_integer()

    @staticmethod
    def Integral(list):
        for number in list:
            if not Utils.Approx_to_int(number).is_integer():
                return False
        return True
