import os.path

from PyQt5.QtGui import QCursor
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from source.domain.utils_file import create_gml_file, change_gml_file, import_gml_graph, change_g6_file, \
    delete_all_gml_nodes
from source.store.export_graph_to import dict_name_export_graph_to
from source.store.operations_graph import dict_name_operations_graph
from source.view.project.project_tool_bar import EditingFeatures
from source.view.project.project_window import ProjectWindow
from source.view.project.project_tool_bar import ProjectToolBar
from source.view.project.about_window import AboutWindow
from source.view.loading.loading_gif import LoadingGif
from source.view.project.docks.graph_information_dock import GraphInformationDock
from source.view.project.docks.visualize_graph_dock import VisualizeGraphDock
from source.view.project.docks.tree_file_dock import TreeFileDock
from source.view.project.docks.invariants_checks_dock import InvariantsCheckDock
from source.store.operations_invariants import *
from source.store.new_graph_store import *
from source.domain.utils import match_graph_code, add_vertex, handle_invalid_graph_open, trigger_message_box
from PyQt5.Qt import QUrl, QDesktopServices
import json
import threading as td


class ProjectController:
    def __init__(self):
        self.project_window = ProjectWindow()

        self.about_window = AboutWindow()

        self.project_tool_bar = ProjectToolBar()

        self.graph_information_dock = GraphInformationDock()
        self.invariants_check_dock = InvariantsCheckDock()
        self.visualize_graph_dock = VisualizeGraphDock()
        self.tree_file_dock = TreeFileDock()

        self.loading_gif = LoadingGif()
        self.is_gif_in_progress = False

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
            handle_invalid_graph_open()
            self.visualize_graph_dock.plot_graph(nx.Graph())

        if project_information_store.get_file_type() == '.gml':
            self.project_tool_bar.combo_graphs.setItemText(0, 'Graph - ' + project_information_store.get_file_name())
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
        self.project_window.new_issue_action.triggered.connect(self.on_new_issues)

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
        self.project_tool_bar.operations_menu.triggered.connect(self.on_operations_button)
        self.project_tool_bar.export_menu.triggered.connect(self.on_export_button)
        self.project_tool_bar.universal_vertex_button.clicked.connect(self.insert_universal_vertex)

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
        if file_type == ".gml":
            try:
                self.visualize_graph_dock.plot_graph(delete_all_gml_nodes(project_information_store.file_path))
            except:
                pass

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
        # self.project_tool_bar.combo_graphs.setStyleSheet('color: black')
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

    @staticmethod
    def on_new_issues():
        QDesktopServices.openUrl(QUrl("https://github.com/GraphFilter/GraphFilter/issues/new"))

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

    def on_invalid_graph_display_alert(self):
        index = self.project_tool_bar.combo_graphs.currentIndex()
        self.project_tool_bar.combo_graphs.setItemText(index, f'Graph {index} - Invalid')
        # self.project_tool_bar.combo_graphs.setStyleSheet('color: red')
        trigger_message_box("Invalid Graph", window_title="Invalid Graph")

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
                self.project_tool_bar.combo_graphs.setDisabled(True)
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
        node_positions = project_information_store.current_graph_pos
        graph, node_positions = add_vertex(graph, node_positions, len(graph), univ=True)

        if len(graph) == 1:
            self.visualize_graph_dock.plot_graph(graph)
        else:
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
                return ''
        else:
            try:
                os.remove(file_path)
                if file_path == project_information_store.file_path:
                    self.project_tool_bar.reset_combo_graphs()
                    self.project_tool_bar.fill_combo_graphs("?")
                    self.on_change_graph()
                    self.visualize_graph_dock.setDisabled(True)
                    project_information_store.file_path = os.path.dirname(file_path)
                    trigger_message_box("You erased the current file. To continue, please create a new graph or select "
                                        "another file in the directory.", window_title="Select another file")
            except FileNotFoundError:
                return
            except PermissionError:
                return
            except OSError:
                return

    def handle_tree_double_click(self):
        single_thread = td.Thread(target=self.open_tree_file_graphs)
        single_thread.start()
        self.loading_gif.start_animation()
        self.loading_gif.show()
        self.is_gif_in_progress = True
        self.project_window.setDisabled(True)

        while self.is_gif_in_progress:
            QApplication.processEvents()

        single_thread.join()
        self.loading_gif.close()

        self.project_tool_bar.combo_graphs.setCurrentIndex(0)
        self.project_window.set_title_bar(project_information_store.get_file_name())
        self.update_graph_to_table()
        if len(project_information_store.current_graph_pos) != 0 and \
                project_information_store.get_file_type() == ".gml":
            self.visualize_graph_dock.plot_graph(project_information_store.current_graph,
                                                 project_information_store.current_graph_pos)
        else:
            project_information_store.current_graph_pos = {}
            self.visualize_graph_dock.plot_graph(project_information_store.current_graph)

    def open_tree_file_graphs(self):
        index = self.tree_file_dock.tree.currentIndex()
        file_path = self.tree_file_dock.model.filePath(index)
        type_item = self.tree_file_dock.model.type(index)

        if type_item == "File Folder":
            return

        project_information_store.file_path = file_path

        if type_item == "gml File":
            graph = import_gml_graph(file_path)
            graphs = [project_information_store.get_file_name()]
            if graph is not None:
                project_information_store.current_graph = graph
            else:
                handle_invalid_graph_open()
                project_information_store.current_graph = nx.Graph()
            self.project_tool_bar.combo_graphs.setDisabled(True)
        else:
            if type_item == "json File":
                f = open(file_path)
                data = json.load(f)
                graphs = tuple(data['filtered_graphs'])
            else:
                with open(file_path) as file:
                    graphs = file.read().splitlines()
            project_information_store.current_graph = nx.from_graph6_bytes(graphs[0].encode('utf-8'))
            self.project_tool_bar.combo_graphs.setEnabled(True)

        self.project_tool_bar.reset_combo_graphs()
        self.project_tool_bar.fill_combo_graphs(graphs)

        self.project_window.setDisabled(False)

        self.is_gif_in_progress = False
        self.visualize_graph_dock.setDisabled(False)
        self.project_tool_bar.set_file_label(project_information_store.get_file_name())

    def update_graph_to_table(self):
        graph = project_information_store.current_graph

        for key in self.invariants_selected.keys():
            if len(graph) == 0:
                self.invariants_selected[key] = "Null Graph"
            else:
                try:
                    self.invariants_selected[key] = dic_invariants_to_visualize[key].print(graph, precision=5)
                except:
                    self.invariants_selected[key] = "ERROR in calculation, please report problem."

        self.graph_information_dock.update_table(self.invariants_selected)

    def on_save_graph(self):
        current_index = self.project_tool_bar.combo_graphs.currentIndex()

        file_path = project_information_store.file_path
        file_name, file_type = os.path.splitext(file_path)
        current_graph = project_information_store.current_graph
        graph = None

        if current_graph is None:
            return
        else:
            new_g6 = nx.to_graph6_bytes(current_graph, header=False).decode("utf-8")[:-1]

        if file_type == ".g6" or file_type == ".txt":
            graph = change_g6_file(file_path, new_g6, current_index)
        if file_type == ".json":
            trigger_message_box("Graph editing is not allowed in .json format, only in .g6, .txt and .gml formats. "
                                "To allow manipulation and saving: \n"
                                "  I. You can export the entire list of graphs list of graphs to g6 by pressing "
                                "right button on the desired file. \n"
                                "  II. Or you can convert this specific graph with the options available in the "
                                "toolbar", window_title="Invalid save format")
        if file_type == ".gml":
            graph = change_gml_file(file_path)

        if graph is None:
            return

        self.project_tool_bar.reset_combo_graphs()
        self.project_tool_bar.fill_combo_graphs(graph)
        self.project_tool_bar.combo_graphs.setCurrentIndex(current_index)
        # self.project_tool_bar.combo_graphs.setStyleSheet('color: black;')
        self.graph_information_dock.update_table(self.invariants_selected)
