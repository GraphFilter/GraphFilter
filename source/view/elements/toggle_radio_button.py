from PyQt5 import QtGui
from PyQt5.QtWidgets import QRadioButton


class ToggleRadioButton(QRadioButton):
    def __init__(self, item):
        super().__init__()
        self.item = item

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setAutoExclusive(not self.isChecked())
        self.setChecked(not self.isChecked())
        self.setAutoExclusive(self.isChecked())

        self.clicked.emit()
