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

        self.combo_graphs = QComboBox()
        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)

        self.create_tool_bar()
        self.create_docks()

    def create_tool_bar(self):
        if self.tool_bar is None:
            self.tool_bar = QToolBar("Tool Bar")
            self.tool_bar.layout().setSpacing(30)
            self.tool_bar.layout().setContentsMargins(15, 10, 20, 20)
            self.tool_bar.setMovable(False)
            self.tool_bar.addWidget(QLabel("List of graphs filtered"))

            self.tool_bar.addWidget(self.combo_graphs)
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

    def fill_combo(self, file_out_path):
        for file in file_out_path:
            lines = open(file, 'r').read().splitlines()
            for i, line in enumerate(lines):
                self.combo_graphs.addItem(f'Graph {i} - {line}')
