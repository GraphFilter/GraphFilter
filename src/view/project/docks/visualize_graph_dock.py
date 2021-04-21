from PyQt5.QtWidgets import *
import matplotlib
import networkx as nx
from PyQt5.QtCore import QUrl
from src.domain.plot.network import Network
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

matplotlib.use('Qt5Agg')


class Graph(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Graph")

        self.webView = QWebEngineView()
        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setWidget(self.webView)

    def plot_graph(self, graph):
        net = Network()
        g = nx.from_graph6_bytes(graph.encode('utf-8'))
        net.create_vis_data(g)

        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../domain/plot/plot.html"))

        self.webView.load(QUrl.fromLocalFile(filepath))
        self.webView.show()
