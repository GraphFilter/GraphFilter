import networkx as nx
import grinpy as gp
import numpy.linalg as la
import numpy as np
import scipy.sparse as ss


class InvariantBool:

    def __init__(self):
        self.all = InvariantBool.__subclasses__()

    name = None
    link = None
    implement = None
    error = 0.00001

    @staticmethod
    def calculate(**kwargs):
        pass


class Planar(InvariantBool):
    name = "planar"

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)[0]


class Connected(InvariantBool):
    name = "connected"

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)


class Biconnected(InvariantBool):
    name = "biconnected"

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)


class Bipartite(InvariantBool):
    name = 'bipartite'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)


class Eulerian(InvariantBool):
    name = 'Eulerian'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)


class Chordal(InvariantBool):
    name = 'Chordal'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal(graph)


class Triangle_free(InvariantBool):
    name = 'Triangle-free'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)


class Regular(InvariantBool):
    name = 'Regular'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)


class Clawfree(InvariantBool):
    name = 'Claw-free'

    @staticmethod
    def calculate(graph):
        return gp.is_claw_free(graph)


class Tree(InvariantBool):
    name = 'Tree'

    @staticmethod
    def calculate(graph):
        return nx.is_tree(graph)


class KRegular(InvariantBool):
    name = 'k-regular'

    @staticmethod
    def calculate(graph, k):
        return gp.is_k_regular(graph, k=k)


class SomeEigenIntegerA(InvariantBool):
    name = 'Some A-eigenvalue integer'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.IsThereInteger(la.eigvalsh(matrix))


class SomeEigenIntegerL(InvariantBool):
    name = "Some L-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.IsThereInteger(la.eigvalsh(matrix))


class SomeEigenIntegerQ(InvariantBool):
    name = "Some Q-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.IsThereInteger(la.eigvalsh(matrix))


class SomeEigenIntegerD(InvariantBool):
    name = "Some D-eigenvalue integer"

    @staticmethod
    def calculate(graph):
        return Utils.IsThereInteger(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class IntegralA(InvariantBool):
    name = "A-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.Integral(la.eigvalsh(matrix))


class IntegralL(InvariantBool):
    name = "L-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.Integral(la.eigvalsh(matrix))


class IntegralQ(InvariantBool):
    name = "Q-integral"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.Integral(la.eigvalsh(matrix))


class integralD(InvariantBool):
    name = "D-integral"

    @staticmethod
    def calculate(graph):
        return Utils.Integral(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class LargestEigenIntegerA(InvariantBool):
    name = "Largest A-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.IsInteger(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerL(InvariantBool):
    name = "Largest L-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.IsInteger(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerQ(InvariantBool):
    name = "Largest Q-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.IsInteger(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerD(InvariantBool):
    name = "Largest D-eigenvalue is integer"

    @staticmethod
    def calculate(graph):
        return Utils.IsInteger(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])


class Utils:

    @staticmethod
    def ApproxToInt(number, error=0.00001):
        if abs(round(number) - number) <= error:
            return float(round(number))
        else:
            return number

    @staticmethod
    def IsThereInteger(list):
        for number in list:
            if Utils.ApproxToInt(number).is_integer():
                return True
        return False

    @staticmethod
    def IsInteger(number):
        return Utils.ApproxToInt(number).is_integer()

    @staticmethod
    def Integral(list):
        for number in list:
            if not Utils.ApproxToInt(number).is_integer():
                return False
        return True
