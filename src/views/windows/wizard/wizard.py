from PyQt5.QtWidgets import *
from src.views.windows.wizard.pages.project_files import ProjectFiles
from src.views.windows.wizard.pages.equations import Equations
from src.views.windows.wizard.pages.graph_files import GraphFiles
from src.views.windows.project.project_window import ProjectWindow
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

        pixmap = QtGui.QPixmap(1,1)
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
        # NOTE: I believe that this point can do the filtering
        self.project_window.visualize.fill_combo(GraphFiles.files_added[0])  # filtering here
        self.project_window.show()


