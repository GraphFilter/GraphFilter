from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
from src.views.wizard import Wizard


class Central(QVBoxLayout):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        title = QLabel("<h1>Graph Filter</h1>")
        title.setAlignment(QtCore.Qt.AlignCenter)

        version = QLabel("<h2>version 1.0</h2>")
        version.setAlignment(QtCore.Qt.AlignCenter)

        logo = QLabel("")
        logo.setPixmap(QPixmap("views/resources/icons/hexagon.png").scaled(92, 92, QtCore.Qt.KeepAspectRatio))
        logo.setAlignment(QtCore.Qt.AlignCenter)

        # TODO: how to separate icons from titles in buttons
        open_button = QPushButton("  Open")
        open_button.setIcon(QIcon("views/resources/icons/folder.png"))
        open_button.setMinimumHeight(50)
        open_button.setMinimumWidth(100)
        open_button.clicked.connect(self.open_project)

        new_button = QPushButton("  New Project")
        new_button.setIcon(QIcon("views/resources/icons/plus.png"))
        new_button.setMinimumHeight(50)
        new_button.setMinimumWidth(150)
        new_button.clicked.connect(self.open_wizard)

        self.addStretch(3)
        self.addWidget(logo)
        self.addStretch(2)
        self.addWidget(title)
        self.addWidget(version)
        self.addStretch(3)
        self.addWidget(open_button)
        self.addStretch(1)
        self.addWidget(new_button)
        self.addStretch(3)
        self.setAlignment(open_button, QtCore.Qt.AlignCenter)
        self.setAlignment(new_button, QtCore.Qt.AlignCenter)

        self.wizard = Wizard(self.main_window)

    def open_wizard(self):
        self.main_window.close()
        self.wizard.open()

    def open_project(self):
        file_dialog = QFileDialog()
        file_dialog.getOpenFileName()
