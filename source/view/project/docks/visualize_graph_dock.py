from PyQt5.QtWidgets import *
import matplotlib

import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from netgraph import EditableGraph
import numpy as np
from PyQt5.QtCore import Qt
matplotlib.use("Qt5Agg")


class VisualizeGraphDock(QDockWidget):

    def __init__(self):
        super().__init__()

        self.canvas = None

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Visualize")
        self.setObjectName("Visualize")

        self.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

    def plot_graph(self, graph):
        self.canvas = MplCanvas(self, nx.from_graph6_bytes(graph.encode('utf-8')))
        self.canvas.setFocusPolicy(Qt.ClickFocus)
        self.canvas.setFocus()
        self.setWidget(self.canvas)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, graph=None, width=8, height=4, dpi=100):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_position([0, 0, 1, 1])
        self.ax.clear()
        if graph is None:
            return
        self.plot_instance = ResizableGraph(graph, scale=(2, 1), ax=self.ax)


class ResizableGraph(EditableGraph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        kwargs.setdefault('origin', (0., 0.))
        kwargs.setdefault('scale', (1., 1.))
        self.origin = kwargs["origin"]
        self.scale = kwargs["scale"]
        self.figure_width = self.fig.bbox.width
        self.figure_height = self.fig.bbox.height
        self.fig.canvas.mpl_connect('resize_event', self._on_resize)

    def _on_resize(self, event, pad=0.05):
        # determine ratio new : old
        scale_x_by = self.fig.bbox.width / self.figure_width
        scale_y_by = self.fig.bbox.height / self.figure_height

        self.figure_width = self.fig.bbox.width
        self.figure_height = self.fig.bbox.height

        # rescale node positions
        for node, (x, y) in self.node_positions.items():
            new_x = ((x - self.origin[0]) * scale_x_by) + self.origin[0]
            new_y = ((y - self.origin[1]) * scale_y_by) + self.origin[1]
            self.node_positions[node] = np.array([new_x, new_y])

        # update axis dimensions
        self.scale = (scale_x_by * self.scale[0],
                      scale_y_by * self.scale[1])
        xmin = self.origin[0] - pad * self.scale[0]
        ymin = self.origin[1] - pad * self.scale[1]
        xmax = self.origin[0] + self.scale[0] + pad * self.scale[0]
        ymax = self.origin[1] + self.scale[1] + pad * self.scale[1]
        self.ax.axis([xmin, xmax, ymin, ymax])

        # redraw
        self._update_node_artists(self.nodes)
        self._update_node_label_positions()
        self._update_edges(self.edges)
        self._update_edge_label_positions(self.edges)
        self.fig.canvas.draw()
