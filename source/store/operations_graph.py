import networkx as nx

from source.view.components.message_box import MessageBox


class OperationsGraph:
    name = None

    def __init__(self):
        self.all = OperationsGraph.__subclasses__()
        self.dict_name_operations_graph: {str: OperationsGraph} = {}
        for operations in self.all:
            self.dict_name_operations_graph[operations.name] = operations


class LineGraph(OperationsGraph):
    name = "Line Graph"

    @staticmethod
    def calculate(graph):
        return nx.line_graph(graph)


class InverseLineGraph(OperationsGraph):
    name = "Inverse Line Graph"

    @staticmethod
    def calculate(graph):
        try:
            if nx.is_connected(graph):
                return nx.inverse_line_graph(graph)
            else:
                root_graphs = []
                for comp in nx.connected_components(graph):
                    root_graphs.append(nx.inverse_line_graph(graph.subgraph(comp)))
                return nx.disjoint_union_all(root_graphs)
        except nx.NetworkXError:
            message_box = MessageBox("The drawn graph is not a line graph of any graph")
            message_box.exec()
        except:
            message_box = MessageBox("There was an error when calculating the inverse line graph")
            message_box.exec()

        return None

class Complement(OperationsGraph):
    name = "Complement"

    @staticmethod
    def calculate(graph):
        return nx.complement(graph)


class CliqueGraph(OperationsGraph):
    name = "Clique Graph"

    @staticmethod
    def calculate(graph):
        return nx.make_max_clique_graph(graph)


operations_graph = OperationsGraph()

dict_name_operations_graph = operations_graph.dict_name_operations_graph
