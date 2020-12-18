from src.views.header import Header
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore


def test():
    print("teste")


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title_bar = "Graph Filter"

        self.width = 600
        self.height = 600

        self.setObjectName("main_window")

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
        self.open.clicked.connect(test)

        self.new = QPushButton("New Project")
        self.new.setIcon(QIcon(QPixmap("views/resources/icons/mais.png")))
        self.new.setFixedSize(200, 50)
        self.new.clicked.connect(test)

        # stylesheet = ""
        #
        # with open("views/resources/stylesheet/design.qss", "r") as f:
        #     stylesheet = f.read()
        # self.setStyleSheet(stylesheet)

        self.ui_components()

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("views/resources/icons/hexagono.png"))
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)

    def ui_components(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setSpacing(30)
        layout.addWidget(self.logo)
        layout.addWidget(self.title)
        layout.addWidget(self.version)
        layout.addWidget(self.open)
        layout.addWidget(self.new)
