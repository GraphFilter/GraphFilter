from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class ProgressWindow(QWidget):
    update_signal = QtCore.pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        self.progress_bar = QProgressBar()
        self._set_content_attributes()
        self.set_up_layout()

    def _set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setValue(0)
        self.setFixedSize(500, 100)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def increase_step(self, value: int):
        self.progress_bar.setValue(value)
        QApplication.processEvents()
