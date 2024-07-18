from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtWidgets import QWizard
from source.domain import Parameters
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
    close_signal = pyqtSignal()

    def __init__(self):
        super().__init__(None)

        self.title_bar = "New Project"

        self.cancel_button = self.button(QWizard.WizardButton.CancelButton)
        self.start_button = self.button(QWizard.WizardButton.FinishButton)
        self.next_button = self.button(QWizard.WizardButton.NextButton)
        self.help_button = self.button(QWizard.WizardButton.HelpButton)

        self.set_window_attributes()
        self.set_content()
        self.help_button.clicked.connect(self.display_help_button)

        self.parameters: Parameters = None

    def set_window_attributes(self):
        self.setWindowIcon(QIcon(SoftwareLogo().pixmap))
        self.setWindowTitle(self.title_bar)

        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint)

        self.setOption(QWizard.WizardOption.HaveHelpButton, True)
        self.setOption(QWizard.WizardOption.HelpButtonOnRight, False)

        self.setWizardStyle(QWizard.WizardStyle.ClassicStyle)
        self.setButtonText(QWizard.WizardButton.FinishButton, "Start")
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
        MessageBox(self.currentPage().help_message).exec()

    def addPage(self, page: WizardPage):
        super().addPage(page)
        page.set_properties()

    def setFixedSize(self, size: QSize = None) -> None:
        screen_rect = QGuiApplication.primaryScreen().geometry()
        target_width = int(screen_rect.width() * 0.6)
        target_height = int(screen_rect.height() * 0.6)
        super().setFixedSize(target_width, target_height)

    def closeEvent(self, event):
        self.close_signal.emit()
        event.accept()

    def done(self, result: int) -> None:
        self.parameters = Parameters(
            self.field("name"),
            self.field("method"),
            self.field("equation"),
            self.field("conditions"),
            self.field("description"),
            self.field("files"),
            self.field("location")
        )
        return super().done(result)

    def is_mac(self):
        return self.style().objectName().lower().startswith('mac')
