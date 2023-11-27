from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QSizePolicy

from source.commons.objects.translation_object import TranslationObject
from source.view.components.verifiable_input import VerifiableInput
from source.view.elements.buttons.default_button import DefaultButton
from source.view.elements.file_dialog import FileDialog
from source.view.elements.inputs.folder_input import FolderInput
from source.view.utils.icons import Icons


class FolderPicker(QWidget):
    def __init__(self):
        """
        This component represents a custom widget for file input. It consists of a button with an icon
        for adding folders, and a text input field for specifying the file location.
        """
        super().__init__()
        self.button = DefaultButton(translation_object=TranslationObject(""), icon=Icons.ADD_FOLDER)
        self.input = VerifiableInput(FolderInput(), "Location", font_size=11)
        self._set_content_attributes()
        self._set_up_layout()
        self._connect_events()

    def _set_content_attributes(self):

        self.button.setFixedHeight(self.input.input.height())
        self.button.setStyleSheet(self.button.styleSheet() + "padding-right: 5px;")
        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input.layout().setContentsMargins(0, 0, 0, 0)

    def _set_up_layout(self):
        layout = QHBoxLayout()

        layout.addWidget(self.input, 1)
        layout.addWidget(self.button, 0)

        layout.setAlignment(self.button, Qt.AlignTop)
        layout.setAlignment(self.input, Qt.AlignTop)

        self.setLayout(layout)

    def get_input(self):
        return self.input.input

    def has_acceptable_input(self) -> bool:
        return self.input.has_acceptable_input()

    def _connect_events(self):
        self.button.clicked.connect(self._add_file_to_input)

    def _add_file_to_input(self):
        file_path = FileDialog().get_existing_directory()
        self.input.set_text(file_path)
