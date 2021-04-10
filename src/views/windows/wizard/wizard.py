from PyQt5.QtWidgets import *

from src.domain.filter_list import FilterList
from src.views.windows.wizard.pages.project_files import ProjectFiles
from src.views.windows.wizard.pages.equations import Equations
from src.views.windows.wizard.pages.conditions import Conditions
from src.views.windows.wizard.pages.method import Method
from src.views.windows.wizard.pages.graph_files import GraphFiles
from src.views.windows.wizard.pages.review import Review
from src.views.windows.project.project_window import ProjectWindow
from PyQt5 import QtGui, QtCore
import json


class Wizard(QWizard):

    def __init__(self, main_window):
        super().__init__()

        self.filter_backend = FilterList()

        # TODO: remove icon from window
        self.width = 900
        self.height = 600

        self.main_window = main_window
        self.project_window = ProjectWindow()

        self.project_files = ProjectFiles()
        self.equations = Equations()
        self.conditions = Conditions(self.equations)
        self.method = Method()
        self.graph_files = GraphFiles()
        self.review = Review(self)

        self.setWindowTitle("New Project")

        self.addPage(self.project_files)
        self.addPage(self.equations)
        self.addPage(self.conditions)
        self.addPage(self.method)
        self.addPage(self.graph_files)
        self.addPage(self.review)

        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setWizardStyle(QWizard.WizardStyle(0))

        pixmap = QtGui.QPixmap(1, 1)
        pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(pixmap))

        cancel_button = self.button(QWizard.CancelButton)
        cancel_button.clicked.connect(self.show_main_window)

        finish_button = self.button(QWizard.FinishButton)
        finish_button.clicked.connect(self.start_filter)

        next_button = self.button(QWizard.NextButton)
        next_button.clicked.connect(self.current_page)

        self.setButtonText(QWizard.FinishButton, "Start")

    def current_page(self):
        if self.currentPage().objectName() == "review":
            self.review.fill()

    def closeEvent(self, event):
        self.main_window.show()

    def show_main_window(self):
        self.main_window.show()

    def start_filter(self):
        list_g6_in = []
        for file in self.graph_files.files_added:
            list_g6_in.extend(open(file, 'r').read().splitlines())

        expression = self.equations.equation.text()

        list_inv_bool_choices = self.conditions.dict_inv_bool_choices.items()

        self.filter_backend.set_inputs(list_g6_in, expression, list_inv_bool_choices)
        self.save_project()

        if self.method.method == 'filter':
            self.filter_backend.run_filter()
        elif self.method.method == 'counterexample':
            self.filter_backend.run_find_counterexample()

        # TODO: Use the percentage returned by filtering
        self.project_window.visualize.fill_combo(self.filter_backend.list_out)
        self.project_window.show()

    def save_project(self):
        project_dictionary = {
            "project_name": self.project_files.project_name_input.text(),
            "project_folder": self.project_files.project_location_input.text(),
            "equation": self.equations.equation.text(),
            "conditions": self.conditions.dict_inv_bool_choices,
            "method": self.method.method,
            "graphs": self.graph_files.files_added
        }
        project_json = json.dumps(project_dictionary)

        project_location = self.project_files.project_location_input.text().replace('\\', '/')

        filename = f"{project_location}/{self.project_files.project_name_input.text()}.json"

        with open(filename, "w") as file_json:
            file_json.write(project_json)
            file_json.close()
