import json

import networkx as nx
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtWidgets import *

from deprecated.controller.filter_controller import FilterController
from deprecated.controller.project_controller import ProjectController
from deprecated.controller.welcome_controller import WelcomeController
from deprecated.controller.wizard_controller import WizardController
from deprecated import utils_file
from deprecated.exports import export_g6_to_png, export_g6_to_tikz, export_g6_to_pdf, export_g6_to_sheet
from deprecated.utils import trigger_message_box, handle_invalid_export_format
from deprecated.utils_file import import_gml_graph, create_gml_file
from deprecated.store.project_information_store import project_information_store
from deprecated.store.project_information_store import update_project_store
from deprecated.view.windows.progress_bar_window import ProgressBarWindow


class Controller:

    def __init__(self):
        self.welcome_controller = WelcomeController()
        self.wizard_controller = WizardController()
        self.filter_controller = FilterController()
        self.project_controller = ProjectController()

        self.progress_bar_window = ProgressBarWindow()

        self.current_open_window = ""

        self.connect_events()

    def connect_welcome_events(self):
        self.welcome_controller.welcome_window.content.new_button.clicked.connect(self.show_wizard_window)
        self.welcome_controller.welcome_window.content.open_button.clicked.connect(self.show_open_project_window)

    def connect_wizard_events(self):
        self.wizard_controller.wizard_window.cancel_button.clicked.connect(self.close_wizard_window)
        self.wizard_controller.wizard_window.close_signal.connect(self.close_wizard_window)
        self.wizard_controller.wizard_window.start_button.clicked.connect(self.finish_wizard)

    def connect_project_events(self):
        self.project_controller.project_window.new_action.triggered.connect(self.show_wizard_window)
        self.project_controller.project_window.open_action.triggered.connect(self.show_open_project_window)

        self.project_controller.tree_file_dock.export_png_action.triggered.connect(self.export_to_png)
        self.project_controller.tree_file_dock.export_g6_action.triggered.connect(self.export_to_g6)
        self.project_controller.tree_file_dock.export_tikz_action.triggered.connect(self.export_to_tikz)
        self.project_controller.tree_file_dock.export_pdf_action.triggered.connect(self.export_to_pdf)
        self.project_controller.tree_file_dock.export_sheet_action.triggered.connect(self.export_to_sheet)

    def connect_events(self):
        self.connect_welcome_events()
        self.connect_wizard_events()
        self.connect_project_events()

    def show_welcome_window(self):
        self.welcome_controller.show_window()
        self.current_open_window = "welcome"

    def show_open_project_window(self):
        file_dialog = QFileDialog()
        default_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        file_dialog.setNameFilters(["Graph File (*.gml *.g6 *.txt *.json)"])
        file_path = file_dialog.getOpenFileName(filter="Graph File (*.gml *.g6 *.txt *.json)", directory=default_dir)
        project_information_store.file_path = file_path[0]
        project_information_store.current_graph_pos = {}
        file_type = project_information_store.get_file_type()

        if file_type == '':
            return
        if file_type == '.json':
            with open(file_path[0]) as file:
                content = file.read()
                data = json.loads(content)
                project_information_store.fill_data(data)
            project_information_store.current_graph = project_information_store.temp_filtered_graphs[0]
        else:
            if file_type == '.gml':
                project_information_store.temp_filtered_graphs = [project_information_store.get_file_name()]
                project_information_store.current_graph = import_gml_graph(file_path[0])
            else:
                with open(file_path[0]) as file:
                    project_information_store.temp_filtered_graphs = file.read().splitlines()
                try:
                    project_information_store.current_graph = project_information_store.temp_filtered_graphs[0]
                except IndexError:
                    project_information_store.current_graph = None

            project_information_store.temp_graph_input_files = project_information_store.file_path

        if self.current_open_window == "project" and project_information_store.get_file_type() != ".gml":
            project_information_store.current_graph_pos = {}
        self.show_project_window()
        project_information_store.reset_store()

    def show_wizard_window(self):
        if self.current_open_window == "welcome":
            self.welcome_controller.close_window()

        self.wizard_controller = WizardController()
        self.connect_wizard_events()
        self.wizard_controller.show_window()

    def start_project(self):
        if not project_information_store.temp_filtered_graphs:
            trigger_message_box("No graph in the input list satisfies the chosen conditions.",
                                window_title="Empty filtering")
            self.show_wizard_window()
        else:
            if project_information_store.temp_method == 'blank':
                project_information_store.current_graph = nx.Graph()
            else:
                project_information_store.current_graph = project_information_store.temp_filtered_graphs[0]
            self.show_project_window()
            project_information_store.reset_store()

    def finish_wizard(self):
        update_project_store()
        project_information_store.current_graph_pos = {}
        if project_information_store.temp_method == 'blank':
            graph = nx.Graph()
            project_information_store.file_path = \
                project_information_store.file_path + "/" + project_information_store.temp_project_name + ".gml"
            project_information_store.temp_filtered_graphs = [project_information_store.temp_project_name]
            create_gml_file(graph, project_information_store.file_path)
            self.start_project()
        else:
            self.filter_controller.start_filter()

            if self.filter_controller.is_complete_filtering:
                self.start_project()
            else:
                self.show_welcome_window()

    def show_project_window(self):
        self.project_controller.show_window()
        self.project_controller.project_window.set_title_bar(project_information_store.get_file_name())
        self.close_welcome_window()
        self.current_open_window = "project"

    def close_welcome_window(self):
        self.welcome_controller.close_window()

    def close_wizard_window(self):
        update_project_store()

        if self.current_open_window == "welcome":
            self.wizard_controller.close_window()
            self.welcome_controller.show_window()

        # if self.current_open_window == "project":
        #     self.wizard_controller.close_window()
        #     self.project_controller.show_window()

    def close_loading_window(self):
        self.wizard_controller.close_window()

    def close_project_window(self):
        self.wizard_controller.close_window()

    def get_graph_from_tree(self):
        index = self.project_controller.tree_file_dock.tree.currentIndex()
        file_path = self.project_controller.tree_file_dock.model.filePath(index)
        type_item = self.project_controller.tree_file_dock.model.type(index)

        if type_item == "json File":
            f = open(file_path)
            data = json.load(f)
            return tuple(data['num_filtered_graphs'])
        if type_item == "g6 File" or type_item == "txt File":
            with open(file_path) as file:
                return file.read().splitlines()

        return None

    def export_to_png(self):
        try:
            graph_to_export = self.get_graph_from_tree()
        except:
            return

        if graph_to_export is None:
            handle_invalid_export_format()
            return

        file_dir = utils_file.get_directory_name_from_existing_directory()
        if file_dir:
            self.show_loading_window(len(graph_to_export))
            for step, graph in enumerate(graph_to_export):
                if self.progress_bar_window.is_forced_to_close:
                    self.progress_bar_window.is_forced_to_close = False
                    return
                try:
                    export_g6_to_png(graph, file_dir, step)
                except:
                    pass
                self.update_loading_window(step)
            self.progress_bar_window.close()

    def export_to_tikz(self):
        try:
            graph_to_export = self.get_graph_from_tree()
        except:
            return

        if graph_to_export is None:
            handle_invalid_export_format()
            return

        file_name = utils_file.get_name_from_save_dialog('tex')
        if file_name:
            self.show_loading_window(len(graph_to_export))
            for step, graph in enumerate(graph_to_export):
                if self.progress_bar_window.is_forced_to_close:
                    self.progress_bar_window.is_forced_to_close = False
                    return
                try:
                    export_g6_to_tikz(graph, file_name, step)
                except:
                    pass
                self.update_loading_window(step)
            self.progress_bar_window.close()

    def export_to_pdf(self):
        try:
            graph_to_export = self.get_graph_from_tree()
        except:
            return

        if graph_to_export is None:
            handle_invalid_export_format()
            return

        file_dir = utils_file.get_directory_name_from_existing_directory()
        if file_dir:
            self.show_loading_window(len(graph_to_export))
            for step, graph in enumerate(graph_to_export):
                if self.progress_bar_window.is_forced_to_close:
                    self.progress_bar_window.is_forced_to_close = False
                    return
                try:
                    export_g6_to_pdf(graph, file_dir, step)
                except:
                    pass
                self.update_loading_window(step)
            self.progress_bar_window.close()

    def export_to_g6(self):
        try:
            graph_to_export = self.get_graph_from_tree()
        except:
            return

        if graph_to_export is None:
            handle_invalid_export_format()
            return

        file_name = utils_file.get_name_from_save_dialog('g6')
        if file_name:
            self.show_loading_window(len(graph_to_export))
            file = open(file_name, 'w')
            for step, graph in enumerate(graph_to_export):
                if self.progress_bar_window.is_forced_to_close:
                    self.progress_bar_window.is_forced_to_close = False
                    return
                file.write(f'{graph}\n')
                self.update_loading_window(step)
            file.close()
            self.progress_bar_window.close()

    def export_to_sheet(self):
        try:
            graph_to_export = self.get_graph_from_tree()
        except:
            return

        if graph_to_export is None:
            handle_invalid_export_format()
            return

        file_name = utils_file.get_name_from_save_dialog('xlsx')
        if file_name:
            self.show_loading_window(len(graph_to_export))
            try:
                export_g6_to_sheet(graph_list=graph_to_export,
                                   invariants=self.project_controller.invariants_selected,
                                   file_name=file_name,
                                   update_progress=self.update_loading_window,
                                   loading_window=self.progress_bar_window)
            except:
                pass
            self.progress_bar_window.close()

    def show_loading_window(self, set_total):
        self.progress_bar_window.progress_bar.setMaximum(set_total)
        self.progress_bar_window.progress_bar.setValue(0)
        self.progress_bar_window.show()

    def update_loading_window(self, step):
        self.progress_bar_window.increase_step(step)
        QApplication.processEvents()
