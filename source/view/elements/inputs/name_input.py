import logging

from PyQt5.QtGui import QValidator
import re

from source.view.elements.inputs import Input


class NameInput(Input):
    def __init__(self):
        super().__init__()

    def validator(self):
        file_name_regex = re.compile(r'^[\w\s]+$')
        try:
            super().validator()
        except NameError as e:
            self.invalidInput.emit("Name input cannot be empty", AttributeError)
            return QValidator.Invalid
        if not file_name_regex.match(self.text()):
            self.invalidInput.emit(f"Invalid file name", ValueError)
            logging.error(f"Invalid file name")
            return QValidator.Invalid

        self.validInput.emit()
        return QValidator.Acceptable

    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        self.validator()
