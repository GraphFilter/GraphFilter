import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore


class Header(QWidget):

    def __init__(self):
        super().__init__()
        self.title = QLabel("<h1>Graph Filter</h1>")
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.version = QLabel("<h2>version 1.0</h2>")
        self.version.setAlignment(QtCore.Qt.AlignCenter)

        self.logo = QLabel("")
        self.logo.setPixmap(QPixmap("views/resources/icons/hexagono.png").scaled(64, 64, QtCore.Qt.KeepAspectRatio))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.open = QPushButton("Open")
        self.open.setIcon(QIcon(QPixmap("views/resources/icons/folder.png")))
        self.open.setFixedSize(200, 50)
        self.open.clicked.connect(self.test)

        self.new = QPushButton("New Project")
        self.new.setIcon(QIcon(QPixmap("views/resources/icons/mais.png")))
        self.new.setFixedSize(200, 50)
        self.open.clicked.connect(self.test)

        self.ui_components()

    def ui_components(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setSpacing(30)
        layout.addWidget(self.logo)
        layout.addWidget(self.title)
        layout.addWidget(self.version)
        layout.addWidget(self.open)
        layout.addWidget(self.new)


    def test(self):
        print("teste")