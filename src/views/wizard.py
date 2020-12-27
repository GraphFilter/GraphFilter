from PyQt5.QtWidgets import *
from src.views.project_files import ProjectFiles
from src.views.equations import Equations
from src.views.graph_files import GraphFiles
from src.views.project_window import ProjectWindow
from PyQt5 import QtGui, QtCore


class Wizard(QWizard):

    def __init__(self, main_window):
        super().__init__()

        # TODO: remove icon from window
        self.width = 900
        self.height = 600

        self.main_window = main_window
        self.project_window = ProjectWindow()

        self.setWindowTitle("New Project")
        self.addPage(ProjectFiles())
        self.addPage(Equations())
        self.addPage(GraphFiles())
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setWizardStyle(QWizard.WizardStyle(0))
        self.setWindowIcon(QtGui.QIcon("views/resources/icons/hexagon.png"))

        cancel = self.button(QWizard.CancelButton)
        cancel.clicked.connect(self.show_main_window)

        finish = self.button(QWizard.FinishButton)
        finish.clicked.connect(lambda: self.project_window.show())

    def show_main_window(self):
        self.main_window.show()
