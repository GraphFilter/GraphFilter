import os
import re
import networkx as nx
import gzip

from PyQt5.QtWidgets import QApplication


def validate_path(path):
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
    if rect.width() > 1920 or rect.height() > 1080:
        self.width = 1129
        self.height = 635
    elif rect.width() > 800 or rect.height() > 600:
        self.width = int(rect.width() / p)
        self.height = int(rect.height() / p)
    elif rect.width() <= 800 or rect.height() <= 600:
        self.width = 770
        self.height = 550
