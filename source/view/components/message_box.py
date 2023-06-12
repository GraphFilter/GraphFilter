from PyQt5.QtWidgets import *
from source.view.components.icon import Icon


class MessageBox(QMessageBox):

    def __init__(self, text, icon=QMessageBox.Information, window_title='Information'):
        super().__init__()

        self.setWindowTitle(window_title)
        self.setIcon(icon)
        self.setWindowIcon(Icon("info"))
        self.setText(text)
