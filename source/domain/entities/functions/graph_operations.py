import networkx as nx

from source.domain.entities.functions import Function


class GraphOperations:
    class Complement(Function):

        def __init__(self):
            super().__init__("Comp")

        def calculate(self, graph):
            return nx.complement(graph)

    class LineGraph(Function):

        def __init__(self):
            super().__init__("\u2113")

        def calculate(self, graph):
            return nx.line_graph(graph)

    class CliqueGraph(Function):

        def __init__(self):
            super().__init__("\u0198")

        def calculate(self, graph):
            return nx.make_max_clique_graph(graph)

    class InverseLineGraph(Function):

        def __init__(self):
            super().__init__("\u2113\u207B\u00B9")

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
