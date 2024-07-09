from PyQt6 import QtCore, QtWidgets

from source.worker import ProgressLabels


class ProgressConfigurations:
    def __init__(self, indeterminate: bool = False, maximum_size: int = 100):
        self.indeterminate = indeterminate
        self.maximum_size = maximum_size


class ProgressWindow(QtWidgets.QProgressDialog):
    update_signal = QtCore.pyqtSignal(int, str)
    finish = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__(labelText=ProgressLabels.DEFAULT)
        self._set_content_attributes()
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.close()

    def _set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.setRange(0, 0)
        self.setFixedSize(500, 100)

    def update_progress(self, value: int, label: str = "", configurations=ProgressConfigurations()):
        if not configurations.indeterminate:
            self.setMinimum(0)
            self.setMaximum(configurations.maximum_size)
        self.setLabelText(label)
        self.setValue(value)
