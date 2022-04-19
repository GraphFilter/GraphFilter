from source.controller.welcome_controller import WelcomeController
from source.controller.wizard_controller import WizardController
from source.controller.filter_controller import FilterController
from source.controller.project_controller import ProjectController
from source.store.project_information_store import update_project_store
from PyQt5.QtWidgets import *
from source.store.project_information_store import project_information_store
import json
from source.domain.exports import export_g6_to_png, export_g6_to_tikz, export_g6_to_pdf, export_g6_to_sheet
from source.view.loading.loading_window import LoadingWindow
from PyQt5 import QtCore


class Controller:

    def __init__(self):
        self.welcome_controller = WelcomeController()
        self.wizard_controller = WizardController()
        self.filter_controller = FilterController()
        self.project_controller = ProjectController()

        self.loading_window = LoadingWindow()

        self.current_open_window = ""

        self.connect_events()

    def connect_welcome_events(self):
        self.welcome_controller.welcome_content.new_button.clicked.connect(self.show_wizard_window)
        self.welcome_controller.welcome_content.open_button.clicked.connect(self.show_open_project_window)

    def connect_wizard_events(self):
        self.wizard_controller.wizard_window.cancel_button.clicked.connect(self.close_wizard_window)
        self.wizard_controller.wizard_window.close_signal.connect(self.close_wizard_window)
        self.wizard_controller.wizard_window.start_button.clicked.connect(self.start_filter)

    def connect_filter_events(self):
        self.filter_controller.loading_window.filter_complete_signal.connect(self.show_project_window)

    def connect_project_events(self):
        self.project_controller.project_window.new_action.triggered.connect(self.show_wizard_window)
        self.project_controller.project_window.open_action.triggered.connect(self.show_open_project_window)

        self.project_controller.project_window.export_png_action.triggered.connect(self.export_to_png)
        self.project_controller.project_window.export_g6_action.triggered.connect(self.export_to_g6)
        self.project_controller.project_window.export_tikz_action.triggered.connect(self.export_to_tikz)
        self.project_controller.project_window.export_pdf_action.triggered.connect(self.export_to_pdf)
        self.project_controller.project_window.export_sheet_action.triggered.connect(self.export_to_sheet)

    def connect_events(self):
        self.connect_welcome_events()
        self.connect_wizard_events()
        self.connect_filter_events()
        self.connect_project_events()

    def show_welcome_window(self):
        self.welcome_controller.show_window()
        self.current_open_window = "welcome"

    def show_open_project_window(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Json (*.json)"])
        file_path = file_dialog.getOpenFileName(filter="Json (*.json)")
        if file_path[0] == '':
            return
        with open(file_path[0]) as file:
            content = file.read()
            data = json.loads(content)
            project_information_store.fill_data(data)
        if self.current_open_window == "welcome":
            self.show_project_window()
            self.close_welcome_window()
        if self.current_open_window == "project":
            self.show_project_window()
        self.current_open_window = "project"

    def show_wizard_window(self):
        if self.current_open_window == "welcome":
            self.welcome_controller.close_window()

        self.wizard_controller = WizardController()
        self.connect_wizard_events()
        self.wizard_controller.show_window()

    def finish_filter(self):
        self.show_project_window()
        self.close_loading_window()

    def start_filter(self):
        update_project_store()
        self.filter_controller.start_filter()

    def show_project_window(self):
        self.project_controller.show_window()
        self.current_open_window = "project"

    def close_welcome_window(self):
        self.welcome_controller.close_window()

    def close_wizard_window(self):
        update_project_store()

        if self.current_open_window == "welcome":
            self.wizard_controller.close_window()
            self.welcome_controller.show_window()

        if self.current_open_window == "project":
            self.wizard_controller.close_window()
            self.project_controller.show_window()

    def close_loading_window(self):
        self.wizard_controller.close_window()

    def close_project_window(self):
        self.wizard_controller.close_window()

    def get_name_from_save_dialog(self, format_file):
        file_name = QFileDialog.getSaveFileName(parent=self.project_controller.project_window,
                                                caption=self.project_controller.project_window.tr(f"Export graphs to {format_file} file"),
                                                filter=self.project_controller.project_window.tr(f"Files (*.{format_file})"),
                                                directory=f"{project_information_store.project_name}.{format_file}"
                                                )[0]
        if file_name:
            if not QtCore.QFileInfo(file_name).suffix():
                file_name += f".{format_file}"
        return file_name

    def export_to_png(self):
        file_dir = str(QFileDialog.getExistingDirectory(parent=self.project_controller.project_window, caption="Select Directory"))
        if file_dir:
            self.show_loading_window(len(project_information_store.filtered_graphs))
            for step, graph in enumerate(project_information_store.filtered_graphs):
                export_g6_to_png(graph, file_dir, step)
                self.update_loading_window(step)
            self.loading_window.close()

    def export_to_tikz(self):
        file_dir = str(QFileDialog.getExistingDirectory(parent=self.project_controller.project_window, caption="Select Directory"))
        if file_dir:
            self.show_loading_window(len(project_information_store.filtered_graphs))
            for step, graph in enumerate(project_information_store.filtered_graphs):
                export_g6_to_tikz(graph, file_dir, step)
                self.update_loading_window(step)
            self.loading_window.close()

    def export_to_pdf(self):
        file_dir = str(QFileDialog.getExistingDirectory(parent=self.project_controller.project_window, caption="Select Directory"))
        if file_dir:
            self.show_loading_window(len(project_information_store.filtered_graphs))
            for step, graph in enumerate(project_information_store.filtered_graphs):
                export_g6_to_pdf(graph, file_dir, step)
                self.update_loading_window(step)
            self.loading_window.close()

    def export_to_g6(self):
        file_name = self.get_name_from_save_dialog('g6')
        if file_name:
            self.show_loading_window(len(project_information_store.filtered_graphs))
            file = open(file_name, 'w')
            for step, graph in enumerate(project_information_store.filtered_graphs):
                file.write(f'{graph}\n')
                self.update_loading_window(step)
            file.close()
            self.loading_window.close()

    def export_to_sheet(self):
        file_name = self.get_name_from_save_dialog('xlsx')
        if file_name:
            self.show_loading_window(len(project_information_store.filtered_graphs))
            export_g6_to_sheet(graph_list=project_information_store.filtered_graphs,
                               invariants=self.project_controller.invariants_selected,
                               file_name=file_name,
                               update_progress=self.update_loading_window)
            self.loading_window.close()

    def show_loading_window(self, set_total):
        self.loading_window.progressBar.setMaximum(set_total)
        self.loading_window.progressBar.setValue(0)
        self.loading_window.show()

    def update_loading_window(self, step):
        self.loading_window.increase_step(step)
        QApplication.processEvents()
