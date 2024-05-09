from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from source.view.utils.colors import Colors
from source.view.utils.icons import Icons


class MessageBoxDescription:
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text


class MessageBox(QMessageBox):

    def __init__(self,
                 description: MessageBoxDescription,
                 icon: int = QMessageBox.Information,
                 window_title: str = 'Information'):
        super().__init__()
        self.setTextFormat(Qt.RichText)

        self.setWindowTitle(window_title)
        self.setWindowIcon(Icons.INFO(color=Colors.TEXT()))
        self.setIcon(icon)
        self.setText(description.title)
        self.setInformativeText(description.text)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setDefaultButton(QMessageBox.Ok)

        self.resize_text(description.text)

    def resize_text(self, text: str):
        children_label = self.findChildren(QLabel)
        for label in children_label:
            if label.text() == text:
                label.setStyleSheet("min-width: 400px;")
