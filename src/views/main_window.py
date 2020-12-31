from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from src.views.central import Central


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        pixmap = QtGui.QPixmap(1, 1)
        pixmap.fill(QtCore.Qt.transparent)
        self.title_bar = "Graph Filter"
        self.icon = QtGui.QIcon(pixmap)

        self.width = 600
        self.height = 600

        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

        self.setLayout(Central(self))
        self.init_window()

    def init_window(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
