from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWizard, QDesktopWidget
from PyQt5 import QtCore

from source.view.elements.message_box import MessageBox
from source.view.items.logo import SoftwareLogo
from source.view.pages import WizardPage
from source.view.pages.conditions import Conditions
from source.view.pages.equation import Equation
from source.view.pages.files import Files
from source.view.pages.information import Information
from source.view.pages.method import Method
from source.view.pages.review import Review


class WizardWindow(QWizard):
    close_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__(None)

        self.title_bar = "New Project"

        self.cancel_button = self.button(QWizard.CancelButton)
        self.start_button = self.button(QWizard.FinishButton)
        self.next_button = self.button(QWizard.NextButton)
        self.help_button = self.button(QWizard.HelpButton)

        self.set_window_attributes()
        self.set_content()
        self.help_button.clicked.connect(self.display_help_button)

    def set_window_attributes(self):
        self.setWindowIcon(QIcon(SoftwareLogo().pixmap))
        self.setWindowTitle(self.title_bar)

        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.setOption(QWizard.HaveHelpButton, True)
        self.setOption(QWizard.HelpButtonOnRight, False)

        self.setWizardStyle(QWizard.ClassicStyle)
        self.setButtonText(QWizard.FinishButton, "Start")
        self.setFixedSize()

    def set_content(self):
        self.addPage(Method())
        self.addPage(Information())
        self.addPage(Equation())
        self.addPage(Conditions())
        self.addPage(Files())
        self.addPage(Review())

        self.next_button.setShortcut("Return")

    def display_help_button(self):
        MessageBox(self.currentPage().help_message).exec_()

    def addPage(self, page: WizardPage):
        super().addPage(page)
        page.set_properties()

    def setFixedSize(self, a0: QtCore.QSize = None) -> None:
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry(desktop.primaryScreen())
        target_width = int(screen_rect.width() * 0.6)
        target_height = int(screen_rect.height() * 0.6)
        super().setFixedSize(target_width, target_height)

    def closeEvent(self, event):
        self.close_signal.emit()
        event.accept()

    def is_mac(self):
        return self.style().objectName().lower().startswith('mac')
