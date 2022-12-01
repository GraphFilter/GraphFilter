from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class LoadingWindow(QDialog):
    filter_complete_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.progressBar = QProgressBar(self)
        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.setFixedSize(500, 100)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

    def increase_step(self, value):
        self.progressBar.setValue(value)

    def closeEvent(self, event):
        self.filter_complete_signal.emit(1)
        event.accept()

    def set_maximum(self, value):
        self.progressBar.setMaximum(value)
