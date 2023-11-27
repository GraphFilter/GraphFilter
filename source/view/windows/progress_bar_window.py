from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from source.view.elements.progress_bar import ProgressBar


class ProgressBarWindow(QDialog):
    filter_complete_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.progress_bar = ProgressBar()
        self.set_content_attributes()
        self.set_up_layout()
        self.is_forced_to_close = False

    def set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.progress_bar.setGeometry(25, 25, 300, 40)
        self.setFixedSize(500, 100)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def closeEvent(self, event):
        if event.spontaneous():
            self.is_forced_to_close = True
        else:
            self.filter_complete_signal.emit(1)
            event.accept()
