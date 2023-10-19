import grinpy as gp
import networkx as nx
import numpy as np
import numpy.linalg as la

import source.store.operations_and_invariants.other_invariants as inv_other
from source.store.operations_and_invariants.invariants import Invariant
from source.store.operations_and_invariants.invariants import UtilsToInvariants as Utils


class InvariantNum(Invariant):
    type = None
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


class NumberVertices(InvariantNum):
    name = "Number of vertices"
    code = 'n'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NumberVertices.calculate(graph), precision)


class NumberEdges(InvariantNum):
    name = "Number of edges"
    code = '\u0415'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NumberEdges.calculate(graph), precision)


class CliqueNumber(InvariantNum):
    name = "Clique number"
    code = '\u03c9'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return len(set(nx.max_weight_clique(graph, weight=None)[0]))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(set(nx.max_weight_clique(graph, weight=None)[0]), precision)


class IndependenceNumber(InvariantNum):
    name = "Independence number"
    code = '\u237a'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return CliqueNumber.calculate(nx.complement(graph))

    @staticmethod
    def print(graph, precision):
        return CliqueNumber.print(nx.complement(graph), precision)


class DominationNumber(InvariantNum):
    name = "Domination number"
    code = '\u0194'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(gp.domination_number(graph), precision)


class ChromaticNumber(InvariantNum):
    name = "Chromatic number (estimated)"
    code = '\u03c7'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        n = len(graph.nodes())
        m = len(graph.edges())
        if m == 0:
            return 1
        if m == n * (n - 1) / 2:
            return n
        if m == (n * (n - 1) / 2) - 1:
            return n - 1
        if nx.is_bipartite(graph):
            return 2

        strategies = [max(nx.greedy_color(graph, strategy='DSATUR').values()),
                      max(nx.greedy_color(graph, strategy='largest_first', interchange=True).values()),
                      max(nx.greedy_color(graph, strategy='smallest_last', interchange=True).values()),
                      max(nx.greedy_color(graph, strategy='random_sequential', interchange=True).values())
                      ]

        return round(min(strategies) + 1)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(ChromaticNumber.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(GirthNumber.calculate(graph), precision)


class MatchingNumber(InvariantNum):
    name = "Matching number"
    code = '\u03bd'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return IndependenceNumber.calculate(nx.line_graph(graph))

    @staticmethod
    def print(graph, precision):
        return IndependenceNumber.print(nx.line_graph(graph), precision)


class NumberComponnents(InvariantNum):
    name = "Number of components"
    code = 'w'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NumberComponnents.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Valency.calculate(graph), precision)


class DegreeMax(InvariantNum):
    name = "Maximum degree"
    code = '\u0394'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return max(gp.degree_sequence(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DegreeMax.calculate(graph), precision)


class DegreeMin(InvariantNum):
    name = "Minimum degree"
    code = '\u1e9f'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return min(gp.degree_sequence(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DegreeMin.calculate(graph), precision)


class DegreeAverage(InvariantNum):
    name = "Average degree"
    code = 'd\u2090'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        sequence = (gp.degree_sequence(graph))
        return sum(sequence) / len(sequence)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DegreeAverage.calculate(graph), precision)


class VertexCover(InvariantNum):
    name = "Vertex cover number"
    code = '\u03c4'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(VertexCover.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Diameter.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Radius.calculate(graph), precision)


class Largest1EigenA(InvariantNum):
    name = "Largest A-eigenvalue"
    code = "\u03bb\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.largest_eigen(inv_other.AdjacencyMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenA.calculate(graph), precision)


class Largest1EigenL(InvariantNum):
    name = "Largest L-eigenvalue"
    code = "\u03bc\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.largest_eigen(inv_other.LaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenL.calculate(graph), precision)


class Largest1EigenQ(InvariantNum):
    name = "Largest Q-eigenvalue"
    code = "q\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.largest_eigen(inv_other.SignlessLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenQ.calculate(graph), precision)


class Largest1EigenD(InvariantNum):
    name = "Largest D-eigenvalue"
    code = "\u0398\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.largest_eigen(inv_other.DistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenD.calculate(graph), precision)


class Largest1EigenDL(InvariantNum):
    name = "Largest DL-eigenvalue"
    code = "\u03bbL\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.largest_eigen(inv_other.LaplacianDistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenDL.calculate(graph), precision)


class Largest1EigenDQ(InvariantNum):
    name = "Largest DQ-eigenvalue"
    code = "\u03bbQ\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.largest_eigen(inv_other.SignlessLaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenDQ.calculate(graph), precision)


class Largest1EigenN(InvariantNum):
    name = "Largest N-eigenvalue"
    code = "\u03bc\u207f\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.largest_eigen(inv_other.NormalizedLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenN.calculate(graph), precision)


class Largest1EigenS(InvariantNum):
    name = "Largest S-eigenvalue"
    code = "\u03bb\u002a\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.largest_eigen(inv_other.SeidelMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenS.calculate(graph), precision)


class Largest1EigenE(InvariantNum):
    name = "Largest E-eigenvalue"
    code = "\u03b5\u2081"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.largest_eigen(inv_other.EccentricityMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest1EigenE.calculate(graph), precision)


class Largest2EigenA(InvariantNum):
    name = "2th Largest A-eigenvalue"
    code = "\u03bb\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.largest_eigen(inv_other.AdjacencyMatrix.calculate(graph))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenA.calculate(graph), precision)


class Largest2EigenL(InvariantNum):
    name = "2th Largest L-eigenvalue"
    code = "\u03bc\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.second_largest_eigen(inv_other.LaplacianMatrix.calculate(graph))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenL.calculate(graph), precision)


class Largest2EigenQ(InvariantNum):
    name = "2th Largest Q-eigenvalue"
    code = "q\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.second_largest_eigen(inv_other.SignlessLaplacianMatrix.calculate(graph))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenQ.calculate(graph), precision)


class Largest2EigenD(InvariantNum):
    name = "2th Largest D-eigenvalue"
    code = "\u0398\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        elif nx.is_connected(graph):
            return Utils.second_largest_eigen(inv_other.DistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenD.calculate(graph), precision)


class Largest2EigenDL(InvariantNum):
    name = "2th Largest DL-eigenvalue"
    code = "\u03bbL\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.second_largest_eigen(inv_other.LaplacianDistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenDL.calculate(graph), precision)


class Largest2EigenDQ(InvariantNum):
    name = "2th Largest DQ-eigenvalue"
    code = "\u03bbQ\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.second_largest_eigen(inv_other.SignlessLaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenDQ.calculate(graph), precision)


class Largest2EigenN(InvariantNum):
    name = "2th Largest N-eigenvalue"
    code = "\u03bc\u207f\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.second_largest_eigen(inv_other.NormalizedLaplacianMatrix.calculate(graph))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenN.calculate(graph), precision)


class Largest2EigenS(InvariantNum):
    name = "2th Largest S-eigenvalue"
    code = "\u03bb\u002a\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return Utils.second_largest_eigen(inv_other.SeidelMatrix.calculate(graph))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenS.calculate(graph), precision)


class Largest2EigenE(InvariantNum):
    name = "2th Largest E-eigenvalue"
    code = "\u03b5\u2082"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.second_largest_eigen(inv_other.EccentricityMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Largest2EigenE.calculate(graph), precision)


class SmallestEigenA(InvariantNum):
    name = "Smallest A-eigenvalue"
    code = "\u03bb\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.AdjacencyMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenA.calculate(graph), precision)


class SmallestEigenL(InvariantNum):
    name = "Smallest L-eigenvalue"
    code = "\u03bc\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.LaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenL.calculate(graph), precision)


class SmallestEigenQ(InvariantNum):
    name = "Smallest Q-eigenvalue"
    code = "q\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.SignlessLaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenQ.calculate(graph), precision)


class SmallestEigenD(InvariantNum):
    name = "Smallest D-eigenvalue"
    code = "\u0398\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.DistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenD.calculate(graph), precision)


class SmallestEigenDL(InvariantNum):
    name = "Smallest DL-eigenvalue"
    code = "\u03bb L\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.LaplacianDistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenDL.calculate(graph), precision)


class SmallestEigenDQ(InvariantNum):
    name = "Smallest DQ-eigenvalue"
    code = "\u03bb Q\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.SignlessLaplacianDistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenDQ.calculate(graph), precision)


class SmallestEigenN(InvariantNum):
    name = "Smallest N-eigenvalue"
    code = "\u03bc\u207f\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.NormalizedLaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenN.calculate(graph), precision)


class SmallestEigenS(InvariantNum):
    name = "Smallest S-eigenvalue"
    code = "\u03bb\u002a\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.SeidelMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenS.calculate(graph), precision)


class SmallestEigenE(InvariantNum):
    name = "Smallest E-eigenvalue"
    code = "\u03b5\u2099"
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.smallest_eigen(inv_other.EccentricityMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SmallestEigenE.calculate(graph), precision)


class AdjacencyEnergy(InvariantNum):
    name = 'Adjacenc Energy'
    code = 'EA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.energy(inv_other.AdjacencyMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(AdjacencyEnergy.calculate(graph), precision)


class LaplacianEnergy(InvariantNum):
    name = 'Laplacian Energy'
    code = 'EL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.energy(inv_other.LaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(LaplacianEnergy.calculate(graph), precision)


class SignlessLaplacianEnergy(InvariantNum):
    name = 'Signless Laplacian Energy'
    code = 'EQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.energy(inv_other.SignlessLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SignlessLaplacianEnergy.calculate(graph), precision)


class DistanceEnergy(InvariantNum):
    name = 'Distance Energy'
    code = 'Edist'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.energy(inv_other.DistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DistanceEnergy.calculate(graph), precision)


class LaplacianDistanceEnergy(InvariantNum):
    name = 'Laplacian Distance Energy'
    code = 'EDL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.energy(inv_other.LaplacianDistanceMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(LaplacianDistanceEnergy.calculate(graph), precision)


class SignlessLaplacianDistanceEnergy(InvariantNum):
    name = 'Signless Laplacian Distance Energy'
    code = 'EDQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.energy(inv_other.SignlessLaplacianMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SignlessLaplacianDistanceEnergy.calculate(graph), precision)


class NormalizedLaplacianEnergy(InvariantNum):
    name = 'Normalized Laplacian Energy'
    code = 'EN'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.energy(inv_other.NormalizedLaplacianMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NormalizedLaplacianEnergy.calculate(graph), precision)


class SeidelEnergy(InvariantNum):
    name = 'Seidel Energy'
    code = 'ES'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.energy(inv_other.SeidelMatrix.calculate(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(SeidelEnergy.calculate(graph), precision)


class EccentricityEnergy(InvariantNum):
    name = 'Eccentricity Energy'
    code = 'E\u03b5'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.energy(inv_other.EccentricityMatrix.calculate(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(EccentricityEnergy.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(AlgebraicConnectivity.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(VertexConnectivity.calculate(graph), precision)


class EdgeConnectivity(InvariantNum):
    name = "Edge connectivity"
    code = '\u03bb'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.edge_connectivity(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(EdgeConnectivity.calculate(graph), precision)


class ChromaticIndex(InvariantNum):
    name = "Chromatic Index (estimated)"
    code = "\u03c7'"
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return ChromaticNumber.calculate(nx.line_graph(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(ChromaticIndex.calculate(graph), precision)


class MinimumEdgeCover(InvariantNum):
    name = "Minimum edge cover number"
    code = 'mec'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.number_of_isolates(graph) < 1 < nx.number_of_nodes(graph):
            return len(nx.algorithms.covering.min_edge_cover(graph))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        if nx.number_of_isolates(graph) < 1:
            return Utils.print_set(nx.algorithms.covering.min_edge_cover(graph), precision)
        else:
            return "Graph has isolate vertice."


class NumberOfTriangles(InvariantNum):
    name = "Number of triangles"
    code = '\u03A4'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1 and nx.number_of_edges(graph) > 1:
            return int(sum(nx.algorithms.cluster.triangles(graph).values()) / 3)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NumberOfTriangles.calculate(graph), precision)


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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(WienerIndex.calculate(graph), precision)


class EstradaIndex(InvariantNum):
    name = 'Estrada index'
    code = 'EE'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(nx.estrada_index(graph))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(EstradaIndex.calculate(graph), precision)


class Nullity(InvariantNum):
    name = 'Nullity'
    code = '\u03b7'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph) - la.matrix_rank(inv_other.AdjacencyMatrix.calculate(graph), hermitian=True)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Nullity.calculate(graph), precision)


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
        return int(la.det(NumberSpanningTree.submatrix(nx.laplacian_matrix(graph))))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(NumberSpanningTree.calculate(graph), precision)


class Density(InvariantNum):
    name = 'Density'
    code = '\u018a'
    type = "number_structural"

    @staticmethod
    def calculate(graph):
        return nx.density(graph)

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(Density.calculate(graph), precision)


class MainEigenvalueAdjacency(InvariantNum):
    name = 'Number main A-eigen'
    code = 'mainA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return len(Utils.main_eigenvalue(inv_other.AdjacencyMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(Utils.main_eigenvalue(inv_other.AdjacencyMatrix.calculate(graph)), precision)


class MainEigenvalueDistance(InvariantNum):
    name = 'Number main D-eigen'
    code = 'mainD'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return len(Utils.main_eigenvalue(inv_other.DistanceMatrix.calculate(graph)))
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        if nx.is_connected(graph):
            return Utils.print_set(Utils.main_eigenvalue(inv_other.DistanceMatrix.calculate(graph)), precision)
        else:
            return 0


class MainEigenvalueSignlessLaplacian(InvariantNum):
    name = 'Number main Q-eigen'
    code = 'mainQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return len(Utils.main_eigenvalue(inv_other.SignlessLaplacianMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(Utils.main_eigenvalue(inv_other.SignlessLaplacianMatrix.calculate(graph)), precision)


class MainEigenvalueSeidel(InvariantNum):
    name = 'Number main S-eigen'
    code = 'mainS'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return len(Utils.main_eigenvalue(inv_other.SeidelMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_set(Utils.main_eigenvalue(inv_other.SeidelMatrix.calculate(graph)), precision)


class RankAdjacency(InvariantNum):
    name = 'Rank A-matrix'
    code = 'rankA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.AdjacencyMatrix.calculate(graph), hermitian=True)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankAdjacency.calculate(graph), precision)


class RankLaplacian(InvariantNum):
    name = 'Rank L-matrix'
    code = 'rankL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.LaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankLaplacian.calculate(graph), precision)


class RankSignlessLaplacian(InvariantNum):
    name = 'Rank Q-matrix'
    code = 'rankQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.SignlessLaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankSignlessLaplacian.calculate(graph), precision)


class RankDistance(InvariantNum):
    name = 'Rank D-matrix'
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

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankDistance.calculate(graph), precision)


class RankLaplacianDistance(InvariantNum):
    name = 'Rank DL-matrix'
    code = 'rankDL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        if nx.is_connected(graph):
            return la.matrix_rank(inv_other.LaplacianDistanceMatrix.calculate(graph), hermitian=True)
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankLaplacianDistance.calculate(graph), precision)


class RankSignlessLaplacianDistance(InvariantNum):
    name = 'Rank DQ-matrix'
    code = 'rankDQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        if nx.is_connected(graph):
            return la.matrix_rank(inv_other.SignlessLaplacianDistanceMatrix.calculate(graph), hermitian=True)
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankSignlessLaplacianDistance.calculate(graph), precision)


class RankNormalizedLaplacian(InvariantNum):
    name = 'Rank N-matrix'
    code = 'rankN'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.NormalizedLaplacianMatrix.calculate(graph), hermitian=True)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankNormalizedLaplacian.calculate(graph), precision)


class RankSeidel(InvariantNum):
    name = 'Rank S-matrix'
    code = 'rankS'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) > 1:
            return la.matrix_rank(inv_other.SeidelMatrix.calculate(graph), hermitian=True)
        else:
            return 0

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankSeidel.calculate(graph), precision)


class RankEccentricity(InvariantNum):
    name = 'Rank E-matrix'
    code = 'rankE'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.number_of_nodes(graph) < 2:
            return 0
        if nx.is_connected(graph):
            return la.matrix_rank(inv_other.EccentricityMatrix.calculate(graph), hermitian=True)
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(RankEccentricity.calculate(graph), precision)


class DeterminantAdjacency(InvariantNum):
    name = 'Determinant A'
    code = 'detA'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.AdjacencyMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantAdjacency.calculate(graph), precision)


class DeterminantLaplacian(InvariantNum):
    name = 'Determinant L'
    code = 'detL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.LaplacianMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantLaplacian.calculate(graph), precision)


class DeterminantSignlessLaplacianMatrix(InvariantNum):
    name = 'Determinant Q'
    code = 'detQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.SignlessLaplacianMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantSignlessLaplacianMatrix.calculate(graph), precision)


class DeterminantDistance(InvariantNum):
    name = 'Determinant D'
    code = 'detD'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(la.det(inv_other.DistanceMatrix.calculate(graph)))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantDistance.calculate(graph), precision)


class DeterminantLaplacianDistance(InvariantNum):
    name = 'Determinant DL'
    code = 'detDL'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(la.det(inv_other.LaplacianDistanceMatrix.calculate(graph)))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantLaplacianDistance.calculate(graph), precision)


class DeterminantSignlessLaplacianDistance(InvariantNum):
    name = 'Determinant DQ'
    code = 'detDQ'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(la.det(inv_other.SignlessLaplacianDistanceMatrix.calculate(graph)))
        else:
            return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantSignlessLaplacianDistance.calculate(graph), precision)


class DeterminantSeidelMatrix(InvariantNum):
    name = 'Determinant S'
    code = 'detS'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.SeidelMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantSeidelMatrix.calculate(graph), precision)


class DeterminantNormalizedLaplacian(InvariantNum):
    name = 'Determinant N'
    code = 'detN'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        return Utils.approx_to_int(la.det(inv_other.NormalizedLaplacianMatrix.calculate(graph)))

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantNormalizedLaplacian.calculate(graph), precision)


class DeterminantEccentricityMatrix(InvariantNum):
    name = 'Determinant E'
    code = 'det\u03b5'
    type = "number_spectral"

    @staticmethod
    def calculate(graph):
        if nx.is_connected(graph):
            return Utils.approx_to_int(la.det(inv_other.EccentricityMatrix.calculate(graph)))
        return 10 ** 10

    @staticmethod
    def print(graph, precision):
        return Utils.print_numeric(DeterminantEccentricityMatrix.calculate(graph), precision)
