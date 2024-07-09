from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow


class ProjectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._set_content_attributes()

    def _set_content_attributes(self):
        self.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint
                            | QtCore.Qt.WindowType.WindowMinMaxButtonsHint)
