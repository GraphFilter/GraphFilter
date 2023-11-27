import networkx as nx

from source.domain.entities.symbols import Unicode, Symbol
from source.domain.objects.function_object import FunctionObject
from source.domain.entities.operations import Operation


class GraphOperations:
    class Complement(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Complement", code="Comp")

        def calculate(self, graph):
            return nx.complement(graph)

    class LineGraph(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Line", code="\u2113")

        def calculate(self, graph):
            return nx.line_graph(graph)

    class CliqueGraph(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Clique Operator (maximal)", code="\u0198")

        def calculate(self, graph):
            return nx.make_max_clique_graph(graph)

    class Graph(Operation):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Graph", code="G")

        def calculate(self, graph):
            return graph

    class InverseLineGraph(Operation):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Inverse Line Graph", code="")

        def calculate(self, graph):
            try:
                if nx.is_connected(graph):
                    return nx.inverse_line_graph(graph)
                else:
                    root_graphs = []
                    for comp in nx.connected_components(graph):
                        root_graphs.append(nx.inverse_line_graph(graph.subgraph(comp)))
                    return nx.disjoint_union_all(root_graphs)
            except nx.NetworkXError:
                raise "The drawn graph is not a line graph of any graph"
