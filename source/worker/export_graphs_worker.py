import os

import networkx as nx


class ExportGraphsWorker:
    def __init__(self, list_graphs, directory, file_name):
        self.list_graphs = list_graphs
        self.directory = directory
        self.file_name = file_name

    def save_nx_list_to_files(self):
        output_file = os.path.join(self.directory, f"{self.file_name}_graphs.g6")

        with open(output_file, 'w') as out_file:
            for graph in self.list_graphs:
                graph6_str = nx.to_graph6_bytes(graph, header=False).decode('utf-8').strip()
                out_file.write(graph6_str + '\n')
