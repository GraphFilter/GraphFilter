from PyQt5.QtWidgets import *
import matplotlib
import networkx as nx
from PyQt5.QtCore import QUrl
from pyvis.network import Network
from PyQt5.QtWebEngineWidgets import QWebEngineView

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
        net.width = "100%"
        net.height = "100%"
        net.set_options("var options = {}")
        g = nx.from_graph6_bytes(graph.encode('utf-8'))
        net.from_nx(g)
        net.write_html('graph.html')

        filepath = 'D:\Documentos\GitHub\GraphFilter.py\src\graph.html'.replace('\\', '/')

        with open(filepath, "r") as f:
            lines = f.read().splitlines()
            lines[58] = """
            var options = {
                "configure": {
                    "enabled": false
                },
                "edges": {
                    "color": {
                        "inherit": true
                    },
                    "smooth": {
                        "enabled": false,
                        "type": "continuous"
                    }
                },
                "interaction": {
                    "dragNodes": true,
                    "hideEdgesOnDrag": false,
                    "hideNodesOnDrag": false
                },
                "physics": {
                    "enabled": true,
                    "stabilization": {
                        "enabled": true,
                        "fit": true,
                        "iterations": 1000,
                        "onlyDynamicEdges": false,
                        "updateInterval": 50
                    }
                },
                manipulation: {
                    enabled: true,
                    initiallyActive: false,
                    addNode: function(nodeData,callback) {
                      nodeData.label = nodes.length;
                      nodeData.size = 10;
                      nodeData.shape = 'dot';
                      callback(nodeData);
                    },
                    addEdge: true,
                    editNode: undefined,
                    editEdge: true,
                    deleteNode: true,
                    deleteEdge: true
                }
            };
            """
            data = "\n".join(lines)

        with open(filepath, "w") as f:
            f.write(data)

        self.webView.load(QUrl(filepath))
        self.webView.show()
