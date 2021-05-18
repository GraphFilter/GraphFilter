import networkx as nx
import numpy as np
import numpy.linalg as la
import scipy.sparse as ss
from src.store.operations_and_invariants.invariants import UtilsToInvariants as Utils
from src.store.operations_and_invariants.invariants import Invariant


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
    def calculate(graph):
        pass


# NOTE: matrix: numpy array; list: python list


class AdjacencyMatrix(InvariantOther):
    name = "Adjacency Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.graphmatrix.adjacency_matrix(graph))


class IncidenceMatrix(InvariantOther):
    name = "Incidence Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.graphmatrix.incidence_matrix(graph))


class LaplacianMatrix(InvariantOther):
    name = "Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.laplacian_matrix(graph))


class SignlessLaplacianMatrix(InvariantOther):
    name = "Signless Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))


class NormalizedLaplacianMatrix(InvariantOther):
    name = "Normalized Laplacian Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.normalized_laplacian_matrix(graph))


class DistanceMatrix(InvariantOther):
    name = "Distance Matrix"
    type = 'matrix'

    @staticmethod
    def calculate(graph):
        return nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)


class AdjacencySpectrum(InvariantOther):
    name = "Adjacency Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(AdjacencyMatrix.calculate(graph)).tolist())


class LaplacianSpectrum(InvariantOther):
    name = "Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(LaplacianMatrix.calculate(graph)).tolist())


class SignlessLaplacianSpectrum(InvariantOther):
    name = "Signless Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(la.eigvalsh(SignlessLaplacianMatrix.calculate(graph)).tolist())


class NormalizedLaplacianSpectrum(InvariantOther):
    name = "Normalized Laplacian Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        return Utils.approx_array_to_int(nx.linalg.spectrum.normalized_laplacian_spectrum(graph).tolist())


class DistanceSpectrum(InvariantOther):
    name = "Distance Spectrum"
    type = 'list'

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_array_to_int(la.eigvalsh(nx.floyd_warshall_numpy(graph)).tolist())
        else:
            return 'Disconnected graph'


class AdjacencyEigenvectors(InvariantOther):
    name = 'Adjacency Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(AdjacencyMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)


class LaplacianEigenvectors(InvariantOther):
    name = 'Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(LaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)


class SignlessLaplacianEigenvectors(InvariantOther):
    name = 'Signless Laplacian Eigenvectors'
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(SignlessLaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)


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


class NormalizedLaplacianEigenvectors(InvariantOther):
    name = "Normalized Laplacian Eigenvectors"
    type = 'list_and_matrix'

    @staticmethod
    def calculate(graph):
        values, vectors = la.eigh(NormalizedLaplacianMatrix.calculate(graph))
        return values, Utils.approx_array_to_int(vectors)


if __name__ == '__main__':
    inv = InvariantOther()
    print(DistanceEigenvectors.calculate(nx.generators.complete_graph(5)))
    print(AdjacencySpectrum.calculate(nx.generators.complete_graph(5)))
