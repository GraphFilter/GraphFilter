from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from source.domain.utils import set_view_size

class WizardWindow(QWizard):

    close_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.width = 0
        self.height = 0
        set_view_size(self,1.7)

        self.window_title = "New Project"

        self.pixmap = QtGui.QPixmap(1, 1)

        self.cancel_button = self.button(QWizard.CancelButton)
        self.start_button = self.button(QWizard.FinishButton)
        self.next_button = self.button(QWizard.NextButton)
        self.help_button = self.button(QWizard.HelpButton)

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle(self.window_title)
        self.setFixedSize(self.width,self.height)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

        self.setOption(QWizard.HaveHelpButton, True)
        self.setOption(QWizard.HelpButtonOnRight, False)

        self.setWizardStyle(QWizard.ClassicStyle)

        self.pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(self.pixmap))

        self.setButtonText(QWizard.FinishButton, "Start")

    def closeEvent(self, event):
        self.close_signal.emit(1)
        event.accept()
