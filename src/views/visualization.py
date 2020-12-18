import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect


class Visualization(QWidget):
    def __init__(self):
        super().__init__()
        self.name = QLabel("Visualization")

        self.ui_components()

    def ui_components(self):
        button = QPushButton("It does something.", self)
        button.setGeometry(QRect(300, 100, 111, 50))
        button.clicked.connect(self.something)
        button.setObjectName("teste")
        # button.setStyleSheet("""
        # QPushButton {
        #     border-radius: 10px;
        #     background-color: teal;
        #     }
        # QPushButton:hover{
        #     cursor:pointer;
        # }
        # """)

    def something(self):
        print("It did something")
