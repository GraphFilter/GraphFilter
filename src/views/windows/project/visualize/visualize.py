from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from src.views.windows.project.visualize.docks.info import Info
from src.views.windows.project.visualize.docks.graph import Graph


class Visualize(QWidget):

    def __init__(self, project_window):
        super().__init__()

        self.graph = None
        self.info = None

        self.tool_bar = None

        self.project_window = project_window

        self.create_tool_bar()
        self.create_docks()

    def create_tool_bar(self):
        if self.tool_bar is None:
            self.tool_bar = QToolBar("Tool Bar")
            self.tool_bar.layout().setSpacing(30)
            self.tool_bar.layout().setContentsMargins(15, 10, 20, 20)
            self.tool_bar.setMovable(False)
            self.tool_bar.addWidget(QLabel("List of graphs filtered"))

            self.graphs_list = QComboBox()
            self.graphs_list.adjustSize()
            self.graphs_list.setMaximumWidth(500)

            self.tool_bar.addWidget(self.graphs_list)
            self.tool_bar.addSeparator()
            self.tool_bar.addAction(self.project_window.zoom_in_action)
            self.tool_bar.addAction(self.project_window.zoom_out_action)
            self.tool_bar.addAction(self.project_window.zoom_fit_action)
            self.tool_bar.addAction(self.project_window.print_action)
            self.project_window.addToolBar(self.tool_bar)

    def create_docks(self):
        if (self.graph and self.info) is None:
            self.graph = Graph(self)
            self.info = Info(self)
            self.project_window.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.graph)
            self.project_window.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.info)

    def remove_docks(self):
        if self.graph and self.info is not None:
            self.project_window.removeDockWidget(self.graph)
            self.project_window.removeDockWidget(self.info)

            self.graph = None
            self.info = None

    def load_file_out(self, file_out_path):
        file = open(file_out_path, 'r')
        list_graphs_g6 = file.read().splitlines()

        for i in range(0, len(list_graphs_g6)):
            self.graphs_list.addItem(f'Graph {i}')



