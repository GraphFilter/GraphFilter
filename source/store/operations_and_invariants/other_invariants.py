import networkx as nx
import numpy as np
import numpy.linalg as la
import scipy.sparse as ss
import grinpy as gp
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils
from source.store.operations_and_invariants.invariants import Invariant


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
        return Utils.print_matrix(NormalizedLaplacianMatrix.calculate(graph), precision)


class DistanceMatrix(InvariantOther):
    name = "Distance Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_matrix(DistanceMatrix.calculate(graph), precision)


class AdjacencySpectrum(InvariantOther):
    name = "Adjacency Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(AdjacencyMatrix.calculate(graph)).tolist())

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(AdjacencySpectrum.calculate(graph), precision)


class LaplacianSpectrum(InvariantOther):
    name = "Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(LaplacianMatrix.calculate(graph)).tolist())

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(LaplacianSpectrum.calculate(graph), precision)


class SignlessLaplacianSpectrum(InvariantOther):
    name = "Signless Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(SignlessLaplacianMatrix.calculate(graph)).tolist())

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(SignlessLaplacianSpectrum.calculate(graph), precision)


class NormalizedLaplacianSpectrum(InvariantOther):
    name = "Normalized Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(nx.linalg.spectrum.normalized_laplacian_spectrum(graph).tolist())

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(NormalizedLaplacianSpectrum.calculate(graph), precision)


class DistanceSpectrum(InvariantOther):
    name = "Distance Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_array_to_int(la.eigvalsh(nx.floyd_warshall_numpy(graph)).tolist())
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_list(DistanceSpectrum.calculate(graph), precision)


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
        values, vectors = la.eigh(AdjacencyMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(AdjacencyEigenvectors.calculate(graph), precision)


class LaplacianEigenvectors(InvariantOther):
    name = 'Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(LaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(LaplacianEigenvectors.calculate(graph), precision)


class SignlessLaplacianEigenvectors(InvariantOther):
    name = 'Signless Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(SignlessLaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(SignlessLaplacianEigenvectors.calculate(graph), precision)


class DistanceEigenvectors(InvariantOther):
    name = 'Distance Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            values, vectors = la.eigh(DistanceMatrix.calculate(graph))
            return values, Utils.approx_array_to_int(vectors)
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(DistanceEigenvectors.calculate(graph), precision)


class NormalizedLaplacianEigenvectors(InvariantOther):
    name = "Normalized Laplacian Eigenvectors"
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(NormalizedLaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)

    @staticmethod
    def print(graph, precision):
        return Utils.print_eigenvectors_and_eigenvalues(NormalizedLaplacianEigenvectors.calculate(graph), precision)


class MaximumClique(InvariantOther):
    name = "Maximum Clique"
    type = 'set'

    @staticmethod
    def calculate(graph):
        return set(nx.max_weight_clique(graph, weight=None)[0])

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(set(nx.max_weight_clique(graph, weight=None)[0]), precision)


class MainEigenvalueAdjacency(InvariantOther):
    name = 'Main A-eigenvalues (set)'
    type = "set"

    @staticmethod
    def calculate(graph):
        return list(Utils.MainEigenvalue(AdjacencyMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(MainEigenvalueAdjacency.calculate(graph), precision)


class MainEigenvalueDistance(InvariantOther):
    name = 'Main D-eigenvalues (set)'
    type = "set"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return list(Utils.MainEigenvalue(DistanceMatrix.calculate(graph)))
        else:
            return 'Disconnected graph'

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(MainEigenvalueDistance.calculate(graph), precision)


class MainEigenvalueSignlessLaplacian(InvariantOther):
    name = 'Main Q-eigenvalues (set)'
    type = "set"

    @staticmethod
    def calculate(graph):
        return list(Utils.MainEigenvalue(SignlessLaplacianMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(MainEigenvalueSignlessLaplacian.calculate(graph), precision)


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
