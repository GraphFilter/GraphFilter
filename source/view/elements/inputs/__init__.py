from abc import ABC, ABCMeta, abstractmethod
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QValidator
from PyQt5.QtWidgets import QLineEdit


class InputMixin:
    def __call__(self):
        return self


class InputMeta(type(QLineEdit), ABCMeta, type(InputMixin)):
    pass


class Input(QLineEdit, ABC, InputMixin, metaclass=InputMeta):
    validInput = pyqtSignal()
    invalidInput = pyqtSignal(str, object)

    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.ClickFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Home:
            self.setCursorPosition(0)
        elif event.key() == Qt.Key_End:
            self.setCursorPosition(len(self.text()))
        else:
            super().keyPressEvent(event)

    @abstractmethod
    def validator(self):
        if not self.text().strip():
            raise NameError("Empty field")

    def hasAcceptableInput(self) -> bool:
        return True if self.validator() is QValidator.Acceptable else False
