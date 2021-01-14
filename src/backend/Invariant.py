import networkx as nx
import grinpy as gp
import numpy as np


class Invariant():
    dic_invariants_num = {}
    invariants_bool = []
    numeric_names = []


    def __init__(self):
        for subclass in Invariant.__subclasses__():
            if subclass.type == 'numeric':
                self.dic_invariants_num[subclass.code]=subclass.calculate
            else:
                if subclass.type == 'bool': self.invariants_bool.append(subclass)


    @staticmethod
    def calculate(graph):
        pass


class Chromatic_number(Invariant):
    type = 'numeric'
    name = "Chromatic number"
    code = 'chi'

    @staticmethod
    def calculate(graph):
        return gp.chromatic_number(graph)


class Number_of_vertice(Invariant):
    type = 'numeric'
    name = "Chromatic number"
    code = 'n'

    @staticmethod
    def calculate(graph):
        return nx.number_of_nodes(graph)


class Number_of_edges(Invariant):
    type = 'numeric'
    name = "Chromatic number"
    code = 'm'

    @staticmethod
    def calculate(graph):
        return nx.number_of_edges(graph)

class Clique_Number(Invariant):
    type = 'numeric'
    name = "Clique Number"
    code = 'omega'

    @staticmethod
    def calculate(graph):
        return gp.clique_number(graph)

class Independence_Number(Invariant):
    type = 'numeric'
    name = "Independence Number"
    code = 'alpha'

    @staticmethod
    def calculate(graph):
        return gp.independence_number(graph)

class Domination_Number(Invariant):
    type = 'numeric'
    name = "Domination Number"
    code = 'dom'

    @staticmethod
    def calculate(graph):
        return gp.domination_number(graph)

class Total_Domination_Number(Invariant):
    type = 'numeric'
    name = "Total Domination Number"
    code = 'tdom'

    @staticmethod
    def calculate(graph):
        return gp.total_domination_number(graph)

class Connected_domination_number(Invariant):
    type = 'numeric'
    name = "Independent Domination Number"
    code = 'cdom'

class Independent_domination_number(Invariant):
    type = 'numeric'
    name = "Independent Domination Number"
    code = 'idom'

    @staticmethod
    def calculate(graph):
        return gp.independent_domination_number(graph)

class Power_Domination_Number(Invariant):
    type = 'numeric'
    name = "Power Domination Number"
    code = 'pdom'

    @staticmethod
    def calculate(graph):
        return gp.power_domination_number(graph)

class Zero_Forcing_Number(Invariant):
    type = 'numeric'
    name = "Zero Forcing Number"
    code = 'zeroForcing'

    @staticmethod
    def calculate(graph):
        return gp.zero_forcing_number(graph)

class Zero_Forcing_Number(Invariant):
    type = 'numeric'
    name = "Total Zero Forcing Number"
    code = 'tZeroForcing'

    @staticmethod
    def calculate(graph):
        return gp.total_zero_forcing_number(graph)

class Connected_Zero_forcing_number(Invariant):
    type = 'numeric'
    name = "Connected ero Forcing Number"
    code = 'cZeroForcing'

    @staticmethod
    def calculate(graph):
        return gp.connected_zero_forcing_number(graph)

class MatchingNumber(Invariant):
    type = 'numeric'
    name = "Matching Number"
    code = 'match'

    @staticmethod
    def calculate(graph):
        return gp.matching_number(graph)

class Vertex_Connectivity(Invariant):
    type = 'numeric'
    name = "Vertex Connectivity"
    code = 'vcon'

    @staticmethod
    def calculate(graph):
        return gp.node_connectivity()

class Edge_Connectivity(Invariant):
    type = 'numeric'
    name = "Vertex Connectivity"
    code = 'vcon'

    @staticmethod
    def calculate(graph):
        return gp.edge_connectivity()

class Edge_Connectivity(Invariant):
    type = 'numeric'
    name = "Number of components"
    code = 'comp'

    @staticmethod
    def calculate(graph):
        return nx.number_connected_components(graph)

class Valency(Invariant):
    type = 'bool'
    name = 'Valency'
    code = 'val'

    @staticmethod
    def calculate(graph):
        degSeq = gp.degree_sequence()
        valencies = []
        for i in range(0,nx.number_of_nodes(graph)):
            if (degSeq[i] not in valencies): valencies.append(degSeq[i])
        return valencies.count()

class Degree_Max(Invariant):
    type = 'numeric'
    name = "Maximum Degree"
    code = 'Delta'

    @staticmethod
    def calculate(graph):
        return np.max(gp.degree_sequence(graph))

class Degree_Min(Invariant):
    type = 'numeric'
    name = "Minimum Degree"
    code = 'delta'

    @staticmethod
    def calculate(graph):
        return np.min(gp.degree_sequence(graph))

class Degree_Avg(Invariant):
    type = 'numeric'
    name = "Average Degree"
    code = 'avgDegree'

    @staticmethod
    def calculate(graph):
        return np.average(gp.degree_sequence(graph))

class Vertex_Cover(Invariant):
    type = 'numeric'
    name = "Vertex Cover Number"
    code = 'vCover'

    @staticmethod
    def calculate(graph):
        return gp.vertex_cover_number(graph)


class Planar(Invariant):
    type = 'bool'
    name = "planar"

    @staticmethod
    def calculate(graph):
        return nx.check_planarity(graph)

class Connected(Invariant):
    type = 'bool'
    name = "connected"

    @staticmethod
    def calculate(graph):
        return nx.is_connected(graph)

class Biconnected(Invariant):
    type = 'bool'
    name = "biconnected"

    @staticmethod
    def calculate(graph):
        return nx.is_biconnected(graph)

class Bipartite(Invariant):
    type = 'bool'
    name = 'bipartite'

    @staticmethod
    def calculate(graph):
        return nx.is_bipartite(graph)

class Eulerian(Invariant):
    type = 'bool'
    name = 'Eulerian'

    @staticmethod
    def calculate(graph):
        return gp.is_eulerian(graph)

class Chordal(Invariant):
    type = 'bool'
    name = 'Chordal'

    @staticmethod
    def calculate(graph):
        return gp.is_chordal()

class Triangle_free(Invariant):
    type = 'bool'
    name = 'Triangle-free'

    @staticmethod
    def calculate(graph):
        return gp.is_triangle_free(graph)

class Regular(Invariant):
    type = 'bool'
    name = 'Regular'

    @staticmethod
    def calculate(graph):
        return gp.is_regular(graph)

class k_Regular(Invariant):
    type = 'bool'
    name = 'k-regular'

    @staticmethod
    def calculate(graph,k):
        return gp.is_k_regular(graph,k=k)





