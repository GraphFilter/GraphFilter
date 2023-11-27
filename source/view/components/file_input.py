from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QSizePolicy

from source.domain.objects.nameable_object import NameableObject
from source.domain.utils import validate_path
from source.view.components.verifiable_input import VerifiableInput
from source.view.elements.buttons.default_button import DefaultButton
from source.view.elements.file_dialog import FileDialog
from source.view.utils.constants.icons import Icons


class FileInput(QWidget):
    def __init__(self):
        super().__init__()
        self.button = DefaultButton(nameable_object=NameableObject(""), icon=Icons.ADD_FOLDER, font_size=30)
        self.input = VerifiableInput("Location", font_size=11)
        self.set_up_layout()
        self.connect_events()

    def set_up_layout(self):
        layout = QHBoxLayout()

        layout.addWidget(self.input, 1)
        layout.addWidget(self.button, 0)

        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input.layout().setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(self.button, Qt.AlignTop)
        self.button.setFixedHeight(self.input.input.sizeHint().height())
        self.button.setStyleSheet(self.button.styleSheet() + "padding: 10px;")

        self.setLayout(layout)

    def connect_events(self):
        self.button.clicked.connect(self.add_file_to_input)
        self.input.input.textEdited.connect(lambda text: self.validate_input(text))

    def add_file_to_input(self):
        file_name = FileDialog().get_existing_directory()
        self.input.input.setText(file_name)
        self.validate_input(file_name)

    def validate_input(self, path):
        if not validate_path(path):
            error_message = "Invalid path"
        else:
            error_message = None

        self.input.set_error_label(error_message)
