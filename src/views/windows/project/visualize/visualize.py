from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from src.views.windows.project.visualize.docks.info import Info
from src.views.windows.project.visualize.docks.graph import Graph
from src.views.windows.project.visualize.docks.invariants import Invariants
from src.domain.operations_and_invariants.operations_invariants import Invariants as Inv

import re
from PyQt5 import QtGui


def match_graph_code(text):
    pattern = re.compile(r'(Graph \d* - )(.*)')
    match = pattern.match(text)
    return match.group(2)


class Visualize(QWidget):
    invariants_selected = {}
    dic_invariants = {}

    def __init__(self, project_window):
        super().__init__()

        # TODO: import should come from the Wizard's FilterList, fix it after the wizard's refactor.
        inv = Inv()
        self.dic_invariants = {**inv.numerics.dic_name_calc, **inv.booleans.dic_name_calc}

        self.graph = None
        self.info = None
        self.invariants = None

        self.tool_bar = None

        self.project_window = project_window

        self.combo_graphs = QComboBox()
        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)
        self.combo_graphs.activated.connect(self.change_graph)

        self.left_button = QPushButton()
        self.left_button.clicked.connect(self.move_up)
        self.right_button = QPushButton()
        self.right_button.clicked.connect(self.move_down)

        self.current_graph = None

        self.create_tool_bar()
        self.create_docks()

    def create_tool_bar(self):
        if self.tool_bar is None:
            self.tool_bar = QToolBar("Tool Bar")
            self.tool_bar.layout().setSpacing(30)
            self.tool_bar.layout().setContentsMargins(15, 10, 20, 20)
            self.tool_bar.setMovable(False)
            self.tool_bar.addWidget(QLabel("List of graphs filtered"))

            self.left_button.setIcon(QtGui.QIcon("views/resources/icons/left_arrow_key.png"))
            self.left_button.setIconSize(QtCore.QSize(20, 20))

            self.left_button.setDisabled(True)

            self.right_button.setIcon(QtGui.QIcon("views/resources/icons/right_arrow_key.png"))
            self.right_button.setIconSize(QtCore.QSize(20, 20))
            self.right_button.setDisabled(False)

            self.tool_bar.addWidget(self.combo_graphs)
            self.tool_bar.addWidget(self.left_button)
            self.tool_bar.addWidget(self.right_button)
            self.tool_bar.addSeparator()
            self.tool_bar.addAction(self.project_window.zoom_in_action)
            self.tool_bar.addAction(self.project_window.zoom_out_action)
            self.tool_bar.addAction(self.project_window.zoom_fit_action)
            self.tool_bar.addAction(self.project_window.print_action)
            self.project_window.addToolBar(self.tool_bar)

    def create_docks(self):
        if (self.graph and self.info and self.invariants) is None:
            self.graph = Graph(self)
            if self.current_graph is not None:
                self.graph.plot_graph(self.current_graph)
            self.info = Info(self)
            self.invariants = Invariants(self)
            self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants)
            self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.graph)
            self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.info)

    def remove_docks(self):
        if self.graph and self.info is not None:
            self.project_window.removeDockWidget(self.graph)
            self.project_window.removeDockWidget(self.info)
            self.project_window.removeDockWidget(self.invariants)

            self.graph = None
            self.info = None
            self.invariants = None

    def fill_combo(self, list_graphs):
        self.combo_graphs.clear()
        for i, line in enumerate(list_graphs):
            self.combo_graphs.addItem(f'Graph {i} - {line}')
        self.current_graph = match_graph_code(self.combo_graphs.currentText())
        if self.current_graph is not None:
            self.graph.plot_graph(self.current_graph)

    def change_graph(self):
        if self.combo_graphs.currentIndex() == 0:
            self.left_button.setDisabled(True)
        else:
            self.left_button.setDisabled(False)

        if self.combo_graphs.currentIndex() == self.combo_graphs.count() - 1:
            self.right_button.setDisabled(True)
        else:
            self.right_button.setDisabled(False)

        self.current_graph = match_graph_code(self.combo_graphs.currentText())
        if self.current_graph is not None:
            self.graph.plot_graph(self.current_graph)

        self.invariants.update_graph_to_table()
        # self.info.update_table_inv({"test": self.combo_graphs.currentText()})

    def move_up(self):
        self.combo_graphs.setCurrentIndex(self.combo_graphs.currentIndex() - 1)
        self.change_graph()

    def move_down(self):
        self.combo_graphs.setCurrentIndex(self.combo_graphs.currentIndex() + 1)
        self.change_graph()
