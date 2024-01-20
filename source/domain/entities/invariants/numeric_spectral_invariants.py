import networkx as nx
import numpy.linalg as la

from source.domain.entities.functions import Function
from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import \
    largest_eigen, print_numeric, second_largest_eigen, smallest_eigen, \
    energy, approx_to_int, main_eigenvalue, print_set


class NumericSpectralInvariants:
    class FirstLargestEigenA(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixA().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixL().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenQ(Function, Invariant):

        def __init__(self):
            super().__init__("q\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixQ().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenD(Function, Invariant):

        def __init__(self):
            super().__init__("\u0398\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.MatrixD().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenDL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bbL\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenDQ(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bbQ\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.MatrixQ().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenN(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u207f\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixN().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenS(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u002a\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixS().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenE(Function, Invariant):

        def __init__(self):
            super().__init__("\u03b5\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenR(Function, Invariant):

        def __init__(self):
            super().__init__("r\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.MatrixR().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenA(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return largest_eigen(MatrixInvariants.MatrixA().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(MatrixInvariants.MatrixL().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenQ(Function, Invariant):

        def __init__(self):
            super().__init__("q\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(
                    MatrixInvariants.MatrixQ().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenD(Function, Invariant):

        def __init__(self):
            super().__init__("\u0398\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            elif nx.is_connected(graph):
                return second_largest_eigen(MatrixInvariants.MatrixD().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenDL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bbL\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(
                    MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenDQ(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bbQ\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(
                    MatrixInvariants.MatrixQ().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenN(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u207f\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(
                    MatrixInvariants.MatrixN().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenS(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u002a\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(MatrixInvariants.MatrixS().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenE(Function, Invariant):

        def __init__(self):
            super().__init__("\u03b5\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenR(Function, Invariant):

        def __init__(self):
            super().__init__("r\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return largest_eigen(MatrixInvariants.MatrixR().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenA(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixA().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixL().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenQ(Function, Invariant):

        def __init__(self):
            super().__init__("q\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixQ().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenD(Function, Invariant):

        def __init__(self):
            super().__init__("\u0398\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.MatrixD().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenDL(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb L\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenDQ(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb Q\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(
                    MatrixInvariants.MatrixDQ().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenN(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bc\u207f\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixN().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenS(Function, Invariant):

        def __init__(self):
            super().__init__("\u03bb\u002a\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixS().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenE(Function, Invariant):

        def __init__(self):
            super().__init__("\u03b5\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenR(Function, Invariant):

        def __init__(self):
            super().__init__("r\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.MatrixR().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyA(Function, Invariant):

        def __init__(self):
            super().__init__("EA")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixA().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyL(Function, Invariant):

        def __init__(self):
            super().__init__("EL")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixL().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyQ(Function, Invariant):

        def __init__(self):
            super().__init__("EQ")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixQ().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyD(Function, Invariant):

        def __init__(self):
            super().__init__("Edist")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.MatrixD().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyDL(Function, Invariant):

        def __init__(self):
            super().__init__("EDL")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.MatrixDL().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyDQ(Function, Invariant):

        def __init__(self):
            super().__init__("EDQ")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.MatrixQ().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyN(Function, Invariant):

        def __init__(self):
            super().__init__("EN")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixN().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyS(Function, Invariant):

        def __init__(self):
            super().__init__("ES")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixS().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyE(Function, Invariant):

        def __init__(self):
            super().__init__("E\u03b5")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.MatrixE().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EnergyR(Function, Invariant):

        def __init__(self):
            super().__init__("ER")

        def calculate(self, graph):
            return energy(MatrixInvariants.MatrixR().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class AlgebraicConnectivity(Function, Invariant):

        def __init__(self):
            super().__init__("ac")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return approx_to_int(MatrixInvariants.LaplacianSpectrum().calculate(graph)[1])
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EstradaIndex(Function, Invariant):

        def __init__(self):
            super().__init__("EE")

        def calculate(self, graph):
            return approx_to_int(nx.estrada_index(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Nullity(Function, Invariant):

        def __init__(self):
            super().__init__('\u03b7')

        def calculate(self, graph):
            return nx.number_of_nodes(graph) - la.matrix_rank(MatrixInvariants.MatrixA().calculate(graph),
                                                              hermitian=True)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MainEigenvalueA(Function, Invariant):

        def __init__(self):
            super().__init__('mainA')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.MatrixA().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.MatrixA().calculate(graph)), precision)

    class MainEigenvalueD(Function, Invariant):

        def __init__(self):
            super().__init__('mainD')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return len(main_eigenvalue(MatrixInvariants.MatrixD().calculate(graph)))
            else:
                return 0

        def print(self, graph, precision):
            if nx.is_connected(graph):
                return print_set(
                    main_eigenvalue(MatrixInvariants.MatrixD().calculate(graph)), precision)
            else:
                return 0

    class MainEigenvalueQ(Function, Invariant):

        def __init__(self):
            super().__init__('mainQ')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.MatrixQ().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.MatrixQ().calculate(graph)),
                precision)

    class MainEigenvalueS(Function, Invariant):

        def __init__(self):
            super().__init__('mainS')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.MatrixS().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.MatrixS().calculate(graph)), precision)

    class RankA(Function, Invariant):

        def __init__(self):
            super().__init__('rankA')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.MatrixA().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankL(Function, Invariant):

        def __init__(self):
            super().__init__('rankL')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.MatrixL().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankQ(Function, Invariant):

        def __init__(self):
            super().__init__('rankQ')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.MatrixQ().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankD(Function, Invariant):

        def __init__(self):
            super().__init__('rankD')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.MatrixD().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankDL(Function, Invariant):

        def __init__(self):
            super().__init__('rankDL')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.MatrixDL().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankDQ(Function, Invariant):

        def __init__(self):
            super().__init__('rankDQ')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.MatrixDQ().calculate(graph),
                                      hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankN(Function, Invariant):

        def __init__(self):
            super().__init__('rankN')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.MatrixN().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankS(Function, Invariant):

        def __init__(self):
            super().__init__('rankS')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.MatrixS().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankE(Function, Invariant):

        def __init__(self):
            super().__init__('rankE')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.MatrixE().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantA(Function, Invariant):

        def __init__(self):
            super().__init__('detA')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.MatrixA().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantL(Function, Invariant):

        def __init__(self):
            super().__init__('detL')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.MatrixL().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantQ(Function, Invariant):

        def __init__(self):
            super().__init__('detQ')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.MatrixQ().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantD(Function, Invariant):

        def __init__(self):
            super().__init__('detD')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(la.det(MatrixInvariants.MatrixD().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantDL(Function, Invariant):

        def __init__(self):
            super().__init__('detDL')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(
                    la.det(MatrixInvariants.MatrixDL().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantDQ(Function, Invariant):

        def __init__(self):
            super().__init__('detDQ')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(
                    la.det(MatrixInvariants.MatrixDQ().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantS(Function, Invariant):

        def __init__(self):
            super().__init__('detS')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.MatrixS().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantN(Function, Invariant):

        def __init__(self):
            super().__init__('detN')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.MatrixN().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantE(Function, Invariant):

        def __init__(self):
            super().__init__('det\u03b5')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(la.det(MatrixInvariants.MatrixE().calculate(graph)))
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)
