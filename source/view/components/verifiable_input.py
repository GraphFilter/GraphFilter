from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from source.view.elements.icon_label import IconLabel
from source.view.elements.inputs import Input
from source.view.utils.colors import Colors
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.icons import Icons


class VerifiableInput(QWidget):

    def __init__(self,
                 input: Input,
                 placeholder: str,
                 font_size: int = BUTTON_FONT_SIZE
                 ):
        """
        This widget provides a user interface element for input with verification capabilities.
        It includes a QLineEdit for user text input and an IconLabel for displaying validation icons.

        :param placeholder: The placeholder text to be displayed in the input field.
        :type placeholder: str
        :param font_size: Optional font size for the input field. Defaults to BUTTON_FONT_SIZE.
        :type font_size: int
        """
        super().__init__()
        self.validation = IconLabel()
        self.input = input
        self.placeholder = placeholder
        self.font_size = font_size
        self.key_pressed = ""

        self._set_content_attributes()
        self._set_up_layout()

    def _set_content_attributes(self):
        self.input.setPlaceholderText(self.placeholder)
        self.input.setMaximumHeight(self.font_size * 3)
        self.input.setStyleSheet("padding: 5px;")

        self.input.validInput.connect(self.set_valid_label)
        self.input.invalidInput.connect(self.set_invalid_label)

        self.validation.set_font(QFont("Arial"))

    def _set_up_layout(self):
        layout = QVBoxLayout()

        layout.addWidget(self.input)
        layout.addWidget(self.validation, alignment=Qt.AlignTop)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def set_text(self, text: str):
        self.input.setText(text)

    def has_acceptable_input(self) -> bool:
        return self.input.hasAcceptableInput()

    def set_valid_label(self):
        self.validation.set_content_attributes(Icons.SUCCESS, "Valid Input", Colors.GREEN_TEXT())

    def set_invalid_label(self, message: str, error: Exception):
        if error == ValueError:
            self.validation.set_content_attributes(Icons.ERROR, message, Colors.RED_TEXT())
        elif error == NameError:
            self.validation.set_content_attributes(
                Icons.INFO,
                message if message else "Empty field",
                Colors.BLUE_TEXT()
            )
        else:
            self.validation.set_content_attributes(Icons.WARNING, message, Colors.YELLOW_TEXT())

    def add_custom_text(self, text: str):
        cursor = self.input.cursorPosition()
        modified_text = f"{self.input.text()[:cursor]}{text}{self.input.text()[cursor:]}"
        self.input.setText(modified_text)
        self.input.setCursorPosition(cursor + len(text) - 1 if "(" in text else cursor + len(text))

        self.input.setFocus()
