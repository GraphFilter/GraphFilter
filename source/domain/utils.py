import os
import re
import networkx as nx
import gzip

from PyQt5.QtWidgets import QApplication


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

    for i, node in enumerate(graph):
        new_dict[node] = i

    for edge in graph.edges:
        new_edges.append((new_dict[edge[0]], new_dict[edge[1]]))
    return nx.from_edgelist(new_edges)
