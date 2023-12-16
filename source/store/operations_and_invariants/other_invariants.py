import math

import grinpy as gp
import networkx as nx
import numpy as np
import scipy.sparse as ss

from source.store.operations_and_invariants.invariants import Invariant
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils


class InvariantOther(Invariant):
    type = ''
    dic_name_inv = {}
    all = []
    name = ''

    def __init__(self):
        self.all = InvariantOther.__subclasses__()
        for invariant in self.all:
            self.dic_name_inv[invariant.name] = invariant

    @staticmethod
    def calculate(**kwargs):
        pass

    @staticmethod
    def print(**kwargs):
        pass


# NOTE: matrix: numpy array; list: python list


class AdjacencyMatrix(InvariantOther):
    name = "Adjacency Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.graphmatrix.adjacency_matrix(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(AdjacencyMatrix.calculate(graph), precision)


class IncidenceMatrix(InvariantOther):
    name = "Incidence Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.graphmatrix.incidence_matrix(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(IncidenceMatrix.calculate(graph), precision)


class LaplacianMatrix(InvariantOther):
    name = "Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.laplacian_matrix(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(LaplacianMatrix.calculate(graph), precision)


class SignlessLaplacianMatrix(InvariantOther):
    name = "Signless Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(SignlessLaplacianMatrix.calculate(graph), precision)


class NormalizedLaplacianMatrix(InvariantOther):
    name = "Normalized Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.normalized_laplacian_matrix(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(NormalizedLaplacianMatrix.calculate(graph), precision,
                                  NormalizedLaplacianMatrix.name)


class DistanceMatrix(InvariantOther):
    name = "Distance Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(DistanceMatrix.calculate(graph), precision)


class SeidelMatrix(InvariantOther):
    name = "Seidel Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        n = nx.number_of_nodes(graph)
        j = np.empty([n, n])
        j.fill(1)
        return np.subtract(np.subtract(j, np.identity(n)), np.multiply(2, AdjacencyMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(SeidelMatrix.calculate(graph), precision)


class LaplacianDistanceMatrix(InvariantOther):
    name = "Laplacian Distance Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
        trans = np.sum(dist, axis=1)
        dist_neg = np.multiply(-1, dist)
        np.fill_diagonal(dist_neg, trans)
        return dist_neg

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(LaplacianDistanceMatrix.calculate(graph), precision)


class SignlessLaplacianDistanceMatrix(InvariantOther):
    name = "Signless Laplacian Distance Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
        trans = np.sum(dist, axis=1)
        np.fill_diagonal(dist, trans)
        return dist

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(SignlessLaplacianDistanceMatrix.calculate(graph), precision)


class EccentricityMatrix(InvariantOther):
    name = "Eccentricity Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        distance_matrix = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
        if float('inf') not in distance_matrix:
            size = len(graph.nodes)
            eccentricity_matrix = np.zeros((size, size))
            for i in range(size):
                for j in range(i + 1, size):
                    min_eccentricity = min(max(distance_matrix[i]), max(distance_matrix[j]))
                    if min_eccentricity == distance_matrix[i][j]:
                        eccentricity_matrix[i][j] = min_eccentricity
                        eccentricity_matrix[j][i] = min_eccentricity
            return eccentricity_matrix

        return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(EccentricityMatrix.calculate(graph), precision)


class RandicMatrix(InvariantOther):
    name = "Randic Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        adj = nx.adjacency_matrix(graph)
        size = len(graph.nodes)
        randic = np.zeros((size, size))
        degree = gp.degree_sequence(graph)

        for i in range(size):
            for j in range(i + 1, size):
                if adj[i, j] == 1:
                    randic[i][j] = 1 / math.sqrt(degree[i] * degree[j])
                    randic[j][i] = randic[i][j]
        return randic

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(RandicMatrix.calculate(graph), precision, RandicMatrix.name)


class AdjacencySpectrum(InvariantOther):
    name = "Adjacency Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(AdjacencyMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(AdjacencySpectrum.calculate(graph), precision)


class LaplacianSpectrum(InvariantOther):
    name = "Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(LaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(LaplacianSpectrum.calculate(graph), precision)


class SignlessLaplacianSpectrum(InvariantOther):
    name = "Signless Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(SignlessLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(SignlessLaplacianSpectrum.calculate(graph), precision)


class DistanceSpectrum(InvariantOther):
    name = "Distance Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.spectrum(nx.floyd_warshall_numpy(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(DistanceSpectrum.calculate(graph), precision)


class LaplacianDistanceSpectrum(InvariantOther):
    name = "Laplacian Distance Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.spectrum(LaplacianDistanceMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(LaplacianDistanceSpectrum.calculate(graph), precision)


class SignlessLaplacianDistanceSpectrum(InvariantOther):
    name = "Signless Laplacian Distance Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.spectrum(SignlessLaplacianDistanceMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(SignlessLaplacianDistanceSpectrum.calculate(graph), precision)


class SeidelSpectrum(InvariantOther):
    name = "Seidel Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(SeidelMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(SeidelSpectrum.calculate(graph), precision)


class RandicSpectrum(InvariantOther):
    name = "Randic Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(RandicMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(RandicSpectrum.calculate(graph), precision)


class NormalizedLaplacianSpectrum(InvariantOther):
    name = "Normalized Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.spectrum(NormalizedLaplacianMatrix.calculate(graph))
        # return Utils.approx_array_to_int(nx.linalg.spectrum.normalized_laplacian_spectrum(graph).tolist())

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(NormalizedLaplacianSpectrum.calculate(graph), precision)


class EccentricitySpectrum(InvariantOther):
    name = "Eccentricity Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.spectrum(EccentricityMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(EccentricitySpectrum.calculate(graph), precision)


class DegreeSequence(InvariantOther):
    name = "Degree Sequence"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return gp.degree_sequence(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(DegreeSequence.calculate(graph), precision)


class AdjacencyEigenvectors(InvariantOther):
    name = 'Adjacency Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(AdjacencyMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(AdjacencyEigenvectors.calculate(graph), precision)


class LaplacianEigenvectors(InvariantOther):
    name = 'Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(LaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(LaplacianEigenvectors.calculate(graph), precision)


class SignlessLaplacianEigenvectors(InvariantOther):
    name = 'Signless Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(SignlessLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(SignlessLaplacianEigenvectors.calculate(graph), precision)


class NormalizedLaplacianEigenvectors(InvariantOther):
    name = "Normalized Laplacian Eigenvectors"
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(NormalizedLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(NormalizedLaplacianEigenvectors.calculate(graph), precision)


class SeidelEigenvectors(InvariantOther):
    name = "Seidel Eigenvectors"
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(SeidelMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(SeidelEigenvectors.calculate(graph), precision)


class DistanceEigenvectors(InvariantOther):
    name = 'Distance Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.eigenvectors(DistanceMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(DistanceEigenvectors.calculate(graph), precision)


class LaplacianDistanceEigenvectors(InvariantOther):
    name = 'Laplacian Distance Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.eigenvectors(LaplacianDistanceMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(LaplacianDistanceEigenvectors.calculate(graph), precision)


class SignlessLaplacianDistanceEigenvectors(InvariantOther):
    name = 'Signless Laplacian Distance Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.eigenvectors(SignlessLaplacianMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(SignlessLaplacianEigenvectors.calculate(graph), precision)


class EccentricityEigenvectors(InvariantOther):
    name = 'Eccentricity Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.eigenvectors(EccentricityMatrix.calculate(graph))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(EccentricityEigenvectors.calculate(graph), precision)


class RandicEigenvectors(InvariantOther):
    name = "Randic Eigenvectors"
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        return Utils.eigenvectors(RandicMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(RandicEigenvectors.calculate(graph), precision)


class DegreeCentrality(InvariantOther):
    name = "Degree Centrality"
    type = 'dict'

    @staticmethod
    def calculate(graph):
        return dict(sorted(nx.degree_centrality(graph).items(), key=lambda x: x[1]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(DegreeCentrality.calculate(graph), precision)


class EigenvectorCentrality(InvariantOther):
    name = "Eigenvector Centrality"
    type = 'dict'

    @staticmethod
    def calculate(graph):
        try:
            return dict(sorted(nx.eigenvector_centrality_numpy(graph).items(), key=lambda x: x[1]))
        except TypeError:
            return dict(sorted(nx.eigenvector_centrality(graph).items(), key=lambda x: x[1]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(EigenvectorCentrality.calculate(graph), precision)


class ClosenessCentrality(InvariantOther):
    name = "Closeness Centrality"
    type = 'dict'

    @staticmethod
    def calculate(graph):
        return dict(sorted(nx.closeness_centrality(graph).items(), key=lambda x: x[1]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(ClosenessCentrality.calculate(graph), precision)


class BetweennessCentrality(InvariantOther):
    name = "Betweenness Centrality"
    type = 'dict'

    @staticmethod
    def calculate(graph):
        return dict(sorted(nx.betweenness_centrality(graph).items(), key=lambda x: x[1]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(BetweennessCentrality.calculate(graph), precision)


class HarmonicCentrality(InvariantOther):
    name = "Harmonic Centrality"
    type = 'dict'

    @staticmethod
    def calculate(graph):
        return dict(sorted(nx.harmonic_centrality(graph).items(), key=lambda x: x[1]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(HarmonicCentrality.calculate(graph), precision)


class Transmission(InvariantOther):
    name = "Transmission"
    type = "dict"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            dist_matrix = DistanceMatrix.calculate(graph)
            trans = {}
            for i in range(0, dist_matrix.shape[0]):
                trans[i] = sum(dist_matrix[:, i])
            return trans
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(Transmission.calculate(graph), precision)


class CoreNumber(InvariantOther):
    name = "Core number"
    type = "dict"

    @staticmethod
    def calculate(graph):
        return nx.core_number(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_dict(CoreNumber.calculate(graph), precision)
