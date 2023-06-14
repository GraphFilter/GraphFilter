from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from source.view.components.image import Icon
from source.domain.utils import set_view_size

class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        self.icon = Icon("graph_filter_logo")

        self.width = 0
        self.height = 0
        set_view_size(self, 1.5)

        self.set_screen_position()

        self.set_window_attributes()

    def set_window_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.width = int(self.width/1.7)
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
