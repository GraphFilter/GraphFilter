from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore


class WizardWindow(QWizard):

    close_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.width = 0
        self.height = 0
        self.setViewSize()

        self.window_title = "New Project"

        self.pixmap = QtGui.QPixmap(1, 1)

        self.cancel_button = self.button(QWizard.CancelButton)
        self.start_button = self.button(QWizard.FinishButton)
        self.next_button = self.button(QWizard.NextButton)
        self.help_button = self.button(QWizard.HelpButton)

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle(self.window_title)

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setOption(QWizard.HaveHelpButton, True)
        self.setOption(QWizard.HelpButtonOnRight, False)

        self.setWizardStyle(QWizard.ClassicStyle)

        self.pixmap.fill(QtCore.Qt.transparent)
        self.setWindowIcon(QtGui.QIcon(self.pixmap))

        self.setButtonText(QWizard.FinishButton, "Start")

    def closeEvent(self, event):
        self.close_signal.emit(1)
        event.accept()

    def setViewSize(self):
        screen = QApplication.desktop()
        rect = screen.screenGeometry()
        if rect.width() > 800 or rect.height() > 600:
            self.width = int(rect.width() / 1.5)
            self.height = int(rect.height() / 1.5)
            self.setFixedSize(self.width, self.height)
        elif rect.width() > 1920 or rect.height()>1080:
            self.width = 1280
            self.height = 720
        elif rect.width() == 800 or rect.height == 600:
            self.width = 700
            self.height = 500
            self.setFixedSize(self.width,self.height)