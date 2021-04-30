from src.view.welcome.welcome_window import WelcomeWindow
from src.view.welcome.welcome_content import WelcomeContent
from src.controller.wizard_controller import WizardController
from src.controller.project_controller import ProjectController
from PyQt5.QtWidgets import *
from src.store.project_information_store import project_information_store
import json


class WelcomeController:
    def __init__(self, welcome_window: WelcomeWindow):
        self.welcome_window = welcome_window
        self.welcome_content = WelcomeContent()
        self.wizard_controller = WizardController()
        self.project_controller = ProjectController()

    def show_window(self):
        self.welcome_window.setCentralWidget(self.welcome_content)
        self.connect_actions()
        self.welcome_window.show()

    def connect_actions(self):
        self.welcome_content.open_button.clicked.connect(self.on_open_project)
        self.welcome_content.new_button.clicked.connect(self.on_open_wizard)

    def on_open_wizard(self):
        self.welcome_window.close()
        self.wizard_controller.show_window()

    def on_open_project(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Json (*.json)"])
        file_path = file_dialog.getOpenFileName(filter="Json (*.json)")
        with open(file_path[0]) as file:
            content = file.read()
            data = json.loads(content)
            project_information_store.fill_data(data)
        self.project_controller.show_window()
        self.welcome_window.close()
