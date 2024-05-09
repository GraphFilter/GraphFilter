from PyQt5.QtWidgets import *
import matplotlib

import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from netgraph import EditableGraph
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from deprecated.utils import fix_graph_nodes
from deprecated.store.project_information_store import project_information_store

matplotlib.use("Qt5Agg")


class VisualizeGraphDock(QDockWidget):
    any_signal = QtCore.pyqtSignal()
    invalid_graph_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.canvas = None
        self.current_graph = None

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Visualize")
        self.setObjectName("Visualize")

        self.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

    def plot_graph(self, graph, layout='spring'):
        try:
            self.current_graph = nx.from_graph6_bytes(graph.encode('utf-8'))
        except AttributeError:
            self.current_graph = graph
        except (nx.NetworkXError, IndexError):
            self.invalid_graph_signal.emit()
            self.current_graph = nx.Graph()
        self.canvas = MplCanvas(self, self.current_graph, self.synchronize_change, layout)
        self.canvas.setFocusPolicy(Qt.ClickFocus)
        self.canvas.setFocus()
        self.setWidget(self.canvas)

    def synchronize_change(self):
        self.any_signal.emit()


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, graph=None, synchronize_change=None, layout='spring', width=8, height=4, dpi=100, ):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_position([0, 0, 1, 1])
        self.ax.clear()
        if graph is None:
            return
        self.plot_instance = ResizableGraph(synchronize_change, graph, scale=(2, 1), ax=self.ax, node_labels=True,
                                            node_label_fontdict=dict(size=8), node_layout=layout, node_size=2,
                                            edge_width=0.5)


class ResizableGraph(EditableGraph):

    def __init__(self, synchronize_change, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.node_labels = {}
        self.synchronize_change = synchronize_change
        self.restart_label()
        self.set_node_positions_store()

    def restart_label(self):
        try:
            self.node_labels = {node: i for i, node in enumerate(self.nodes)}
            self.node_label_offset[self.nodes[len(self.nodes) - 1]] = (0.0, 0.0)
            self.draw_node_labels(self.node_labels, self.node_label_fontdict)

            new_graph = nx.Graph()
            new_graph.add_nodes_from(self.nodes)
            new_graph.add_edges_from(self.edges)
            new_graph = fix_graph_nodes(new_graph)
        except IndexError:
            new_graph = nx.Graph()
            pass

        project_information_store.current_graph = new_graph
        self.synchronize_change()

    def set_node_positions_store(self):
        node_positions = {}

        for node, (x, y) in self.node_positions.items():
            node_positions[self.node_labels[node]] = (x, y)

        project_information_store.current_graph_pos = node_positions

    def _on_key_press(self, event):
        if event.key == "enter" or event.key == "alt+enter":
            return
        if event.key == '=':
            self._add_node(event)
        if event.key == 'backspace':
            self._delete_nodes()
            self._delete_edges()
        super()._on_key_press(event)

        self.restart_label()
        self.set_node_positions_store()

    def _on_motion(self, event):
        super()._on_motion(event)
        self.set_node_positions_store()

    def _on_press(self, event):
        super()._on_press(event)
        self.restart_label()

    def _add_or_remove_nascent_edge(self, event):
        for node, artist in self.node_artists.items():
            if artist.contains(event)[0]:   
                if self._nascent_edge:
                    if self._nascent_edge.source == node:
                        return
        super()._add_or_remove_nascent_edge(event)

    def draw_node_labels(self, node_labels, node_label_fontdict):
        for i, (node, label) in enumerate(node_labels.items()):
            x, y = self.node_positions[node]
            dx, dy = self.node_label_offset[node]

            artist = self.ax.text(x + dx, y + dy, label, **node_label_fontdict)

            if node in self.node_label_artists:
                self.node_label_artists[node].remove()
            self.node_label_artists[node] = artist
