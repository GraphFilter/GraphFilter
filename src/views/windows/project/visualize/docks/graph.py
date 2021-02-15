from PyQt5.QtWidgets import *
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')


class Graph(QDockWidget):

    def __init__(self, visualize, graph):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Graph")

        figure = Figure(figsize=(5, 4), dpi=100)

        canvas = FigureCanvasQTAgg(figure)
        canvas.axes = figure.add_subplot(111)

        # TODO: convert g6 code to graph and plot
        #  if graph is not None:
        #     G = nx.convert(graph)
        #     nx.draw(G, with_labels=True)
        #     plt.plot()

        canvas.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setWidget(canvas)
