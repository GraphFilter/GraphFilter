import sys
from PyQt5.QtWidgets import *


class Footer(QWidget):

    def __init__(self):
        super().__init__()
        self.name = QLabel("I'm a footer")

        self.ui_components()

    def ui_components(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.name)