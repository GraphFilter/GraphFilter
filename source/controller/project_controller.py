from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from source.view.project.project_window import ProjectWindow
from source.view.project.project_tool_bar import ProjectToolBar
from source.view.project.about_window import AboutWindow
from source.view.project.docks.graph_information_dock import GraphInformationDock
from source.view.project.docks.visualize_graph_dock import VisualizeGraphDock
from source.view.project.docks.invariants_checks_dock import InvariantsCheckDock
from source.store.project_information_store import project_information_store
from source.store.operations_invariants import *
from source.domain.utils import match_graph_code, convert_g6_to_nx
from PyQt5.Qt import QUrl, QDesktopServices


class ProjectController:
    def __init__(self):
        self.project_window = ProjectWindow()

        self.about_window = AboutWindow()

        self.project_tool_bar = ProjectToolBar()

        self.graph_information_dock = GraphInformationDock()
        self.invariants_check_dock = InvariantsCheckDock()
        self.visualize_graph_dock = VisualizeGraphDock()

        self.invariants_selected = {}
        self.edited_graph = None

        self.settings = QtCore.QSettings("project", "GraphFilter")
        self.connect_events()

    def show_window(self):
        self.create_docks()

        self.project_window.set_title_bar(project_information_store.project_name)
        self.project_window.addToolBar(self.project_tool_bar)

        self.project_tool_bar.reset_combo_graphs()

        self.project_tool_bar.current_graph = \
            self.project_tool_bar.fill_combo_graphs(project_information_store.filtered_graphs)

        self.visualize_graph_dock.plot_graph(self.project_tool_bar.current_graph)

        self.invariants_check_dock.create_conditions(dic_invariants_to_visualize, self.on_check_condition)

        self.project_window.show()

        self.settings.setValue("state", self.project_window.saveState())

    def connect_events(self):

        self.project_window.exit_action.triggered.connect(self.on_exit)

        self.project_window.visualize_action.triggered.connect(self.on_visualize)
        self.project_window.invariants_check_action.triggered.connect(self.on_invariants_check)
        self.project_window.graph_info_action.triggered.connect(self.on_graph_info)

        self.project_window.dictionary_action.triggered.connect(self.on_dictionary)

        self.project_window.restore_layout_action.triggered.connect(self.on_restore)

        self.project_window.about_action.triggered.connect(self.on_about)

        self.connect_tool_bar_events()

        self.visualize_graph_dock.any_signal.connect(self.update_graph_to_table)

        # self.project_window.print_action.triggered.connect(self.on_print)

    def connect_tool_bar_events(self):
        self.project_tool_bar.combo_graphs.activated.connect(self.on_change_graph)
        self.project_tool_bar.left_button.clicked.connect(self.on_click_button_left)
        self.project_tool_bar.right_button.clicked.connect(self.on_click_button_right)

    def create_docks(self):
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.visualize_graph_dock)
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.graph_information_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants_check_dock)

        self.project_window.setTabPosition(QtCore.Qt.RightDockWidgetArea, QTabWidget.East)

    def on_exit(self):
        self.project_window.close()

    def on_print(self):
        # printer = QPrinter(QPrinter.HighResolution)
        # dialog = QPrintDialog(printer, self)
        #
        # if dialog.exec_() == QPrintDialog.Accepted:
        #     pass
        pass

    def on_visualize(self):
        self.visualize_graph_dock.setVisible(True)

    def on_invariants_check(self):
        self.invariants_check_dock.setVisible(True)

    def on_graph_info(self):
        self.graph_information_dock.setVisible(True)

    def on_about(self):
        self.about_window.show()

    def on_restore(self):
        self.project_window.restoreState(self.settings.value("state"))

    def on_change_graph(self):
        self.edited_graph = None
        if self.project_tool_bar.combo_graphs.currentIndex() == 0:
            self.project_tool_bar.left_button.setDisabled(True)
        else:
            self.project_tool_bar.left_button.setDisabled(False)

        if self.project_tool_bar.combo_graphs.currentIndex() == self.project_tool_bar.combo_graphs.count() - 1:
            self.project_tool_bar.right_button.setDisabled(True)
        else:
            self.project_tool_bar.right_button.setDisabled(False)

        self.project_tool_bar.current_graph = match_graph_code(self.project_tool_bar.combo_graphs.currentText())
        if self.project_tool_bar.current_graph is not None:
            self.visualize_graph_dock.plot_graph(self.project_tool_bar.current_graph)

        self.update_graph_to_table(None)
        self.graph_information_dock.update_table(self.invariants_selected)

    def on_click_button_left(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() - 1)
        self.on_change_graph()

    def on_click_button_right(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() + 1)
        self.on_change_graph()

    def on_dictionary(self):
        QDesktopServices.openUrl(QUrl("https://github.com/GraphFilter/GraphFilter/wiki/Dictionary"))

    def on_check_condition(self):
        check = QCheckBox().sender()
        g6code = self.project_tool_bar.current_graph

        if check.text() not in self.invariants_selected:
            if self.edited_graph is not None:
                self.invariants_selected[check.text()] = \
                    dic_invariants_to_visualize[check.text()].print(self.edited_graph, precision=5)
            else:
                if g6code is not None:
                    self.invariants_selected[check.text()] = \
                        dic_invariants_to_visualize[check.text()].print(convert_g6_to_nx(g6code), precision=5)
                else:
                    self.invariants_selected[check.text()] = 'No graph selected'
        else:
            del self.invariants_selected[check.text()]

        self.graph_information_dock.update_table(self.invariants_selected)

    def update_graph_to_table(self, edited_graph):
        g6code = self.project_tool_bar.current_graph
        self.edited_graph = edited_graph

        for key in self.invariants_selected.keys():
            if self.edited_graph is not None:
                self.invariants_selected[key] = \
                    dic_invariants_to_visualize[key].print(self.edited_graph, precision=5)
            else:
                if g6code is not None:
                    self.invariants_selected[key] = \
                        dic_invariants_to_visualize[key].print(convert_g6_to_nx(g6code), precision=5)
                else:
                    self.invariants_selected[key] = 'No graph selected'
        self.graph_information_dock.update_table(self.invariants_selected)
