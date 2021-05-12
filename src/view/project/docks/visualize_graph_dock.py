from PyQt5.QtWidgets import *
import matplotlib
import networkx as nx
import numpy as np
import pyqtgraph as pg
from src.domain.graph import Graph

matplotlib.use('Qt5Agg')


class VisualizeGraphDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.graphic_layout_widget = pg.GraphicsLayoutWidget(show=True)
        self.view_box = self.graphic_layout_widget.addViewBox()

        self.graph = Graph()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Visualize")
        self.setObjectName("Visualize")

        self.graphic_layout_widget.setBackground('w')

        self.view_box.setAspectLocked()

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

        self.setWidget(self.graphic_layout_widget)

    def plot_graph(self, graph):
        if graph is None:
            self.view_box.removeItem(self.graph)
            return

        g = nx.from_graph6_bytes(graph.encode('utf-8'))
        self.view_box.addItem(self.graph)
        self.define_graph(g)

    def define_graph(self, graph):
        position = []
        adjacency = []
        indexes = []

        points = nx.drawing.layout.spring_layout(graph)
        for i, point in enumerate(points.values()):
            aux = [point[0] * 10 // 1, point[1] * 10 // 1]
            position.append(aux)
            indexes.append(i)

        edges = graph.edges(data=True)
        for edge in edges:
            aux = [edge[0], edge[1]]
            if not reversed(aux) in adjacency:
                adjacency.append(aux)

        pos = np.array(position, dtype=float)
        adj = np.array(adjacency)

        texts = ["%d" % i for i in indexes]

        self.graph.setData(pos=pos, adj=adj, size=1, pxMode=False, text=texts)
