from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *


class External(QThread):
    countChanged = pyqtSignal(int)


class LoadingWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.progressBar = QProgressBar(self)
        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.resize(500, 100)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

    def increase_step(self, value):
        self.progressBar.setValue(value)