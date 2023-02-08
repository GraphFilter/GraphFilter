from PyQt5.QtWidgets import *
import matplotlib

import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from netgraph import EditableGraph
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

matplotlib.use("Qt5Agg")


class VisualizeGraphDock(QDockWidget):
    any_signal = QtCore.pyqtSignal(object)

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
        try:
            self.canvas = MplCanvas(self, nx.from_graph6_bytes(graph.encode('utf-8')), self.synchronize_change)
        except AttributeError:
            self.canvas = MplCanvas(self, graph, self.synchronize_change)
        self.canvas.setFocusPolicy(Qt.ClickFocus)
        self.canvas.setFocus()
        self.setWidget(self.canvas)

    def synchronize_change(self, new_graph):
        self.any_signal.emit(new_graph)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, graph=None, synchronize_change=None, width=8, height=4, dpi=100, ):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_position([0, 0, 1, 1])
        self.ax.clear()
        if graph is None:
            return
        self.plot_instance = ResizableGraph(synchronize_change, graph, scale=(2, 1), ax=self.ax, node_labels=True)


class ResizableGraph(EditableGraph):

    def __init__(self, synchronize_change, *args, **kwargs):
        super().__init__(*args, **kwargs)

        kwargs.setdefault('origin', (0., 0.))
        kwargs.setdefault('scale', (1., 1.))
        self.origin = kwargs["origin"]
        self.scale = kwargs["scale"]
        self.figure_width = self.fig.bbox.width
        self.figure_height = self.fig.bbox.height
        self.synchronize_change = synchronize_change
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

    def _on_key_press(self, event):
        if event.key == "enter" or event.key == "alt+enter":
            return
        super()._on_key_press(event)
        new_graph = nx.Graph(self.edges)
        new_graph.add_nodes_from(self.nodes)
        self.synchronize_change(new_graph)

    def _on_press(self, event):
        super()._on_press(event)
        new_graph = nx.Graph(self.edges)
        new_graph.add_nodes_from(self.nodes)
        self.synchronize_change(new_graph)

    def _add_or_remove_nascent_edge(self, event):
        for node, artist in self.node_artists.items():
            if artist.contains(event)[0]:
                if self._nascent_edge:
                    if self._nascent_edge.source == node:
                        return
        super()._add_or_remove_nascent_edge(event)
