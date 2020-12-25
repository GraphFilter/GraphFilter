from PyQt5.QtWidgets import *
from src.views import project_files
from src.views import equations
from src.views import graph_files


class Wizard(QWizard):

    def __init__(self):
        super().__init__()

        self.width = 900
        self.height = 800

        self.setWindowTitle("New Project")
        self.addPage(project_files.ProjectFiles())
        self.addPage(equations.Equations())
        self.addPage(graph_files.GraphFiles())
        self.setFixedSize(self.width, self.height)
