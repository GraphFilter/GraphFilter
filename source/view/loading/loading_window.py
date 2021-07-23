from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class External(QThread):
    countChanged = pyqtSignal(int)


class LoadingWindow(QDialog):
    filter_complete_signal = pyqtSignal(int)

    def __init__(self, maximum):
        super().__init__()
        self.progressBar = QProgressBar(self)
        self.set_content_attributes(maximum)
        self.set_up_layout()

    def set_content_attributes(self, maximum):
        self.setWindowTitle("Loading...")
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.setFixedSize(500, 100)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)
        self.progressBar.setMaximum(maximum)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

    def increase_step(self):
        self.progressBar.setValue(self.progressBar.value()+1)

    def closeEvent(self, event):
        self.filter_complete_signal.emit(1)
        event.accept()
