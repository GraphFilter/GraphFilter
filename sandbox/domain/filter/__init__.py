import os
import sys
import atexit
from unittest.mock import MagicMock, patch
import networkx as nx
import numpy as np

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

from source.controller import Controller
from source.domain.filter import Filter, FindAnExample


class GraphHandler:
    @staticmethod
    def create_random_graph():
        n = np.random.randint(10, 20)
        p = np.random.uniform(0.1, 0.5)
        return nx.erdos_renyi_graph(n, p)

    @staticmethod
    def save_graphs_to_file(num_graphs, filename):
        with open(filename, 'w') as f:
            for _ in range(num_graphs):
                graph = GraphHandler.create_random_graph()
                g6_code = nx.to_graph6_bytes(graph, header=False).decode('ascii')
                f.write(g6_code)
        return filename


class WizardMock(QMainWindow):
    close_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.cancel_button = QPushButton()
        self.start_button = QPushButton()
        self.setWindowTitle("Wizard mock")
        print("Creating files")
        self.relative_path = os.path.relpath(GraphHandler.save_graphs_to_file(10000, 'graphs.g6'))

        atexit.register(self.cleanup)

    def field(self, field_name: str):
        if field_name == "files":
            return [self.relative_path]
        if field_name == "method":
            return FindAnExample()
        if field_name == "equation":
            return "N(G) > 0"

    def cleanup(self):
        if os.path.exists(self.relative_path):
            os.remove(self.relative_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wizard = WizardMock()

    with patch('source.controller.WelcomeWindow', new=MagicMock), \
            patch('source.controller.WizardWindow', new=lambda: wizard):
        controller = Controller()
        controller.start_filter()

    sys.exit(app.exec_())
