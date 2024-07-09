from PyQt6 import QtCore
from PyQt6.QtWidgets import *

from deprecated.utils import set_view_size
from source.view.elements.buttons.generic_button import DefaultButton
from source.view.elements.icon import Icon
from source.view.items.logo import Logo
from source.view.items.subtitle import Subtitle
from source.view.items.title import Title


class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        self.icon = Icon("graph_filter_logo")

        self.width = 0
        self.height = 0

        self.content = WelcomeContent()

        set_view_size(self, 1.5)

        self.set_screen_position()

        self.set_window_attributes()

    def set_window_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.width = int(self.width / 1.7)
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint
                            | QtCore.Qt.WindowTitleHint
                            | QtCore.Qt.WindowCloseButtonHint
                            )

        self.setCentralWidget(self.content)

    def set_screen_position(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())


class WelcomeContent(QWidget):

    def __init__(self):
        super().__init__()

        self.logo = Logo("resources/logos/graph_filter.png")

        self.open_button = DefaultButton("Open", Icon("folder"))
        self.new_button = DefaultButton("New Project", Icon("plus"))

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

    def set_up_layout(self):
        layout = QVBoxLayout(self)
        layout.addStretch(3)
        layout.addWidget(self.logo)
        layout.addStretch(2)
        layout.addWidget(Title("Graph Filter"))
        layout.addWidget(Subtitle("v3.6.9"))
        layout.addStretch(3)
        layout.addWidget(self.open_button)
        layout.addStretch(1)
        layout.addWidget(self.new_button)
        layout.addStretch(3)
        layout.setAlignment(self.open_button, QtCore.Qt.AlignCenter)
        layout.setAlignment(self.new_button, QtCore.Qt.AlignCenter)
