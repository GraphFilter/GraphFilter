from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class EditingFeatures(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.setWindowTitle("Information")
