from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from source.view.resources.components.icon import Icon


class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        self.icon = Icon("hexagon")

        self.width = 600
        self.height = 600

        self.set_screen_position()

        self.set_window_attributes()

    def set_window_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint
                            | QtCore.Qt.WindowTitleHint
                            | QtCore.Qt.WindowCloseButtonHint
                            | QtCore.Qt.WindowStaysOnTopHint)

    def set_screen_position(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())
