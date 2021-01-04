from PyQt5.QtWidgets import *


class Graph(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Graph")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setWidget(QTextEdit())
