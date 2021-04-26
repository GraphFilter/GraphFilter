from PyQt5.QtWidgets import *


class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.progressBar = QProgressBar(self)

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setWindowTitle("Loading...")

        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(0)

        self.resize(500, 100)

    def increase_step(self, value):
        self.progressBar.setValue(self.progressBar.value()+value)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)
