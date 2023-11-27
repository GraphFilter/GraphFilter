from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWizardPage, QTextEdit

from source.domain.utils import validate_file_name, validate_path
from source.view.components.form_template_layout import FormTemplateLayout
from source.view.components.verifiable_input import VerifiableInput
from source.view.elements.caption_container import CaptionContainer
from source.view.items.typography import H4
from source.view.utils.PairWidgets import PairWidgets

from source.view.components.file_input import FileInput


class Information(QWizardPage):
    def __init__(self):
        super().__init__()

        self.form = None
        self.input_name = VerifiableInput("Name", font_size=11)
        self.input_location = FileInput()
        self.description_input = QTextEdit()
        self.set_content_attributes()
        self.set_up_layout()
        self.connect_events()

    def set_content_attributes(self):
        self.input_name.layout().setContentsMargins(0, 0, 0, 0)
        self.input_location.layout().setContentsMargins(0, 0, 0, 0)
        self.description_input.setMinimumHeight(100)
        self.description_input.setMaximumHeight(200)
        self.description_input.setFont(QFont("Arial", 11))

        self.form = FormTemplateLayout(
            [
                PairWidgets(H4("Project Name"), self.input_name),
                PairWidgets(H4("Project location"), self.input_location),
                PairWidgets(CaptionContainer("Project description", "(Optional)"), self.description_input),
            ]
        )

    def set_up_layout(self):
        self.setTitle("Information")
        self.setLayout(self.form)

    def connect_events(self):
        self.input_name.input.textEdited.connect(lambda text: self.validate_input_name(text))
        self.input_location.input.input.textEdited.connect(self.emit_complete_signal)

    def validate_input_name(self, name):
        if not validate_file_name(name):
            error_message = "Invalid file name"
        else:
            error_message = None

        self.input_name.set_error_label(error_message)
        self.emit_complete_signal()

    def emit_complete_signal(self):
        self.completeChanged.emit()

    def isComplete(self):
        return validate_file_name(self.input_name.input.text()) and\
            validate_path(self.input_location.input.input.text())
