import networkx as nx
import numpy.linalg as la

from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import is_there_integer, print_boolean, integral, is_integer, approx_to_int


class BooleanSpectralInvariants:
    class SomeEigenIntegerA(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some A-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.AdjacencySpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some L-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.LaplacianSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some Q-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SignlessLaplacianSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerD(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some D-eigenvalue integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.DistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerDL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some DL-eigenvalue integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.LaplacianDistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerDQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some DQ-eigenvalue integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(
                    MatrixInvariants.SignlessLaplacianDistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerS(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some S-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SeidelSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerN(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some N-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.NormalizedLaplacianSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerE(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some E-eigenvalue integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.EccentricitySpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerR(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Some R-eigenvalue integer")

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.RandicSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralA(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Adjacency integral")

        def calculate(self, graph):
            return integral(MatrixInvariants.AdjacencySpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian integral")

        def calculate(self, graph):
            return integral(MatrixInvariants.LaplacianSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian integral")

        def calculate(self, graph):
            return integral(MatrixInvariants.SignlessLaplacianSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralN(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Normalized Laplacian integral")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.NormalizedLaplacianSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralS(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Seidel integral")

        def calculate(self, graph):
            return integral(MatrixInvariants.SeidelSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralD(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Distance integral")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.DistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralDL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Distance integral")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.LaplacianDistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralDQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Distance integral")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SignlessLaplacianDistanceSpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralE(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Eccentricity integral")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.EccentricitySpectrum().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralR(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Randic integral")

        def calculate(self, graph):
            return integral(MatrixInvariants.RandicSpectrum().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerA(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest A-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.AdjacencySpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest L-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.LaplacianSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest Q-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SignlessLaplacianSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerD(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest D-eigen is integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.DistanceSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerDL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest DL-eigen is integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.LaplacianDistanceSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerDQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest DQ-eigen is integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.
                    SignlessLaplacianDistanceSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerS(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest S-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SeidelSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerN(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest N-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.NormalizedLaplacianSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerE(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest E-eigen is integer")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.EccentricitySpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])
            return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerR(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest R-eigen is integer")

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.RandicSpectrum().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class RegularTransmission(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Regular Transmission")

        def calculate(self, graph):
            if nx.is_connected(graph):
                dist_matrix = nx.algorithms.shortest_paths.floyd_warshall_numpy(graph)
                transmission = [sum(dist_matrix[:, i]) for i in range(0, dist_matrix.shape[0])]
                return bool(max(transmission) == min(transmission))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixA(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="A matrix is invertible")

        def calculate(self, graph):
            return bool(
                approx_to_int(la.det(MatrixInvariants.AdjacencyMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="L matrix is invertible")

        def calculate(self, graph):
            return bool(
                approx_to_int(la.det(MatrixInvariants.LaplacianMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Q matrix is invertible")

        def calculate(self, graph):
            return bool(
                approx_to_int(
                    la.det(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixD(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="D matrix is invertible")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(la.det(MatrixInvariants.DistanceMatrix().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixDL(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="DL matrix is invertible")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(
                        la.det(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixDQ(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="DQ matrix is invertible")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(approx_to_int(
                    la.det(MatrixInvariants.SignlessLaplacianDistanceMatrix().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixN(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="N matrix is invertible")

        def calculate(self, graph):
            return bool(
                approx_to_int(
                    la.det(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixS(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="S matrix is invertible")

        def calculate(self, graph):
            return bool(approx_to_int(la.det(MatrixInvariants.SeidelMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixE(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="E matrix is invertible")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(la.det(MatrixInvariants.EccentricityMatrix().calculate(graph))) != 0)
            return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixR(Invariant):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="R matrix is invertible")

        def calculate(self, graph):
            return bool(approx_to_int(la.det(MatrixInvariants.RandicMatrix().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)
