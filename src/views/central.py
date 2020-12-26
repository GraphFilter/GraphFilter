from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
from src.views import wizard


class Central(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        title = QLabel("<h1>Graph Filter</h1>")
        title.setAlignment(QtCore.Qt.AlignCenter)

        version = QLabel("<h2>version 1.0</h2>")
        version.setAlignment(QtCore.Qt.AlignCenter)

        logo = QLabel("")
        logo.setPixmap(QPixmap("views/resources/icons/hexagono.png").scaled(64, 64, QtCore.Qt.KeepAspectRatio))
        logo.setAlignment(QtCore.Qt.AlignCenter)

        open_button = QPushButton("  Open")
        open_button.setIcon(QIcon("views/resources/icons/folder.png"))
        open_button.setMinimumHeight(50)
        open_button.setMinimumWidth(100)
        open_button.clicked.connect(self.open_project)

        new_button = QPushButton("  New Project")
        new_button.setIcon(QIcon("views/resources/icons/mais.png"))
        new_button.setMinimumHeight(50)
        new_button.setMinimumWidth(150)
        new_button.clicked.connect(self.open_wizard)

        layout = QVBoxLayout(self)
        layout.addStretch(3)
        layout.addWidget(logo)
        layout.addStretch(2)
        layout.addWidget(title)
        layout.addWidget(version)
        layout.addStretch(3)
        layout.addWidget(open_button)
        layout.addStretch(1)
        layout.addWidget(new_button)
        layout.addStretch(3)
        layout.setAlignment(open_button, QtCore.Qt.AlignCenter)
        layout.setAlignment(new_button, QtCore.Qt.AlignCenter)

        self.wizard = wizard.Wizard(self.main_window)

    def open_wizard(self):
        self.main_window.close()
        self.wizard.open()

    def open_project(self):
        file_dialog = QFileDialog()
        file_dialog.getOpenFileName(self, 'OpenFile')
