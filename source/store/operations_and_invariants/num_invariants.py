import grinpy as gp
import networkx as nx
import numpy as np
import numpy.linalg as la
import itertools
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils
from source.store.operations_and_invariants.invariants import Invariant
import source.store.operations_and_invariants.other_invariants as inv_other


class InvariantNum(Invariant):
    code = None
    name = None
    code_literal = None

    def __init__(self):
        self.all = InvariantNum.__subclasses__()
        self.dic_function: {str: staticmethod} = {}
        self.dic_name_inv_structural: {str: InvariantNum} = {}
        self.dic_name_inv_spectral: {str: InvariantNum} = {}
        for i, inv in enumerate(self.all):
            inv.is_a_function = True
            inv.code_literal = 'F' + str(i)
            self.dic_function[inv.code_literal] = inv.calculate
            if inv.type == 'number_structural':
                self.dic_name_inv_structural[inv.name] = inv
            elif inv.type == 'number_spectral':
                self.dic_name_inv_spectral[inv.name] = inv
        self.dic_name_inv = {**self.dic_name_inv_structural, **self.dic_name_inv_spectral}

    @staticmethod
    def calculate(graph):
        pass


class ChromaticNumber(InvariantNum):
    name = "Chromatic number"
    code = '\u03c7'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return len(set(nx.greedy_color(graph).values()))


class NumberVertices(InvariantNum):
    name = "Number of vertices"
    code = 'n'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)


class NumberEdges(InvariantNum):
    name = "Number of edges"
    code = '\u0415'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)


class CliqueNumber(InvariantNum):
    name = "Clique number"
    code = '\u03c9'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.clique_number(graph)


class IndependenceNumber(InvariantNum):
    name = "Independence number"
    code = '\u237a'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.independence_number(graph)


class TotalDominationNumber(InvariantNum):
    name = "Total domination number"
    code = '\u0194\u209c'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)


class DominationNumber(InvariantNum):
    name = "Domination number"
    code = '\u0194'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)


class ConnectedDominationNumber(InvariantNum):
    name = "Connected domination number"
    code = '\u0194c'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.connected_domination_number(graph)


class GirthNumber(InvariantNum):
    name = "Girth"
    code = '\u0261'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return len(nx.minimum_cycle_basis(graph))
        else:
            return 10 ** 10


# class IndependentDominationNumber(InvariantNum):
#     name = "Independent Domination Number"
#     code = 'idom'
#     type = "number"
#
#     @staticmethod
#     def calculate(graph):
#         return gp.independent_domination_number(graph)

#
# class PowerDominationNumber(InvariantNum):
#     name = "Power Domination Number"
#     code = ['pdom']
#     type = "number"
#
#     @staticmethod
#     def calculate(graph):
#         return gp.power_domination_number(graph)


# class ZeroForcingNumber(InvariantNum):
#     name = "Zero Forcing Number"
#     code = ['zeroForcing']
#     type = "number"
#
#     @staticmethod
#     def calculate(graph):
#         return gp.zero_forcing_number(graph)


# class TotalZeroForcingNumber(InvariantNum):
#     name = "Total Zero Forcing Number"
#     code = ['tZeroForcing']
#     type = "number"
#
#     @staticmethod
#     def calculate(graph):
#         return gp.total_zero_forcing_number(graph)


# class ConnectedZeroForcingNumber(InvariantNum):
#     name = "Connected zero Forcing Number"
#     code = ['cZeroForcing']
#     type = "number"
#
#     @staticmethod
#     def calculate(graph):
#         return gp.connected_zero_forcing_number(graph)


class MatchingNumber(InvariantNum):
    name = "Matching number"
    code = '\u03bd'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.matching_number(graph)


class NumberComponnents(InvariantNum):
    name = "Number of components"
    code = 'w'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)


class Valency(InvariantNum):
    name = 'Degree regularity'
    code = 'd\u1d63'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        deg_seq = gp.degree_sequence(graph)
        valencies = []
        for i in range(0, nx.number_of_nodes(graph)):
            if deg_seq[i] not in valencies:
                valencies.append(deg_seq[i])
        return len(valencies)


class DegreeMax(InvariantNum):
    name = "Maximum degree"
    code = '\u0394'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return max(gp.degree_sequence(graph))


class DegreeMin(InvariantNum):
    name = "Minimum degree"
    code = '\u1e9f'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return min(gp.degree_sequence(graph))


class DegreeAverage(InvariantNum):
    name = "Average degree"
    code = 'd\u2090'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        sequence = (gp.degree_sequence(graph))
        return sum(sequence) / len(sequence)


class VertexCover(InvariantNum):
    name = "Vertex cover number"
    code = '\u03c4'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)


class Diameter(InvariantNum):
    name = "Diameter"
    code = "diam"
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return nx.diameter(graph)
        else:
            return 10 ** 10


class Radius(InvariantNum):
    name = "Radius"
    code = "r"
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return nx.radius(graph)
        else:
            return 10 ** 10


class Largest1EigenA(InvariantNum):
    name = "Largest A-eigenvalue"
    code = "\u03bb\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(inv_other.AdjacencySpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class Largest1EigenL(InvariantNum):
    name = "Largest L-eigenvalue"
    code = "\u03bc\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(inv_other.LaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class Largest1EigenQ(InvariantNum):
    name = "Largest Q-eigenvalue"
    code = "q\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(inv_other.SignlessLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class Largest1EigenN(InvariantNum):
    name = "Largest N-eigenvalue"
    code = "\u03bc\u207f\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return \
            Utils.approx_to_int(inv_other.NormalizedLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])


class Largest1EigenD(InvariantNum):
    name = "Largest D-eigenvalue"
    code = "\u0398\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(inv_other.DistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 1])
        else:
            return 10 ** 10


class Largest2EigenA(InvariantNum):
    name = "Second Largest A-eigenvalue"
    code = "\u03bb\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph):
            return Utils.approx_to_int(inv_other.AdjacencySpectrum.calculate(graph)[nx.number_of_nodes(graph) - 2])
        else:
            return 0


class Largest2EigenL(InvariantNum):
    name = "Second Largest L-eigenvalue"
    code = "\u03bc\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.approx_to_int(inv_other.LaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 2])
        else:
            return 0


class Largest2EigenQ(InvariantNum):
    name = "Second Largest Q-eigenvalue"
    code = "q\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return \
                Utils.approx_to_int(inv_other.SignlessLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 2])
        else:
            return 0


class Largest2EigenN(InvariantNum):
    name = "Second Largest N-eigenvalue"
    code = "\u03bc\u207f\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.approx_to_int(
                inv_other.NormalizedLaplacianSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 2]
            )
        else:
            return 0


class Largest2EigenD(InvariantNum):
    name = "Second Largest D-eigenvalue"
    code = "\u0398\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        elif nx.is_connected(graph):
            return Utils.approx_to_int(inv_other.DistanceSpectrum.calculate(graph)[nx.number_of_nodes(graph) - 2])
        else:
            return 10 ** 10


class AlgebraicConnectivity(InvariantNum):
    name = 'Algebraic connectivity'
    code = 'ac'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.approx_to_int(inv_other.LaplacianSpectrum.calculate(graph)[1])
        else:
            return 0


class VertexConnectivity(InvariantNum):
    name = "Vertex connectivity"
    code = '\u03f0'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return gp.node_connectivity(graph)
        else:
            return 0


class EdgeConnectivity(InvariantNum):
    name = "Edge connectivity"
    code = '\u03bb'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.edge_connectivity(graph)


# class ChromaticIndex(InvariantNum):
#     name = "Chromatic Index"
#     code = "\u03c7'"
#     type = "number_structural"
#
#     @staticmethod
#     def calculate(graph):
#         return len(set(nx.greedy_color(nx.line_graph(graph)).values()))


class MinimumEdgeCover(InvariantNum):
    name = "Minimum edge cover number"
    code = 'mec'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.number_of_isolates(graph) < 1 and nx.number_of_nodes(graph) > 1:
            return len(nx.algorithms.covering.min_edge_cover(graph))
        else:
            return 10 ** 10


class NumberOfTriangles(InvariantNum):
    name = "Number of triangles"
    code = '\u03A4'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1 and nx.number_of_edges(graph) > 1:
            return int(sum(nx.algorithms.cluster.triangles(graph).values())/3)
        else:
            return 0


class WienerIndex(InvariantNum):
    name = 'Wiener index'
    code = 'W'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(nx.wiener_index(graph))
        else:
            return 10 ** 10


class EstradaIndex(InvariantNum):
    name = 'Estrada index'
    code = 'EE'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(nx.estrada_index(graph))


class Nullity(InvariantNum):
    name = 'Nullity'
    code = '\u03b7'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph) - la.matrix_rank(inv_other.AdjacencyMatrix.calculate(graph), hermitian=True)


class NumberSpanningTree(InvariantNum):
    name = 'Number of spanning trees'
    code = '\u0288'
    type = "number_structural"

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
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.density(graph)


class AdjacencyEnergy(InvariantNum):
    name = 'Adjacency Energy'
    code = 'Ea'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return sum(np.absolute(inv_other.AdjacencySpectrum.calculate(graph)))


class LaplacianEnergy(InvariantNum):
    name = 'Laplacian Energy'
    code = 'El'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        eigenvalues = inv_other.LaplacianSpectrum.calculate(graph)
        avg_degree = DegreeAverage.calculate(graph)
        return sum([np.absolute(x - avg_degree) for x in eigenvalues])


class SignlessLaplacianEnergy(InvariantNum):
    name = 'Signless Laplacian Energy'
    code = 'Eq'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        eigenvalues = inv_other.SignlessLaplacianSpectrum.calculate(graph)
        avg_degree = DegreeAverage.calculate(graph)
        return sum([np.absolute(x-avg_degree) for x in eigenvalues])


class DistanceEnergy(InvariantNum):
    name = 'Distance Energy'
    code = 'Ed'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return sum(np.absolute(inv_other.DistanceSpectrum.calculate(graph)))
        else:
            return 10 ** 10


class MainEigenvalueAdjacency(InvariantNum):
    name = 'Number main A-eigenvalues'
    code = 'mainA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return len(Utils.MainEigenvalue(inv_other.AdjacencyMatrix.calculate(graph)))


class MainEigenvalueDistance(InvariantNum):
    name = 'Number main D-eigenvalues'
    code = 'mainD'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return len(Utils.MainEigenvalue(inv_other.DistanceMatrix.calculate(graph)))
        else:
            return 0


class MainEigenvalueSignlessLaplacian(InvariantNum):
    name = 'Number main Q-eigenvalues'
    code = 'mainQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return len(Utils.MainEigenvalue(inv_other.SignlessLaplacianMatrix.calculate(graph)))


class RankAdjacency(InvariantNum):
    name = 'Rank Adjacency matrix'
    code = 'rankA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.AdjacencyMatrix.calculate(graph), hermitian=True)
        else:
            return 0


class RankLaplacian(InvariantNum):
    name = 'Rank Laplacian Matrix'
    code = 'rankL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.LaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0


class RankSignlessLaplacian(InvariantNum):
    name = 'Rank Signless Laplacian'
    code = 'rankQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.SignlessLaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0


class RankDistance(InvariantNum):
    name = 'Rank Distance matrix'
    code = 'rankD'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        if nx.is_connected(graph):
            return la.matrix_rank(inv_other.DistanceMatrix.calculate(graph), hermitian=True)
        else:
            return 10 ** 10


class RankNormalizedLaplacian(InvariantNum):
    name = 'Rank Normalized Lap matrix'
    code = 'rankN'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.NormalizedLaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0


class DeterminantAdjacency(InvariantNum):
    name = 'Determinant Adjacency'
    code = 'detA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.AdjacencyMatrix.calculate(graph)))


class DeterminantLaplacian(InvariantNum):
    name = 'Determinant Laplacian matrix'
    code = 'detL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.LaplacianMatrix.calculate(graph)))


class DeterminantSignlessLaplacianMatrix(InvariantNum):
    name = 'Determinant Signless Laplacian'
    code = 'detQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.SignlessLaplacianMatrix.calculate(graph)))


class DeterminantDistance(InvariantNum):
    name = 'Determinant Distance matrix'
    code = 'detD'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(la.det(inv_other.DistanceMatrix.calculate(graph)))
        else:
            return 10 ** 10


class DeterminantNormalizedLaplacian(InvariantNum):
    name = 'Determinant Normalized Laplacian'
    code = 'detN'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.NormalizedLaplacianMatrix.calculate(graph)))
