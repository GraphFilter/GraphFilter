from PyQt5.QtWidgets import *
from src.views.windows.wizard.pages.project_files import ProjectFiles
from src.views.windows.wizard.pages.equations import Equations
from src.views.windows.wizard.pages.graph_files import GraphFiles
from src.views.windows.project.project_window import ProjectWindow
from PyQt5 import QtGui, QtCore
import json


class Wizard(QWizard):

    def __init__(self, main_window):
        super().__init__()

        # TODO: remove icon from window
        self.width = 900
        self.height = 600

        self.main_window = main_window
        self.project_window = ProjectWindow()

        self.project_files = ProjectFiles()
        self.equations = Equations()
        self.graph_files = GraphFiles()

        self.setWindowTitle("New Project")

        self.addPage(self.project_files)
        self.addPage(self.equations)
        self.addPage(self.graph_files)

        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setWizardStyle(QWizard.WizardStyle(0))

        pixmap = QtGui.QPixmap(1, 1)
        pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(pixmap))

        cancel = self.button(QWizard.CancelButton)
        cancel.clicked.connect(self.show_main_window)

        finish = self.button(QWizard.FinishButton)
        finish.clicked.connect(self.start_filter)

        self.setButtonText(QWizard.FinishButton, "Start")

    def closeEvent(self, event):
        self.main_window.show()

    def show_main_window(self):
        self.main_window.show()

    def start_filter(self):
        self.save_project()

        # NOTE: I believe that this point can do the filtering
        self.project_window.visualize.fill_combo(self.graph_files.return_files())  # filtering here
        self.project_window.show()

    def disable_next(self):
        self.button(QtGui.QWizard.NextButton).setEnabled(False)

    def save_project(self):
        project_dictionary = {
            "project_name": self.project_files.project_name_input.text(),
            "project_folder": self.project_files.project_location_input.text(),
            "equation": self.equations.equation.text(),
            "conditions": self.equations.radios,
            "method": self.equations.method,
            "graphs": self.graph_files.files_added
        }
        project_json = json.dumps(project_dictionary)

        project_location = self.project_files.project_location_input.text().replace('\\', '/')

        filename = f"{project_location}/{self.project_files.project_name_input.text()}.json"

        with open(filename, "w") as file_json:
            file_json.write(project_json)
            file_json.close()
