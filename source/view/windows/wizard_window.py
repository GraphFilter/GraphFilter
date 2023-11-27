from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from source.domain.utils import set_view_size
from source.view.pages.conditions import Conditions
from source.view.pages.equation import Equation
from source.view.pages.files import Files
from source.view.pages.information import Information
from source.view.pages.method import Method
from source.view.pages.review import Review


class WizardWindow(QWizard):
    def __init__(self):
        super().__init__()

        self.width = 1000
        self.height = 1000
        # set_view_size(self, 1.7)

        self.window_title = "New Project"

        self.pixmap = QtGui.QPixmap(1, 1)

        self.cancel_button = self.button(QWizard.CancelButton)
        self.start_button = self.button(QWizard.FinishButton)
        self.next_button = self.button(QWizard.NextButton)
        self.help_button = self.button(QWizard.HelpButton)

        self.set_content_attributes()
        self.add_pages()

    def set_content_attributes(self):
        self.setWindowTitle(self.window_title)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.setOption(QWizard.HaveHelpButton, True)
        self.setOption(QWizard.HelpButtonOnRight, False)

        self.setWizardStyle(QWizard.ModernStyle)

        self.pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(self.pixmap))

        self.setButtonText(QWizard.FinishButton, "Start")

    def add_pages(self):
        self.addPage(Method())
        self.addPage(Information())
        self.addPage(Equation())
        self.addPage(Conditions())
        self.addPage(Files())
        self.addPage(Review())
