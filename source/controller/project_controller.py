import os.path

import networkx as nx
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from source.domain.utils_file import create_gml_file, change_gml_file, import_gml_graph, change_g6_file
from source.store.export_graph_to import dict_name_export_graph_to
from source.store.operations_graph import dict_name_operations_graph
from source.view.project.project_tool_bar import EditingFeatures
from source.view.project.project_window import ProjectWindow
from source.view.project.project_tool_bar import ProjectToolBar
from source.view.project.about_window import AboutWindow
from source.view.project.docks.graph_information_dock import GraphInformationDock
from source.view.project.docks.visualize_graph_dock import VisualizeGraphDock
from source.view.project.docks.tree_file_dock import TreeFileDock
from source.view.project.docks.invariants_checks_dock import InvariantsCheckDock
from source.store.operations_invariants import *
from source.store.new_graph_store import *
from source.domain.utils import match_graph_code, set_new_vertex_positions
from source.view.components.message_box import MessageBox
from PyQt5.Qt import QUrl, QDesktopServices
import json


class ProjectController:
    def __init__(self):
        self.project_window = ProjectWindow()

        self.about_window = AboutWindow()

        self.project_tool_bar = ProjectToolBar()

        self.graph_information_dock = GraphInformationDock()
        self.invariants_check_dock = InvariantsCheckDock()
        self.visualize_graph_dock = VisualizeGraphDock()
        self.tree_file_dock = TreeFileDock()

        self.editing_features = EditingFeatures()

        self.invariants_selected = {}

        self.active_new_graph_action = None
        self.active_operation_action = None
        self.active_export_action = None

        self.settings = QtCore.QSettings("project", "GraphFilter")
        self.connect_events()

    def show_window(self):
        self.create_docks()

        self.project_window.set_title_bar(project_information_store.temp_project_name)
        self.project_window.addToolBar(self.project_tool_bar)

        self.project_tool_bar.reset_combo_graphs()

        self.project_tool_bar.current_graph = \
            self.project_tool_bar.fill_combo_graphs(project_information_store.temp_filtered_graphs)

        if project_information_store.current_graph is not None:
            if len(project_information_store.current_graph_pos) != 0:
                self.visualize_graph_dock.plot_graph(project_information_store.current_graph,
                                                     project_information_store.current_graph_pos)
            else:
                self.visualize_graph_dock.plot_graph(project_information_store.current_graph)
        else:
            dlg = QMessageBox()
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("The file you tried to open contains an invalid graph. "
                        "Open another file in the tree or in the menu option")
            dlg.setWindowTitle("Invalid graph")
            dlg.exec()
            self.visualize_graph_dock.plot_graph(nx.Graph())

        if project_information_store.get_file_type() == '.gml':
            self.project_tool_bar.combo_graphs.setDisabled(True)

        self.project_tool_bar.set_file_label(project_information_store.get_file_name())

        self.invariants_check_dock.create_conditions(dic_invariants_to_visualize, self.on_check_condition)

        self.project_window.showMaximized()

        self.settings.setValue("state", self.project_window.saveState())

    def connect_events(self):

        self.project_window.exit_action.triggered.connect(self.on_exit)

        self.project_window.visualize_action.triggered.connect(self.on_visualize)
        self.project_window.invariants_check_action.triggered.connect(self.on_invariants_check)
        self.project_window.graph_info_action.triggered.connect(self.on_graph_info)
        self.project_window.visualize_tree_action.triggered.connect(self.on_visualize_tree)

        self.project_window.dictionary_action.triggered.connect(self.on_dictionary)

        self.project_window.restore_layout_action.triggered.connect(self.on_restore)

        self.project_window.about_action.triggered.connect(self.on_about)

        self.tree_file_dock_events()

        self.connect_tool_bar_events()

        self.visualize_graph_dock.any_signal.connect(self.update_graph_to_table)

        self.visualize_graph_dock.invalid_graph_signal.connect(self.on_invalid_graph_display_alert)

        self.project_tool_bar.features_info_button.triggered.connect(self.show_editing_features)

        self.project_tool_bar.new_graph_menu.hovered.connect(self.set_active_new_graph_action)
        self.project_tool_bar.operations_menu.hovered.connect(self.set_active_operation_action)
        self.project_tool_bar.export_menu.hovered.connect(self.set_active_export_action)
        self.project_tool_bar.new_graph_menu.triggered.connect(self.on_new_graph_button)
        self.project_tool_bar.operations_menu_bar.triggered.connect(self.on_operations_button)
        self.project_tool_bar.export_menu.triggered.connect(self.on_export_button)
        self.project_tool_bar.universal_vertex_button.triggered.connect(self.insert_universal_vertex)

    def tree_file_dock_events(self):
        self.tree_file_dock.tree.doubleClicked.connect(self.handle_tree_double_click)
        self.tree_file_dock.tree.customContextMenuRequested.connect(self.tree_context_menu_events)

    def connect_tool_bar_events(self):
        self.project_tool_bar.combo_graphs.activated.connect(self.on_change_graph)
        self.project_tool_bar.left_button.clicked.connect(self.on_click_button_left)
        self.project_tool_bar.right_button.clicked.connect(self.on_click_button_right)

        self.project_tool_bar.save_button.triggered.connect(self.on_save_graph)
        self.project_tool_bar.delete_button.triggered.connect(self.delete_graph)

    def delete_graph(self):
        current_index = self.project_tool_bar.combo_graphs.currentIndex()
        file_path = project_information_store.file_path
        file_name, file_type = os.path.splitext(file_path)

        if current_index > 0:
            next_index = current_index - 1
        else:
            next_index = 0

        if file_type == ".g6" or file_type == ".txt":
            file = open(file_path, "r")
            changed_data = file.readlines()
            changed_data[current_index] = ""
            file.close()

            with open(file_path, "w", encoding="utf-8") as file:
                if changed_data == [""]:
                    file.writelines("?")
                else:
                    file.writelines(changed_data)

            with open(file_path) as file:
                graph = file.read().splitlines()
                self.project_tool_bar.reset_combo_graphs()
                self.project_tool_bar.fill_combo_graphs(graph)
                self.project_tool_bar.combo_graphs.setCurrentIndex(next_index)
                self.on_change_graph()

        if file_type == ".json":
            f = open(file_path)
            data = json.load(f)
            graph = list(data['filtered_graphs'])

            graph.pop(current_index)
            graph = tuple(graph)
            if graph == ():
                graph = "?"
                project_information_store.temp_filtered_graphs = graph
            else:
                project_information_store.temp_filtered_graphs = graph
            project_information_store.save_project()

            f = open(file_path)
            new_data = json.load(f)
            new_json_file = tuple(new_data['filtered_graphs'])

            self.project_tool_bar.reset_combo_graphs()
            if new_json_file == ():
                new_json_file = ["?"]

            self.project_tool_bar.fill_combo_graphs(new_json_file)
            self.project_tool_bar.combo_graphs.setCurrentIndex(next_index)
            self.on_change_graph()

    def create_docks(self):
        self.tree_file_dock.create_tree()
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.tree_file_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.visualize_graph_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants_check_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.graph_information_dock)
        # self.project_window.setTabPosition(QtCore.Qt.RightDockWidgetArea, QTabWidget.East)

        self.graph_information_dock.setMaximumHeight(250)
        self.tree_file_dock.setMaximumWidth(250)
        self.project_window.splitDockWidget(self.visualize_graph_dock, self.invariants_check_dock,
                                            QtCore.Qt.Horizontal)

    def on_exit(self):
        self.project_window.close()

    def show_editing_features(self):
        self.editing_features.show()

    def on_visualize_tree(self):
        self.tree_file_dock.setVisible(True)

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
        # self.on_visualize_tree()

    def on_change_graph(self):
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

        self.graph_information_dock.update_table(self.invariants_selected)

    def on_click_button_left(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() - 1)
        self.on_change_graph()

    def on_click_button_right(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() + 1)
        self.on_change_graph()

    @staticmethod
    def on_dictionary():
        QDesktopServices.openUrl(QUrl("https://github.com/GraphFilter/GraphFilter/wiki/Dictionary"))

    def on_check_condition(self):
        check = QCheckBox().sender()
        graph = project_information_store.current_graph
        g6code = nx.to_graph6_bytes(graph, header=False).decode('utf-8')

        if check.text() not in self.invariants_selected:
            if graph is not None:
                if len(graph) == 0:
                    self.invariants_selected[check.text()] = \
                        "None Graph"
                else:
                    self.invariants_selected[check.text()] = \
                        dic_invariants_to_visualize[check.text()].print(graph, precision=5)
            else:
                if g6code is not None:
                    self.invariants_selected[check.text()] = \
                        dic_invariants_to_visualize[check.text()].print(graph, precision=5)
                else:
                    self.invariants_selected[check.text()] = 'No graph selected'
        else:
            del self.invariants_selected[check.text()]

        self.graph_information_dock.update_table(self.invariants_selected)

    @staticmethod
    def on_invalid_graph_display_alert():
        message_box = MessageBox("Invalid Graph")
        message_box.exec()

    def on_new_graph_button(self):
        new_graph_dict_name[self.active_new_graph_action].open_dialog()
        graph = new_graph_store.graph
        layout = new_graph_store.layout
        file_path = new_graph_store.file_path

        if graph is not None:
            try:
                graph_g6 = nx.to_graph6_bytes(graph, header=False).decode('utf-8')
            except AttributeError:
                graph_g6 = graph

            if new_graph_store.radio_option == 0:
                project_information_store.file_path = file_path
                create_gml_file(graph, file_path)

                self.project_tool_bar.reset_combo_graphs()
                self.project_tool_bar.fill_combo_graphs([project_information_store.get_file_name()])
                self.graph_information_dock.update_table(self.invariants_selected)
                self.visualize_graph_dock.plot_graph(graph, layout)
                change_gml_file(file_path)

            else:
                self.project_tool_bar.combo_graphs.addItem(f'Graph {self.project_tool_bar.combo_graphs.count()}'
                                                           f' - {graph_g6}')
                self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.count() - 1)
                self.visualize_graph_dock.plot_graph(graph, layout)
                self.on_save_graph()

            self.visualize_graph_dock.setDisabled(False)
            new_graph_store.reset_attributes()

    def on_operations_button(self):
        graph = dict_name_operations_graph[self.active_operation_action]. \
            calculate(project_information_store.current_graph)

        if graph is not None:
            self.visualize_graph_dock.plot_graph(graph)

    def on_export_button(self):
        dict_name_export_graph_to[self.active_export_action].export()

    def set_active_new_graph_action(self):
        if self.project_tool_bar.new_graph_menu.activeAction() is not None:
            self.active_new_graph_action = self.project_tool_bar.new_graph_menu.activeAction().text()

    def set_active_operation_action(self):
        if self.project_tool_bar.operations_menu.activeAction() is not None:
            self.active_operation_action = self.project_tool_bar.operations_menu.activeAction().text()

    def set_active_export_action(self):
        if self.project_tool_bar.export_menu.activeAction() is not None:
            self.active_export_action = self.project_tool_bar.export_menu.activeAction().text()

    def insert_universal_vertex(self):
        graph = project_information_store.current_graph
        new_vertex = len(graph)
        node_positions = project_information_store.current_graph_pos
        graph.add_node(new_vertex)

        for node in graph:
            if node is not new_vertex:
                graph.add_edge(new_vertex, node)

        node_positions[new_vertex] = set_new_vertex_positions(node_positions)

        self.visualize_graph_dock.plot_graph(graph, node_positions)

    def tree_context_menu_events(self):
        self.tree_file_dock.load_file.triggered.connect(self.handle_tree_double_click)

        self.tree_file_dock.delete_file.triggered.disconnect()
        self.tree_file_dock.delete_file.triggered.connect(self.delete_confirmation)

        cursor = QCursor()
        self.tree_file_dock.menu.exec(cursor.pos())

    def delete_confirmation(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Delete confirmation")
        dlg.setText("Are you sure you want to delete this ")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setDefaultButton(QMessageBox.No)
        if dlg.exec_() == QMessageBox.Yes:
            self.delete_tree_file()
            return
        else:
            pass

    def delete_tree_file(self):
        index = self.tree_file_dock.tree.currentIndex()
        file_path = self.tree_file_dock.model.filePath(index)
        type_item = self.tree_file_dock.model.type(index)
        if type_item == "File Folder":
            try:
                os.rmdir(file_path)
            except FileNotFoundError:
                return
            except PermissionError:
                return
            except OSError:
                return''
        else:
            try:
                os.remove(file_path)
                if file_path == project_information_store.file_path:
                    self.project_tool_bar.reset_combo_graphs()
                    self.project_tool_bar.fill_combo_graphs("?")
                    self.on_change_graph()
                    self.visualize_graph_dock.setDisabled(True)
                    project_information_store.file_path = os.path.dirname(file_path)
                    dlg = QMessageBox()
                    dlg.setIcon(QMessageBox.Information)
                    dlg.setText("You erased the current file. To continue, please create a new graph or select another"
                                " file in the directory.")
                    dlg.setWindowTitle("Select another file")
                    dlg.exec()
            except FileNotFoundError:
                return
            except PermissionError:
                return
            except OSError:
                return
        # File Folder

    def handle_tree_double_click(self):
        index = self.tree_file_dock.tree.currentIndex()
        file_path = self.tree_file_dock.model.filePath(index)

        type_item = self.tree_file_dock.model.type(index)
        if type_item == "json File":
            f = open(file_path)
            data = json.load(f)
            graph = tuple(data['filtered_graphs'])
            self.project_tool_bar.reset_combo_graphs()
            self.project_tool_bar.fill_combo_graphs(graph)
            self.on_change_graph()
            project_information_store.file_path = file_path
            self.project_tool_bar.combo_graphs.setEnabled(True)
        if type_item == "g6 File" or type_item == "txt File":
            with open(file_path) as file:
                graph = file.read().splitlines()
                self.project_tool_bar.reset_combo_graphs()
                self.project_tool_bar.fill_combo_graphs(graph)
                self.on_change_graph()
                project_information_store.file_path = file_path
            self.project_tool_bar.combo_graphs.setEnabled(True)
        if type_item == "gml File":
            project_information_store.file_path = file_path
            graph = import_gml_graph(file_path)
            self.project_tool_bar.reset_combo_graphs()
            self.project_tool_bar.fill_combo_graphs([project_information_store.get_file_name()])
            if graph is not None:
                if len(project_information_store.current_graph_pos) != 0:
                    self.visualize_graph_dock.plot_graph(graph,
                                                         project_information_store.current_graph_pos)
                else:
                    self.visualize_graph_dock.plot_graph(graph)
            else:
                dlg = QMessageBox()
                dlg.setIcon(QMessageBox.Information)
                dlg.setText("The file you tried to open contains an invalid graph. "
                            "Open another file in the tree or in the menu option")
                dlg.setWindowTitle("Invalid graph")
                dlg.exec()
                self.visualize_graph_dock.plot_graph(nx.Graph())
            self.project_tool_bar.combo_graphs.setDisabled(True)
        else:
            pass
        self.visualize_graph_dock.setDisabled(False)
        self.project_tool_bar.set_file_label(project_information_store.get_file_name())
        self.project_window.set_title_bar(project_information_store.get_file_name())

    def update_graph_to_table(self):
        graph = project_information_store.current_graph

        for key in self.invariants_selected.keys():
            if len(graph) == 0:
                self.invariants_selected[key] = "Null Graph"
            else:
                self.invariants_selected[key] = dic_invariants_to_visualize[key].print(graph, precision=5)

        self.graph_information_dock.update_table(self.invariants_selected)

    def on_save_graph(self):
        current_index = self.project_tool_bar.combo_graphs.currentIndex()

        file_path = project_information_store.file_path
        file_name, file_type = os.path.splitext(file_path)
        current_graph = project_information_store.current_graph
        graph = None
        new_g6 = ""
        replaced_line = ""

        if current_graph is None:
            return
        else:
            new_g6 = nx.to_graph6_bytes(current_graph, header=False).decode("utf-8")[:-1]

        if file_type == ".g6" or file_type == ".txt":
            graph = change_g6_file(file_path, new_g6, current_index)
        if file_type == ".json":
            dlg = QMessageBox()
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("Graph editing is not allowed in .json format, only in .g6, .txt and .gml formats. "
                        "To allow manipulation and saving: \n"
                        "  I. You can export the entire list of graphs list of graphs to g6 by pressing "
                        "right button on the desired file. \n"
                        "  II. Or you can convert this specific graph with the options available in the toolbar")
            dlg.setWindowTitle("Invalid save format")
            dlg.exec()
            return
        if file_type == ".gml":
            graph = [project_information_store.get_file_name()]
            change_gml_file(file_path)

        self.project_tool_bar.reset_combo_graphs()
        self.project_tool_bar.fill_combo_graphs(graph)
        self.project_tool_bar.combo_graphs.setCurrentIndex(current_index)
        self.graph_information_dock.update_table(self.invariants_selected)
