from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from source.view.components.icon import Icon


class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        self.icon = Icon("hexagon")

        self.width = 0
        self.height = 0
        self.set_view_size(1.5)

        self.set_screen_position()

        self.set_window_attributes()

    def set_window_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint
                            | QtCore.Qt.WindowTitleHint
                            | QtCore.Qt.WindowCloseButtonHint
                            )

    def set_screen_position(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def set_view_size(self, p):
        screen = QApplication.desktop()
        rect = screen.screenGeometry()
        if rect.width() > 1920 or rect.height() > 1080:
            self.width = 720
            self.height = 720
        elif rect.width() > 800 or rect.height() > 600:
            self.width = int(rect.height() / p)
            self.height = int(rect.height() / p)
            self.setFixedSize(self.width, self.height)
        elif rect.width() <= 800 or rect.height() <= 600:
            self.width = 770
            self.height = 550
            self.setFixedSize(self.width, self.height)
