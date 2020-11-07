import sys
from PyQt5.QtWidgets import *
from src.views.header import Header
from src.views.tab import Tab
from src.views.footer import Footer
from PyQt5 import QtGui


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Graph Filter"

        self.width = 600
        self.height = 800

        self.ui_components()

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("views/resources/icons/GraphFilterIcon.png"))
        self.setWindowTitle(self.title)
        self.resize(self.height, self.width)

    def ui_components(self):
        layout = QVBoxLayout(self)
        layout.addWidget(Header())
        layout.addWidget(Tab())
        layout.addWidget(Footer())
