from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
# from source.view.elements.icon import Icon


class MessageBox(QMessageBox):

    def __init__(self, text, icon: int = QMessageBox.Information, window_title: str = 'Information'):
        super().__init__()

        self.setWindowTitle(window_title)
        self.setIcon(icon)
        # self.setWindowIcon(Icon("info"))
        self.setText(text)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
