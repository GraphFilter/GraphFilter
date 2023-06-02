import os
import os.path
import random
import re
import networkx as nx
import gzip

from PyQt5.QtWidgets import QApplication, QMessageBox

from source.view.components.message_box import MessageBox


def validate_path(path):
    forbidden_chars = ['.', '\\', '/', ":"]
    if len(path) != 0:
        if path[0] in forbidden_chars:
            return False
        if path[len(path) - 1] in forbidden_chars:
            try:
                open(path + "/verify.txt", "x")
                os.remove(path + "/verify.txt")
            except IOError:
                return False
    return os.path.isdir(path)  # NOTE: or ispath


def validate_file(path):
    return os.path.isfile(path)  # NOTE: or ispath


def validate_file_name(name):
    forbidden_chars = ['?', '\\', '/', ':', '*', '"', '<', '>', '|', "'"]
    return not any(substring in name for substring in forbidden_chars) and len(name) > 0


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def extract_files_to_list(files):
    list_g6 = []
    for file in files:
        if file.endswith('.gz'):
            file_ungzipped = gzip.open(file, 'r')
            list_g6.extend(file_ungzipped.read().decode('utf-8').splitlines())
        else:
            list_g6.extend(open(file, 'r').read().splitlines())
    return list_g6


def match_graph_code(text):
    pattern = re.compile(r'(Graph \d* - )(.*)')
    match = pattern.match(text)
    return match.group(2)


def convert_g6_to_nx(g6code):
    return nx.from_graph6_bytes(g6code.encode('utf-8'))


def set_view_size(self, p):
    screen = QApplication.desktop()
    rect = screen.screenGeometry()
    self.width = int(rect.width() / p)
    self.height = int(rect.height() / p)


def fix_graph_nodes(graph):
    new_dict = {}
    new_edges = []
    new_graph = nx.Graph()

    for i, node in enumerate(graph):
        new_dict[node] = i
        new_graph.add_node(i)

    for edge in graph.edges:
        new_edges.append((new_dict[edge[0]], new_dict[edge[1]]))

    new_graph.add_edges_from(new_edges)

    return new_graph


def set_new_vertex_positions(node_positions):
    list_x = []
    list_y = []
    new_x = random.uniform(0, 2)
    new_y = random.uniform(0, 1)

    for (x, y) in node_positions.values():
        list_x.append(round(x, 1))
        list_y.append(round(y, 1))

    while new_x in list_x:
        new_x = random.uniform(0, 2)

    while new_y in list_y:
        new_y = random.uniform(0, 1)

    return new_x, new_y


def add_vertex(graph, node_positions, new_vertex, univ=False):
    graph.add_node(new_vertex)
    node_positions[new_vertex] = set_new_vertex_positions(node_positions)

    if univ:
        for node in graph:
            if node is not new_vertex:
                graph.add_edge(new_vertex, node)

    return graph, node_positions


def trigger_message_box(text, icon=QMessageBox.Information, window_title='Information'):
    message_box = MessageBox(text, icon, window_title)
    message_box.exec()


def handle_invalid_graph_open():
    trigger_message_box("The file you tried to open contains an invalid graph. \n"
                        "Open another file in the tree or in the menu option"
                        "(If you edit the graph, the changes will replace the"
                        " invalid graph by clicking on save button)", window_title="Invalid graph")
