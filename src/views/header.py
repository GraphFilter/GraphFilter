import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Header(QWidget):

    def __init__(self):
        super().__init__()
        self.title = QLabel("<h1>Graph Filter</h1>")
        self.version = QLabel("<h2>v1.0</h2>")
        self.image = QLabel("")
        self.pixmap = (QPixmap("views/resources/icons/GraphFilterIcon.png"))
        self.image.setPixmap(self.pixmap)

        self.ui_components()

    def ui_components(self):
        layout = QGridLayout(self)
        layout.addWidget(self.title, 0, 0)
        layout.addWidget(self.version, 0, 2)
        layout.addWidget(self.image, 0, 1)


