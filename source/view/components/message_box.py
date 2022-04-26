from PyQt5.QtWidgets import *
from source.view.components.icon import Icon


class MessageBox(QMessageBox):

    def __init__(self, text):
        super().__init__()

        self.setWindowTitle("Information")
        self.setIcon(QMessageBox.Information)
        self.setWindowIcon(Icon("info"))
        self.setText(text)

