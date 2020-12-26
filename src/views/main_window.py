from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from src.views import central


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        self.icon = QtGui.QIcon("views/resources/icons/hexagono.png")

        self.width = 600
        self.height = 600

        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

        self.setObjectName("main_window")
        self.setCentralWidget(central.Central(self))
        self.init_window()

    def init_window(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)
