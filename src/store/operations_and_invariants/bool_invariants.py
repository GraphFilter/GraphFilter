import networkx as nx
import grinpy as gp
import numpy.linalg as la
import numpy as np
import scipy.sparse as ss
from src.store.operations_and_invariants.invariants import Invariant
from src.store.operations_and_invariants.invariants import Utils


class InvariantBool(Invariant):
    dic_name_inv = {}
    dic_name_inv_structural = {}
    dic_name_inv_spectral = {}
    name = None
    link = None
    implement = None
    error = 0.00001
    type = None

    def __init__(self):
        self.all = InvariantBool.__subclasses__()
        for inv in self.all:
            #self.dic_name_calc[inv.name] = inv.calculate
            if inv.type == 'structural':
                self.dic_name_inv_structural[inv.name] = inv
            elif inv.type == 'spectral':
                self.dic_name_inv_spectral[inv.name] = inv
        self.dic_name_inv = {**self.dic_name_inv_structural, **self.dic_name_inv_spectral}

    @staticmethod
    def calculate(**kwargs):
        pass


class Planar(InvariantBool):
    name = "Planar"
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)[0]


class Connected(InvariantBool):
    name = "Connected"
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)


class Biconnected(InvariantBool):
    name = "Biconnected"
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)


class Bipartite(InvariantBool):
    name = 'Bipartite'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)


class Eulerian(InvariantBool):
    name = 'Eulerian'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)


class Chordal(InvariantBool):
    name = 'Chordal'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal(graph)


class TriangleFree(InvariantBool):
    name = 'Triangle-free'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)


class Regular(InvariantBool):
    name = 'Regular'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)


class ClawFree(InvariantBool):
    name = 'Claw-free'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return gp.is_claw_free(graph)


class Tree(InvariantBool):
    name = 'Tree'
    type = 'structural'

    @staticmethod
    def calculate(graph):
        return nx.is_tree(graph)


# TODO: create k-regular in numeric invariant

# class KRegular(InvariantBool):
#     name = 'k-regular'
#
#     @staticmethod
#     def calculate(graph, k):
#         return gp.is_k_regular(graph, k=k)


class SomeEigenIntegerA(InvariantBool):
    name = 'Some A-eigenvalue integer'
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerL(InvariantBool):
    name = "Some L-eigenvalue integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerQ(InvariantBool):
    name = "Some Q-eigenvalue integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerD(InvariantBool):
    name = "Some D-eigenvalue integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class IntegralA(InvariantBool):
    name = "A-integral"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralL(InvariantBool):
    name = "L-integral"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralQ(InvariantBool):
    name = "Q-integral"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralD(InvariantBool):
    name = "D-integral"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(la.eigvalsh(nx.floyd_warshall_numpy(graph)))


class LargestEigenIntegerA(InvariantBool):
    name = "Largest A-eigenvalue is integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerL(InvariantBool):
    name = "Largest L-eigenvalue is integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerQ(InvariantBool):
    name = "Largest Q-eigenvalue is integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerD(InvariantBool):
    name = "Largest D-eigenvalue is integer"
    type = 'spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])

