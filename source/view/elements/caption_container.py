from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

from source.view.items.typography import H4


class CaptionContainer(QWidget):
    def __init__(self, title: str, content):
        super().__init__()

        self.title = H4(title, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.content = QLabel(content) if content.__class__.__name__ == 'str' else content

        self.set_content_attributes()

    def set_content_attributes(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.content)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def update_content(self, text: str):
        self.content.setText(text)