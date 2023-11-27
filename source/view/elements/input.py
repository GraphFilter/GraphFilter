import typing

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit

from source.commons import calculate_string_difference


class Input(QLineEdit):
    textChanged = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.key_pressed = ""
        self.previous_text = ""

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        current_text, difference = self.get_difference()
        self.textChanged.emit(current_text, difference)

    def setText(self, a0: typing.Optional[str]):
        super().setText(a0)
        current_text, difference = self.get_difference()
        if difference != "":
            self.textChanged.emit(current_text, difference)

    def get_difference(self) -> tuple[str, str]:
        current_text = self.text()
        difference = calculate_string_difference(current_text, self.previous_text)
        self.previous_text = current_text

        return current_text, difference
