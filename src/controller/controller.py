from src.controller.welcome_controller import WelcomeController
from src.controller.wizard_controller import WizardController
from src.controller.filter_controller import FilterController
from src.controller.project_controller import ProjectController
from src.store.project_information_store import update_project_store
from PyQt5.QtWidgets import *
from src.store.project_information_store import project_information_store
import json


class Controller:

    def __init__(self):
        self.welcome_controller = WelcomeController()
        self.wizard_controller = WizardController()
        self.filter_controller = FilterController()
        self.project_controller = ProjectController()

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
