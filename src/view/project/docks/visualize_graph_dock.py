from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import matplotlib
import networkx as nx
from PyQt5.QtCore import QUrl
from src.domain.plot.network import Network
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

matplotlib.use('Qt5Agg')


class VisualizeGraphDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.webView = QWebEngineView()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Visualize")
        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setWidget(self.webView)

        self.webView.setContextMenuPolicy(Qt.NoContextMenu)

    def plot_graph(self, graph):
        net = Network()
        g = nx.from_graph6_bytes(graph.encode('utf-8'))
        net.create_vis_data(g)

        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../domain/plot/plot.html"))

        self.webView.load(QUrl.fromLocalFile(filepath))
        self.webView.show()
