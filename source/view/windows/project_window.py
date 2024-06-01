from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow


class ProjectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._set_content_attributes()

    def _set_content_attributes(self):
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint
                            | QtCore.Qt.WindowMinMaxButtonsHint)
