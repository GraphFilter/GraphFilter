import scipy.sparse as ss
import numpy as np
import networkx as nx
import grinpy as gp
import math

from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import print_matrix, spectrum, print_list, eigenvectors, \
    print_eigenvectors_and_eigenvalues


class MatrixInvariants:
    class MatrixA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.graphmatrix.adjacency_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.laplacian_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return ss.csc_matrix.toarray(np.abs(nx.laplacian_matrix(graph)))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return ss.csc_matrix.toarray(nx.linalg.normalized_laplacian_matrix(graph))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            n = nx.number_of_nodes(graph)
            j = np.empty([n, n])
            j.fill(1)
            return np.subtract(np.subtract(j, np.identity(n)), np.multiply(2, MatrixInvariants.MatrixA().
                                                                           calculate(graph)))

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
            trans = np.sum(dist, axis=1)
            dist_neg = np.multiply(-1, dist)
            np.fill_diagonal(dist_neg, trans)
            return dist_neg

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            dist = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
            trans = np.sum(dist, axis=1)
            np.fill_diagonal(dist, trans)
            return dist

        def print(self, graph, precision):
            return print_matrix(self.calculate(graph), precision)

    class MatrixE(Invariant):

        def __init__(self):
            super().__init__()

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

    class MatrixR(Invariant):

        def __init__(self):
            super().__init__()

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

    class SpectrumA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixA().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixL().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixQ().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(nx.floyd_warshall_numpy(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.MatrixDQ().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixS().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixR().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return spectrum(MatrixInvariants.MatrixN().calculate(graph))

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class SpectrumE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return spectrum(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)

    class EigenvectorsA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixA().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixL().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixQ().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixN().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixS().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.MatrixD().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.MatrixDQ().
                                    calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(
                self.calculate(graph),
                precision)

    class EigenvectorsE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return eigenvectors(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 'Disconnected graph'

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class EigenvectorsR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return eigenvectors(MatrixInvariants.MatrixR().calculate(graph))

        def print(self, graph, precision):
            return print_eigenvectors_and_eigenvalues(self.calculate(graph), precision)

    class DegreeSequence(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return gp.degree_sequence(graph)

        def print(self, graph, precision):
            return print_list(self.calculate(graph), precision)
