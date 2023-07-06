from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from source.view.components.image import Icon
from PyQt5 import QtCore


class WelcomeContent(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel()
        self.version = QLabel()
        self.logo = QLabel()

        self.open_button = QPushButton()
        self.new_button = QPushButton()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.title.setText("<h1>Graph Filter</h1>")
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.version.setText("<h2>version 3.0</h2>")
        self.version.setAlignment(QtCore.Qt.AlignCenter)

        self.logo.setPixmap(QPixmap("resources/logos/graph_filter.png").scaled(150, 150, QtCore.Qt.KeepAspectRatio,
                                                                          QtCore.Qt.SmoothTransformation))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.open_button.setText("  Open")
        self.open_button.setIcon(Icon("folder"))
        self.open_button.setMinimumHeight(50)
        self.open_button.setMinimumWidth(100)

        self.new_button.setText("  New Project")
        self.new_button.setIcon(Icon("plus"))
        self.new_button.setMinimumHeight(50)
        self.new_button.setMinimumWidth(150)

    def set_up_layout(self):
        layout = QVBoxLayout(self)
        layout.addStretch(3)
        layout.addWidget(self.logo)
        layout.addStretch(2)
        layout.addWidget(self.title)
        layout.addWidget(self.version)
        layout.addStretch(3)
        layout.addWidget(self.open_button)
        layout.addStretch(1)
        layout.addWidget(self.new_button)
        layout.addStretch(3)
        layout.setAlignment(self.open_button, QtCore.Qt.AlignCenter)
        layout.setAlignment(self.new_button, QtCore.Qt.AlignCenter)
