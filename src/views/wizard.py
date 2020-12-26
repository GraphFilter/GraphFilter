from PyQt5.QtWidgets import *
from src.views import project_files
from src.views import equations
from src.views import graph_files
from PyQt5 import QtGui


class Wizard(QWizard):

    def __init__(self, main_window):
        super().__init__()

        self.width = 900
        self.height = 600

        self.main_window = main_window

        self.setWindowTitle("New Project")
        self.addPage(project_files.ProjectFiles())
        self.addPage(equations.Equations())
        self.addPage(graph_files.GraphFiles())
        self.setFixedSize(self.width, self.height)

        self.setWizardStyle(QWizard.WizardStyle(0))
        self.setWindowIcon(QtGui.QIcon("views/resources/icons/hexagono.png"))

        close = self.button(QWizard.CancelButton)
        close.clicked.connect(self.show_main_window)

        finish = self.button(QWizard.FinishButton)
        finish.clicked.connect(self.show_project_window)

    def show_project_window(self):
        pass

    def show_main_window(self):
        self.main_window.show()
