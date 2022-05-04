from PyQt5.QtWidgets import *
import matplotlib; matplotlib.use("Qt5Agg")

import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from netgraph import InteractiveGraph
from PyQt5.QtCore import Qt


class VisualizeGraphDock(QDockWidget):

    def __init__(self):
        super().__init__()

        self.canvas = None

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Visualize")
        self.setObjectName("Visualize")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

    def plot_graph(self, graph):
        self.canvas = MplCanvas(self, nx.from_graph6_bytes(graph.encode('utf-8')))
        self.canvas.setFocusPolicy(Qt.ClickFocus)
        self.canvas.setFocus()
        self.setWidget(self.canvas)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, graph=None, width=5, height=4, dpi=100):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        if graph is None:
            return
        self.plot_instance = InteractiveGraph(graph, ax=self.ax)
