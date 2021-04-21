import networkx as nx
import json


class Network:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def create_vis_data(self, nx_graph):
        assert (isinstance(nx_graph, nx.Graph))
        nx_edges = nx_graph.edges(data=True)
        nx_nodes = nx_graph.nodes(data=True)

        for i, node in enumerate(nx_nodes):
            node_struct = {
                "id": i,
                "label": i,
                "shape": "dot",
                "size": 10
            }
            self.nodes.append(node_struct)

        if len(nx_edges) > 0:
            for e in nx_edges:
                edge_struct = {
                    "from": e[0],
                    "to": e[1],
                    "weight": 1
                }
                self.edges.append(edge_struct)

        self.export_data_to_js()

    def export_data_to_js(self):
        data = {"nodes": self.nodes, "edges": self.edges}
        graph_data = json.dumps(data)
        export = f"data = {graph_data}"
        filename = "plot/data.js"

        with open(filename, "w") as file_json:
            file_json.write(export)
            file_json.close()
