import grinpy as gp
import networkx as nx
import numpy.linalg as la

import source.store.operations_and_invariants.other_invariants as inv_other
from source.store.operations_and_invariants.invariants import Invariant
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils


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
    name = 'Some A-eigenvalue integer\n(Adjacency)'
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.AdjacencySpectrum.calculate(graph))


class SomeEigenIntegerL(InvariantBool):
    name = "Some L-eigenvalue integer\n(Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.LaplacianSpectrum.calculate(graph))


class SomeEigenIntegerQ(InvariantBool):
    name = "Some Q-eigenvalue integer\n(Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.SignlessLaplacianSpectrum.calculate(graph))



class SomeEigenIntegerN(InvariantBool):
    name = "Some N-eigenvalue integer\n(Normalized Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.NormalizedLaplacianSpectrum.calculate(graph))



    class SomeEigenIntegerD(InvariantBool):
        name = "Some D-eigenvalue integer\n(Distance)"
        type = 'bool_spectral'

        @staticmethod
        def calculate(graph):
            if nx.is_connected(graph):
                return Utils.is_there_integer(inv_other.DistanceSpectrum.calculate(graph))
            else:
                return False


class IntegralA(InvariantBool):
    name = "A-integral (Adjacency)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.AdjacencySpectrum.calculate(graph))


class IntegralL(InvariantBool):
    name = "L-integral (Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.LaplacianSpectrum.calculate(graph))


class IntegralQ(InvariantBool):
    name = "Q-integral (Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.SignlessLaplacianSpectrum.calculate(graph))


class IntegralD(InvariantBool):
    name = "D-integral (Distance)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.DistanceSpectrum.calculate(graph))
        else:
            return False

class IntegralN(InvariantBool):
    name = "N-integral (Normalized Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.NormalizedLaplacianSpectrum.calculate(graph))
        else:
            return False


class LargestEigenIntegerA(InvariantBool):
    name = "Largest A-eigenvalue is integer\n(Adjacency)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.AdjacencySpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerL(InvariantBool):
    name = "Largest L-eigenvalue is integer\n(Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.LaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerQ(InvariantBool):
    name = "Largest Q-eigenvalue is integer\n(Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.SignlessLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class LargestEigenIntegerD(InvariantBool):
    name = "Largest D-eigenvalue is integer\n(Distance Matrix)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_integer(inv_other.DistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])
        else:
            return False

class LargestEigenIntegerN(InvariantBool):
    name = "Largest N-eigenvalue is integer\n(Normalized Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.NormalizedLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


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
    name = "A is invertible\n(Adjacency)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.AdjacencyMatrix.calculate(graph))) != 0)


class InvertibleMatrixL(InvariantBool):
    name = "L is invertible\n(Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.LaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixQ(InvariantBool):
    name = "Q is invertible\n(Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.SignlessLaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixN(InvariantBool):
    name = "N is invertible\n(Normalized Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.NormalizedLaplacianMatrix.calculate(graph))) != 0)


class InvertibleMatrixD(InvariantBool):
    name = "D is invertible\n(Distance)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return bool(Utils.approx_to_int(la.det(inv_other.DistanceMatrix.calculate(graph))) != 0)
        else:
            return False
