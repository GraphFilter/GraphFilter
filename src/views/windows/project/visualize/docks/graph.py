from PyQt5.QtWidgets import *
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import networkx as nx
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')


class Graph(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Graph")

        self.figure = plt.figure()

        self.canvas = FigureCanvasQTAgg(self.figure)

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setWidget(self.canvas)

    def plot_graph(self, graph):
        self.figure.clf()
        g = nx.from_graph6_bytes(graph.encode('utf-8'))
        nx.draw(g, with_labels=True)
        self.canvas.draw_idle()
