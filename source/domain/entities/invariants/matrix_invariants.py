import scipy.sparse as ss
import numpy as np
import networkx as nx
import grinpy as gp
import math

from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import print_matrix, spectrum, print_list, eigenvectors, \
    print_eigenvectors_and_eigenvalues


class MatrixInvariants:

    class AdjacencyMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Adjacency Matrix")

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.graphmatrix.adjacency_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class LaplacianMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Matrix")

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.laplacian_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class SignlessLaplacianMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Matrix")

        def calculate(self, graph):
            return ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class NormalizedLaplacianMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Normalized Laplacian Matrix")

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.laplacianmatrix.normalized_laplacian_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class DistanceMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Distance Matrix")

        def calculate(self, graph):
            return nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class SeidelMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Seidel Matrix")

        def calculate(self, graph):
            n = nx.number_of_nodes(graph)
            j = np.empty([n, n])
            j.fill(1)
            return np.subtract(np.subtract(j, np.identity(n)), np.multiply(2, MatrixInvariants.AdjacencyMatrix().
                                                                           calculate(graph)))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class LaplacianDistanceMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Distance Matrix")

        def calculate(self, graph):
            dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
            trans = np.sum(dist, axis=1)
            dist_neg = np.multiply(-1, dist)
            np.fill_diagonal(dist_neg, trans)
            return dist_neg

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class SignlessLaplacianDistanceMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Distance Matrix")

        def calculate(self, graph):
            dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
            trans = np.sum(dist, axis=1)
            np.fill_diagonal(dist, trans)
            return dist

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class EccentricityMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Eccentricity Matrix")

        def calculate(self, graph):
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

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class RandicMatrix(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Randic Matrix")

        def calculate(self, graph):
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

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class AdjacencySpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Adjacency Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.AdjacencyMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class LaplacianSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.LaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SignlessLaplacianSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class DistanceSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Distance Spectrum")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(nx.floyd_warshall_numpy(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class LaplacianDistanceSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Distance Spectrum")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SignlessLaplacianDistanceSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Distance Spectrum")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.SignlessLaplacianDistanceMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SeidelSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Seidel Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.SeidelMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class RandicSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Randic Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.RandicMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class NormalizedLaplacianSpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Normalized Laplacian Spectrum")

        def calculate(self, graph):
            return spectrum(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class EccentricitySpectrum(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Eccentricity Spectrum")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class DegreeSequence(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Degree Sequence")

        def calculate(self, graph):
            return gp.degree_sequence(graph)

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class AdjacencyEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Adjacency Eigenvectors')

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.AdjacencyMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class LaplacianEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Laplacian Eigenvectors')

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.LaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class SignlessLaplacianEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Signless Laplacian Eigenvectors')

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class NormalizedLaplacianEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Normalized Laplacian Eigenvectors")

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class SeidelEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Seidel Eigenvectors")

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.SeidelMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class DistanceEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Distance Eigenvectors')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.DistanceMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class LaplacianDistanceEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Laplacian Distance Eigenvectors')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class SignlessLaplacianDistanceEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Signless Laplacian Distance Eigenvectors')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.SignlessLaplacianDistanceMatrix().
                                    calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(
                self.calculate(graph),
                precision)

    class EccentricityEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Eccentricity Eigenvectors')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class RandicEigenvectors(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Randic Eigenvectors")

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.RandicMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)
