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
            self.tool_bar.addWidget(QLabel("View graphs from .g6 file"))

            self.g6_file_load_button = QPushButton("Load")
            self.g6_file_load_button.clicked.connect(self.load_file)
            
            self.graphs_list = QComboBox()
            self.graphs_list.adjustSize()
            self.graphs_list.setMaximumWidth(500)


            self.text_file_loaded = QLabel()
            self.text_file_loaded.setText('(no file loaded)')

            self.tool_bar.addWidget(self.g6_file_load_button)
            self.tool_bar.addWidget(self.graphs_list)
            self.tool_bar.addWidget(self.text_file_loaded)
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

    def load_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Graph Filter (*.g6)"])
        file_path = file_dialog.getOpenFileName(filter="Graph Filter (*.g6)")
        if file_path[0] != '':
            file = open(file_path[0], 'r')
            self.text_file_loaded.setText('(File .../'+file.name.split('/')[-1]+')')
            self.graphs_list.clear()
            self.graphs_list.addItems(file.read().splitlines())

