import networkx as nx
import numpy.linalg as la

from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.objects.function_object import FunctionObject
from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.utils import \
    largest_eigen, print_numeric, second_largest_eigen, smallest_eigen, \
    energy, approx_to_int, main_eigenvalue, print_set


class NumericSpectralInvariants:
    class FirstLargestEigenA(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest A-eigenvalue", code="\u03bb\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.AdjacencyMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest L-eigenvalue", code="\u03bc\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.LaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest Q-eigenvalue", code="q\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenD(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest D-eigenvalue", code="\u0398\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.DistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenDL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest DL-eigenvalue", code="\u03bbL\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenDQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest DQ-eigenvalue", code="\u03bbQ\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenN(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest N-eigenvalue", code="\u03bc\u207f\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenS(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest S-eigenvalue", code="\u03bb\u002a\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.SeidelMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenE(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest E-eigenvalue", code="\u03b5\u2081")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return largest_eigen(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class FirstLargestEigenR(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Largest R-eigenvalue", code="r\u2081")

        def calculate(self, graph):
            return largest_eigen(MatrixInvariants.RandicMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenA(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest A-eigenvalue", code="\u03bb\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return largest_eigen(MatrixInvariants.AdjacencyMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest L-eigenvalue", code="\u03bc\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(MatrixInvariants.LaplacianMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest Q-eigenvalue", code="q\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(
                    MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenD(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest D-eigenvalue", code="\u0398\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            elif nx.is_connected(graph):
                return second_largest_eigen(MatrixInvariants.DistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenDL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest DL-eigenvalue", code="\u03bbL\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(
                    MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenDQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest DQ-eigenvalue", code="\u03bbQ\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(
                    MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenN(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest N-eigenvalue", code="\u03bc\u207f\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(
                    MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenS(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest S-eigenvalue", code="\u03bb\u002a\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return second_largest_eigen(MatrixInvariants.SeidelMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenE(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest E-eigenvalue", code="\u03b5\u2082")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return second_largest_eigen(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SecondLargestEigenR(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="2th Largest R-eigenvalue", code="r\u2082")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return largest_eigen(MatrixInvariants.RandicMatrix().calculate(graph))
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenA(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest A-eigenvalue", code="\u03bb\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.AdjacencyMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest L-eigenvalue", code="\u03bc\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.LaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest Q-eigenvalue", code="q\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenD(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest D-eigenvalue", code="\u0398\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.DistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenDL(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest DL-eigenvalue", code="\u03bb L\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenDQ(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest DQ-eigenvalue", code="\u03bb Q\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(
                    MatrixInvariants.SignlessLaplacianDistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenN(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest N-eigenvalue", code="\u03bc\u207f\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenS(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest S-eigenvalue", code="\u03bb\u002a\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.SeidelMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenE(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest E-eigenvalue", code="\u03b5\u2099")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return smallest_eigen(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SmallestEigenR(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Smallest R-eigenvalue", code="r\u2099")

        def calculate(self, graph):
            return smallest_eigen(MatrixInvariants.RandicMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class AdjacencyEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Adjacency Energy", code="EA")

        def calculate(self, graph):
            return energy(MatrixInvariants.AdjacencyMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class LaplacianEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Energy", code="EL")

        def calculate(self, graph):
            return energy(MatrixInvariants.LaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SignlessLaplacianEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Energy", code="EQ")

        def calculate(self, graph):
            return energy(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DistanceEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Distance Energy", code="Edist")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.DistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class LaplacianDistanceEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Laplacian Distance Energy", code="EDL")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SignlessLaplacianDistanceEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Signless Laplacian Distance Energy", code="EDQ")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class NormalizedLaplacianEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Normalized Laplacian Energy", code="EN")

        def calculate(self, graph):
            return energy(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class SeidelEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Seidel Energy", code="ES")

        def calculate(self, graph):
            return energy(MatrixInvariants.SeidelMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EccentricityEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Eccentricity Energy", code="E\u03b5")

        def calculate(self, graph):
            if nx.is_connected(graph):
                return energy(MatrixInvariants.EccentricityMatrix().calculate(graph))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RandicEnergy(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Randic Energy", code="ER")

        def calculate(self, graph):
            return energy(MatrixInvariants.RandicMatrix().calculate(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class AlgebraicConnectivity(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Algebraic connectivity", code="ac")

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return approx_to_int(MatrixInvariants.LaplacianSpectrum().calculate(graph)[1])
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class EstradaIndex(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Estrada index", code="EE")

        def calculate(self, graph):
            return approx_to_int(nx.estrada_index(graph))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class Nullity(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Nullity', code='\u03b7')

        def calculate(self, graph):
            return nx.number_of_nodes(graph) - la.matrix_rank(MatrixInvariants.AdjacencyMatrix().calculate(graph),
                                                              hermitian=True)

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class MainEigenvalueAdjacency(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Number main A-eigen', code='mainA')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.AdjacencyMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.AdjacencyMatrix().calculate(graph)), precision)

    class MainEigenvalueDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Number main D-eigen', code='mainD')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return len(main_eigenvalue(MatrixInvariants.DistanceMatrix().calculate(graph)))
            else:
                return 0

        def print(self, graph, precision):
            if nx.is_connected(graph):
                return print_set(
                    main_eigenvalue(MatrixInvariants.DistanceMatrix().calculate(graph)), precision)
            else:
                return 0

    class MainEigenvalueSignlessLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Number main Q-eigen', code='mainQ')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph)),
                precision)

    class MainEigenvalueSeidel(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Number main S-eigen', code='mainS')

        def calculate(self, graph):
            return len(main_eigenvalue(MatrixInvariants.SeidelMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_set(
                main_eigenvalue(MatrixInvariants.SeidelMatrix().calculate(graph)), precision)

    class RankAdjacency(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank A-matrix', code='rankA')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.AdjacencyMatrix().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank L-matrix', code='rankL')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.LaplacianMatrix().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankSignlessLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank Q-matrix', code='rankQ')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank D-matrix', code='rankD')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.DistanceMatrix().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankLaplacianDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank DL-matrix', code='rankDL')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankSignlessLaplacianDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank DQ-matrix', code='rankDQ')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.SignlessLaplacianDistanceMatrix().calculate(graph),
                                      hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankNormalizedLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank N-matrix', code='rankN')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankSeidel(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank S-matrix', code='rankS')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) > 1:
                return la.matrix_rank(MatrixInvariants.SeidelMatrix().calculate(graph), hermitian=True)
            else:
                return 0

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class RankEccentricity(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Rank E-matrix', code='rankE')

        def calculate(self, graph):
            if nx.number_of_nodes(graph) < 2:
                return 0
            if nx.is_connected(graph):
                return la.matrix_rank(MatrixInvariants.EccentricityMatrix().calculate(graph), hermitian=True)
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantAdjacency(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant A', code='detA')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.AdjacencyMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant L', code='detL')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.LaplacianMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantSignlessLaplacianMatrix(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant Q', code='detQ')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.SignlessLaplacianMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant D', code='detD')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(la.det(MatrixInvariants.DistanceMatrix().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantLaplacianDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant DL', code='detDL')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(
                    la.det(MatrixInvariants.LaplacianDistanceMatrix().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantSignlessLaplacianDistance(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant DQ', code='detDQ')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(
                    la.det(MatrixInvariants.SignlessLaplacianDistanceMatrix().calculate(graph)))
            else:
                return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantSeidelMatrix(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant S', code='detS')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.SeidelMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantNormalizedLaplacian(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant N', code='detN')

        def calculate(self, graph):
            return approx_to_int(la.det(MatrixInvariants.NormalizedLaplacianMatrix().calculate(graph)))

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)

    class DeterminantEccentricityMatrix(Invariant, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name='Determinant E', code='det\u03b5')

        def calculate(self, graph):
            if nx.is_connected(graph):
                return approx_to_int(la.det(MatrixInvariants.EccentricityMatrix().calculate(graph)))
            return 10 ** 10

        def print(self, graph, precision):
            return print_numeric(self.calculate(graph), precision)
