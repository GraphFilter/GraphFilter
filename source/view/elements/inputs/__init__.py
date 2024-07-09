from abc import ABC, ABCMeta, abstractmethod
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QValidator
from PyQt6.QtWidgets import QLineEdit


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
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Home:
            self.setCursorPosition(0)
        elif event.key() == Qt.Key.Key_End:
            self.setCursorPosition(len(self.text()))
        else:
            super().keyPressEvent(event)

    @abstractmethod
    def validator(self):
        if not self.text().strip():
            raise NameError("Empty field")

    def hasAcceptableInput(self) -> bool:
        return True if self.validator() is QValidator.State.Acceptable else False
