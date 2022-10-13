import grinpy as gp
import networkx as nx
import networkx.algorithms.threshold
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

    @staticmethod
    def print(**kwargs):
        pass


class Planar(InvariantBool):
    name = "Planar"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)[0]

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Planar.calculate(graph), precision)


class Connected(InvariantBool):
    name = "Connected"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Connected.calculate(graph), precision)


class Biconnected(InvariantBool):
    name = "Biconnected"
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Biconnected.calculate(graph), precision)


class Bipartite(InvariantBool):
    name = 'Bipartite'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Bipartite.calculate(graph), precision)


class Eulerian(InvariantBool):
    name = 'Eulerian'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Eulerian.calculate(graph), precision)


class Chordal(InvariantBool):
    name = 'Chordal'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Chordal.calculate(graph), precision)


class TriangleFree(InvariantBool):
    name = 'Triangle-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(TriangleFree.calculate(graph), precision)


class BullFree(InvariantBool):
    name = 'Bull-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_bull_free(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(BullFree.calculate(graph), precision)


class Regular(InvariantBool):
    name = 'Regular'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Regular.calculate(graph), precision)


class ClawFree(InvariantBool):
    name = 'Claw-free'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_claw_free(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(ClawFree.calculate(graph), precision)


class Tree(InvariantBool):
    name = 'Tree'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_tree(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Tree.calculate(graph), precision)


class SelfComplementary(InvariantBool):
    name = 'Self-complementary'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.is_isomorphic(graph, nx.complement(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SelfComplementary.calculate(graph), precision)


class Cubic(InvariantBool):
    name = 'Cubic'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return gp.is_k_regular(graph, k=3)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Cubic.calculate(graph), precision)


class HasBridge(InvariantBool):
    name = 'Has bridge'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.has_bridges(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(HasBridge.calculate(graph), precision)


class Threshold(InvariantBool):
    name = 'Is threshold'
    type = 'bool_structural'

    @staticmethod
    def calculate(graph):
        return nx.algorithms.threshold.is_threshold_graph(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(Threshold.calculate(graph), precision)

class SomeEigenIntegerA(InvariantBool):
    name = 'Some A-eigenvalue integer'
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.AdjacencySpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerA.calculate(graph), precision)


class SomeEigenIntegerL(InvariantBool):
    name = "Some L-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.LaplacianSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerL.calculate(graph), precision)


class SomeEigenIntegerQ(InvariantBool):
    name = "Some Q-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.SignlessLaplacianSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerQ.calculate(graph), precision)


class SomeEigenIntegerS(InvariantBool):
    name = "Some S-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.SeidelSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerS.calculate(graph), precision)


class SomeEigenIntegerN(InvariantBool):
    name = "Some N-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_there_integer(inv_other.NormalizedLaplacianSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerN.calculate(graph), precision)


class SomeEigenIntegerD(InvariantBool):
    name = "Some D-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_there_integer(inv_other.DistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerD.calculate(graph), precision)


class SomeEigenIntegerDL(InvariantBool):
    name = "Some DL-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_there_integer(inv_other.LaplacianDistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerDL.calculate(graph), precision)


class SomeEigenIntegerDQ(InvariantBool):
    name = "Some DQ-eigenvalue integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_there_integer(inv_other.SignlessLaplacianDistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(SomeEigenIntegerDQ.calculate(graph), precision)


class IntegralA(InvariantBool):
    name = "A-integral (Adjacency)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.AdjacencySpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralA.calculate(graph), precision)


class IntegralL(InvariantBool):
    name = "L-integral (Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.LaplacianSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralL.calculate(graph), precision)


class IntegralQ(InvariantBool):
    name = "Q-integral (Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.SignlessLaplacianSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralQ.calculate(graph), precision)


class IntegralN(InvariantBool):
    name = "N-integral (Normalized Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.NormalizedLaplacianSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralN.calculate(graph), precision)


class IntegralS(InvariantBool):
    name = "S-integral (Signless Laplacian)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.integral(inv_other.SeidelSpectrum.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralS.calculate(graph), precision)


class IntegralD(InvariantBool):
    name = "D-integral (Distance)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.DistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralD.calculate(graph), precision)


class IntegralDL(InvariantBool):
    name = "DL-integral (Distance)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.LaplacianDistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralDL.calculate(graph), precision)


class IntegralDQ(InvariantBool):
    name = "DQ-integral (Distance)"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.integral(inv_other.SignlessLaplacianDistanceSpectrum.calculate(graph))
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(IntegralDQ.calculate(graph), precision)


class LargestEigenIntegerA(InvariantBool):
    name = "Largest A-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.AdjacencySpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerA.calculate(graph), precision)


class LargestEigenIntegerL(InvariantBool):
    name = "Largest L-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.LaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerL.calculate(graph), precision)


class LargestEigenIntegerQ(InvariantBool):
    name = "Largest Q-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.SignlessLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerQ.calculate(graph), precision)


class LargestEigenIntegerS(InvariantBool):
    name = "Largest S-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.SeidelSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerS.calculate(graph), precision)


class LargestEigenIntegerD(InvariantBool):
    name = "Largest D-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_integer(inv_other.DistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerD.calculate(graph), precision)


class LargestEigenIntegerDL(InvariantBool):
    name = "Largest DL-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_integer(inv_other.LaplacianDistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerD.calculate(graph), precision)


class LargestEigenIntegerDQ(InvariantBool):
    name = "Largest DQ-eigen is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.is_integer(
                inv_other.SignlessLaplacianDistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerDQ.calculate(graph), precision)


class LargestEigenIntegerN(InvariantBool):
    name = "Largest N-eigenvalue is integer"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return Utils.is_integer(inv_other.NormalizedLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(LargestEigenIntegerN.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(RegularTransmission.calculate(graph), precision)


class InvertibleMatrixA(InvariantBool):
    name = "A is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.AdjacencyMatrix.calculate(graph))) != 0)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixA.calculate(graph), precision)


class InvertibleMatrixL(InvariantBool):
    name = "L is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.LaplacianMatrix.calculate(graph))) != 0)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixL.calculate(graph), precision)


class InvertibleMatrixQ(InvariantBool):
    name = "Q is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.SignlessLaplacianMatrix.calculate(graph))) != 0)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixQ.calculate(graph), precision)


class InvertibleMatrixN(InvariantBool):
    name = "N is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.NormalizedLaplacianMatrix.calculate(graph))) != 0)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixN.calculate(graph), precision)


class InvertibleMatrixD(InvariantBool):
    name = "D is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return bool(Utils.approx_to_int(la.det(inv_other.DistanceMatrix.calculate(graph))) != 0)
        else:
            return False

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixD.calculate(graph), precision)


class InvertibleMatrixS(InvariantBool):
    name = "S is invertible"
    type = 'bool_spectral'

    @staticmethod
    def calculate(graph):
        return bool(Utils.approx_to_int(la.det(inv_other.SeidelMatrix.calculate(graph))) != 0)

    @staticmethod
    def print(graph, precision):
        return Utils.print_boolean(InvertibleMatrixS.calculate(graph), precision)
