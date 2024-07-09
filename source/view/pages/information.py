from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTextEdit, QHBoxLayout, QWizard

from source.view.components.folder_picker import FolderPicker
from source.view.components.form_template_layout import FormTemplateLayout
from source.view.components.verifiable_input import VerifiableInput
from source.view.elements.caption_container import CaptionContainer
from source.view.elements.inputs.name_input import NameInput
from source.view.items.typography import H4
from source.view.pages import WizardPage
from source.view.items.pair_widgets import PairWidgets


class Information(WizardPage):
    def __init__(self):
        super().__init__()

        self.input_name = VerifiableInput(NameInput(), "Name", font_size=11)
        self.location_picker = FolderPicker()
        self.description = self.Description()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setTitle("Information")
        self.setSubTitle(self.subtitle)

    def set_up_layout(self):
        self.input_name.layout().setContentsMargins(0, 0, 0, 0)
        self.location_picker.layout().setContentsMargins(0, 0, 0, 0)

        form = FormTemplateLayout(
            [
                PairWidgets(H4("Project Name"), self.input_name),
                PairWidgets(H4("Project location"), self.location_picker),
                self.description
            ]
        )
        self.setLayout(form)

    def set_properties(self) -> None:
        self.wizard().setDefaultProperty(
            self.description.input.__class__.__name__,
            "plainText",
            self.description.input.textChanged
        )

        self.registerField("name*", self.input_name.input)
        self.registerField("location*", self.location_picker.get_input())
        self.registerField("description", self.description.input)

    def isComplete(self) -> bool:
        return self.location_picker.has_acceptable_input() and self.input_name.has_acceptable_input()

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, False)

    def showEvent(self, a0):
        self.input_name.input.setFocus()

    def cleanupPage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, True)

    class Description(QHBoxLayout):
        def __init__(self):
            super().__init__()

            self.input = QTextEdit()
            self.title = CaptionContainer("Project description", "(Optional)")

            self.set_content_attributes()
            self.set_up_layout()

        def set_content_attributes(self):
            self.input.setMinimumHeight(100)
            self.input.setMaximumHeight(200)
            self.input.setFont(QFont("Arial", 11))

        def set_up_layout(self):
            self.title.layout().setContentsMargins(0, 0, 15, 0)
            self.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignTop)
            self.addWidget(self.input)

    subtitle = """Add some information to help you identify your project."""
