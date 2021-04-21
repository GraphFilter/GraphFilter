from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore


class WizardWindow(QWizard):

    def __init__(self):
        super().__init__()

        self.width = 900
        self.height = 600

        self.window_title = "New Project"

        self.pixmap = QtGui.QPixmap(1, 1)

        self.cancel_button = self.button(QWizard.CancelButton)
        self.finish_button = self.button(QWizard.FinishButton)
        self.next_button = self.button(QWizard.NextButton)

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle(self.window_title)

        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setWizardStyle(QWizard.WizardStyle(0))

        self.pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(self.pixmap))

        self.setButtonText(QWizard.FinishButton, "Start")
