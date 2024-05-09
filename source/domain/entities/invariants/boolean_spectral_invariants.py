import networkx as nx
import numpy.linalg as la

from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import is_there_integer, print_boolean, integral, is_integer, approx_to_int


class BooleanSpectralInvariants:
    class SomeEigenIntegerA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumA().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumL().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumQ().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.SpectrumD().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.SpectrumDL().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(
                    MatrixInvariants.SpectrumDQ().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumS().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumN().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_there_integer(MatrixInvariants.SpectrumE().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class SomeEigenIntegerR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_there_integer(MatrixInvariants.SpectrumR().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return integral(MatrixInvariants.SpectrumA().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return integral(MatrixInvariants.SpectrumL().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return integral(MatrixInvariants.SpectrumQ().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SpectrumN().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return integral(MatrixInvariants.SpectrumS().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SpectrumD().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SpectrumDL().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SpectrumDQ().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return integral(MatrixInvariants.SpectrumE().calculate(graph))
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class IntegralR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return integral(MatrixInvariants.SpectrumR().calculate(graph))

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerA(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumA().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumL().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumQ().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.SpectrumD().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.SpectrumDL().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.
                    SpectrumDQ().calculate(graph)[nx.number_of_nodes(graph) - 1])
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumS().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumN().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return is_integer(
                    MatrixInvariants.SpectrumE().calculate(graph)[nx.number_of_nodes(graph) - 1])
            return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class LargestEigenIntegerR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return is_integer(
                MatrixInvariants.SpectrumR().calculate(graph)[nx.number_of_nodes(graph) - 1])

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class RegularTransmission(Invariant):

        def __init__(self):
            super().__init__()

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

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(
                approx_to_int(la.det(MatrixInvariants.MatrixA().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(
                approx_to_int(la.det(MatrixInvariants.MatrixL().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(
                approx_to_int(
                    la.det(MatrixInvariants.MatrixQ().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixD(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(la.det(MatrixInvariants.MatrixD().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixDL(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(
                        la.det(MatrixInvariants.MatrixDL().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixDQ(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(approx_to_int(
                    la.det(MatrixInvariants.MatrixDQ().calculate(graph))) != 0)
            else:
                return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixN(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(
                approx_to_int(
                    la.det(MatrixInvariants.MatrixN().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixS(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(approx_to_int(la.det(MatrixInvariants.MatrixS().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixE(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            if nx.is_connected(graph):
                return bool(
                    approx_to_int(la.det(MatrixInvariants.MatrixE().calculate(graph))) != 0)
            return False

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)

    class InvertibleMatrixR(Invariant):

        def __init__(self):
            super().__init__()

        def calculate(self, graph):
            return bool(approx_to_int(la.det(MatrixInvariants.MatrixR().calculate(graph))) != 0)

        def print(self, graph, precision):
            return print_boolean(self.calculate(graph), precision)
