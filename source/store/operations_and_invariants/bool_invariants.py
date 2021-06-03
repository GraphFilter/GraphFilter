import networkx as nx
import grinpy as gp
import numpy.linalg as la
import numpy as np
import scipy.sparse as ss
from source.store.operations_and_invariants.invariants import Invariant
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils
import source.store.operations_and_invariants.other_invariants as inv_other


class InvariantBool(Invariant):
    name = None
    type = None

    def __init__(self):
        self.all = InvariantBool.__subclasses__()
        self.dic_name_inv: {str: InvariantBool}
        self.dic_name_inv_structural: {str: InvariantBool} = {}
        self.dic_name_inv_spectral: {str: InvariantBool} = {}
        for inv in self.all:
            inv.is_a_function = False
            if inv.type == 'bool_structural':
                self.dic_name_inv_structural[inv.name] = inv
            elif inv.type == 'bool_spectral':
                self.dic_name_inv_spectral[inv.name] = inv
        self.dic_name_inv = {**self.dic_name_inv_structural, **self.dic_name_inv_spectral}

    @staticmethod
    def calculate(**kwargs):
        pass


class Planar(InvariantBool):
    name = "Planar"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)[0]


class Connected(InvariantBool):
    name = "Connected"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)


class Biconnected(InvariantBool):
    name = "Biconnected"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)


class Bipartite(InvariantBool):
    name = 'Bipartite'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)


class Eulerian(InvariantBool):
    name = 'Eulerian'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)


class Chordal(InvariantBool):
    name = 'Chordal'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal(graph)


class TriangleFree(InvariantBool):
    name = 'Triangle-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)


class BullFree(InvariantBool):
    name = 'Bull-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_bull_free(graph)


class Regular(InvariantBool):
    name = 'Regular'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)


class ClawFree(InvariantBool):
    name = 'Claw-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_claw_free(graph)


class Tree(InvariantBool):
    name = 'Tree'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_tree(graph)


class SelfComplementary(InvariantBool):
    name = 'Self-complementary'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_isomorphic(graph, nx.complement(graph))


class Cubic(InvariantBool):
    name = 'Cubic'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_k_regular(graph, k=3)


class HasBridge(InvariantBool):
    name = 'Has bridge'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.has_bridges(graph)


class SomeEigenIntegerA(InvariantBool):
    name = 'Some A-eigenvalue integer'
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerL(InvariantBool):
    name = "Some L-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerQ(InvariantBool):
    name = "Some Q-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.is_there_integer(la.eigvalsh(matrix))


class SomeEigenIntegerD(InvariantBool):
    name = "Some D-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_there_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph)))
        else:
            return False


class IntegralA(InvariantBool):
    name = "A-integral"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralL(InvariantBool):
    name = "L-integral"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralQ(InvariantBool):
    name = "Q-integral"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.integral(la.eigvalsh(matrix))


class IntegralD(InvariantBool):
    name = "D-integral"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(la.eigvalsh(nx.floyd_warshall_numpy(graph)))
        else:
            return False


class LargestEigenIntegerA(InvariantBool):
    name = "Largest A-eigenvalue is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.adj_matrix(graph))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerL(InvariantBool):
    name = "Largest L-eigenvalue is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(nx.laplacian_matrix(graph))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerQ(InvariantBool):
    name = "Largest Q-eigenvalue is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        matrix = ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))
        return Utils.is_integer(la.eigvalsh(matrix)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerD(InvariantBool):
    name = "Largest D-eigenvalue is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_integer(la.eigvalsh(nx.floyd_warshall_numpy(graph))[nx.number_of_nodes(graph) - 1])
        else:
            return False


class RegularTransmission(InvariantBool):
    name = "Regular Transmission"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            dist_matrix = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
            transmission = [sum(dist_matrix[:, i]) for i in range(0, dist_matrix.shape[0])]
            return bool(max(transmission) == min(transmission))
        else:
            return False


class InvertibleMatrixA(InvariantBool):
    name = "Adjacency matrix is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.AdjacencyMatrix.calculate(graph))) != 0)


class InvertibleMatrixL(InvariantBool):
    name = "Laplacian matrix is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.LaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixQ(InvariantBool):
    name = "Signless Lap matrix is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.SignlessLaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixN(InvariantBool):
    name = "Normalized lap matrix is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.NormalizedLaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixD(InvariantBool):
    name = "Distance matrix is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return bool(Utils.approx_to_int(la.det(inv_other.DistanceMatrix.calculate(graph))) != 0)
        else:
            return False
