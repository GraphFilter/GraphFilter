from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

from source.view.items.typography import H4


class CaptionContainer(QWidget):
    def __init__(self, title: str, content: str):
        super().__init__()

        self.title = title
        self.content = content

        self.set_content_attributes()

    def set_content_attributes(self):
        title = H4(self.title, QtCore.Qt.AlignLeft)
        content = QLabel(self.content)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(content)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
