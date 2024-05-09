import logging

from PyQt5.QtCore import QStandardPaths
from PyQt5.QtGui import QValidator

from source.commons import validate_path
from source.view.elements.inputs import Input


class FolderInput(Input):
    def __init__(self):
        super().__init__()

        self.setText(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
        self.setReadOnly(True)

    def validator(self):
        try:
            super().validator()
        except NameError as e:
            self.invalidInput.emit("Folder input cannot be empty", AttributeError)
            return QValidator.Invalid
        if not validate_path(self.text()):
            self.invalidInput.emit(f"Invalid file path", ValueError)
            logging.error(f"Invalid file path")
            return QValidator.Invalid

        self.validInput.emit()
        return QValidator.Acceptable

    def setText(self, a0: str | None):
        super().setText(a0)
        self.validator()
