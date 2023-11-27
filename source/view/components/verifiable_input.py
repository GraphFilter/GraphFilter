from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout

from source.view.elements.iconizable_label import IconizableLabel
from source.view.elements.input import Input
from source.view.utils import is_dark_theme
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.constants.colors import Colors
from source.view.utils.constants.icons import Icons


class VerifiableInput(QWidget):
    def __init__(self, placeholder: str, font_size: int = BUTTON_FONT_SIZE):
        super().__init__()
        self.input = Input()
        self.validation = IconizableLabel()
        self.placeholder = placeholder
        self.font_size = font_size
        self.key_pressed = ""

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.input.setPlaceholderText(self.placeholder)
        self.input.setMaximumHeight(self.font_size * 3)
        self.input.setFont(QtGui.QFont("Arial", self.font_size))
        self.input.setStyleSheet("padding: 5px;")

        self.validation.set_font(QFont("Arial"))

    def set_up_layout(self):
        layout = QVBoxLayout()

        layout.addWidget(self.input)
        layout.addWidget(self.validation, alignment=Qt.AlignTop)
        layout.setSpacing(0)
        self.setLayout(layout)

    def set_success_label(self, message: str = "Valid input"):
        self.validation.set_content_attributes(Icons.SUCCESS, message,
                                               Colors.LIGHT_GREEN if is_dark_theme() else Colors.DARK_GREEN)

    def set_warning_label(self, message: str):
        self.validation.set_content_attributes(Icons.WARNING, message,
                                               Colors.LIGHT_YELLOW if is_dark_theme() else Colors.DARK_YELLOW)

    def set_error_label(self, message: str):
        self.validation.set_content_attributes(Icons.ERROR, message,
                                               Colors.LIGHT_RED if is_dark_theme() else Colors.DARK_RED)

    def add_custom_text(self, text: str):
        cursor = self.input.cursorPosition()
        modified_text = f"{self.input.text()[:cursor]}{text}{self.input.text()[cursor:]}"
        self.input.setText(modified_text)
        self.input.setCursorPosition(cursor + len(text) - 1 if "(" in text else cursor + len(text))

        self.input.setFocus()


class MathVerifiableInput(VerifiableInput):
    def __init__(self, placeholder: str):
        super().__init__(placeholder)

    def set_content_attributes(self):
        super().set_content_attributes()
        self.input.setFont(QtGui.QFont("Cambria Math", self.font_size))
