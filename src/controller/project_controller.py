from src.view.project.project_window import ProjectWindow
from src.view.project.about_window import AboutWindow
from src.view.project.project_tool_bar import ProjectToolBar
from src.view.project.docks.graph_information_dock import GraphInformationDock
from src.view.project.docks.visualize_graph_dock import VisualizeGraphDock
from src.view.project.docks.invariants_checks_dock import InvariantsCheckDock
from src.store.project_information_store import project_information_store
from src.view.project.project_content_dictionary import ProjectContentDictionary
from src.domain.utils import match_graph_code
from PyQt5 import QtCore
# from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class ProjectController:
    def __init__(self):
        self.project_window = ProjectWindow()

        self.about_window = AboutWindow()

        self.project_tool_bar = ProjectToolBar()

        self.graph_information_dock = GraphInformationDock()
        self.invariants_check_dock = InvariantsCheckDock()
        self.visualize_graph_dock = VisualizeGraphDock()

        self.project_content_dictionary = ProjectContentDictionary()

    def show_window(self):
        self.connect_project_window_menu_actions()
        self.create_docks()
        self.project_window.addToolBar(self.project_tool_bar)
        self.project_window.setCentralWidget(self.project_content_dictionary)
        self.project_tool_bar.fill_combo_graphs(project_information_store.filtered_graphs)
        self.project_window.show()

    def connect_project_window_menu_actions(self):
        # self.project_window.print_action.triggered.connect(self.on_print)

        self.project_window.exit_action.triggered.connect(self.on_exit)
        self.project_window.visualize_action.triggered.connect(self.on_visualize)
        self.project_window.restore_default_layout_action.triggered.connect(self.on_restore)

        self.project_window.dictionary_action.triggered.connect(self.on_dictionary)
        self.project_window.about_action.triggered.connect(self.on_about)

        self.project_tool_bar.combo_graphs.activated.connect(self.change_graph)
        self.project_tool_bar.left_button.clicked.connect(self.move_up)
        self.project_tool_bar.right_button.clicked.connect(self.move_down)

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
        self.project_content_dictionary.setVisible(False)
        self.graph_information_dock.setVisible(True)
        self.invariants_check_dock.setVisible(True)
        self.visualize_graph_dock.setVisible(True)
        self.project_tool_bar.setVisible(True)

    def on_dictionary(self):
        self.graph_information_dock.setVisible(False)
        self.invariants_check_dock.setVisible(False)
        self.visualize_graph_dock.setVisible(False)
        self.project_tool_bar.setVisible(False)
        self.project_content_dictionary.setVisible(True)

    def on_about(self):
        self.about_window.show()

    def on_restore(self):
        pass

    def create_docks(self):
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants_check_dock)
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.visualize_graph_dock)
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.graph_information_dock)

    def change_graph(self):
        if self.project_tool_bar.combo_graphs.currentIndex() == 0:
            self.project_tool_bar.left_button.setDisabled(True)
        else:
            self.project_tool_bar.left_button.setDisabled(False)

        if self.project_tool_bar.combo_graphs.currentIndex() == self.project_tool_bar.combo_graphs.count() - 1:
            self.project_tool_bar.right_button.setDisabled(True)
        else:
            self.project_tool_bar.right_button.setDisabled(False)
        #
        # self.project_tool_bar.current_graph = match_graph_code(self.project_tool_bar.combo_graphs.currentText())
        # if self.project_tool_bar.current_graph is not None:
        #     self.visualize_graph_dock.plot_graph(self.project_tool_bar.current_graph)

        # self.graph_information_dock.update_graph_to_table()
        # self.info.update_table_inv({"test": self.combo_graphs.currentText()})

    def move_up(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() - 1)
        self.change_graph()

    def move_down(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() + 1)
        self.change_graph()
