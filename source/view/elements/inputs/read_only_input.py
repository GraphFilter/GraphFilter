from PyQt5.QtGui import QFont

from source.view.elements.inputs import Input


class ReadOnlyInput(Input):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Courier"))
        self.setReadOnly(True)
        self.setStyleSheet("ReadOnlyInput { padding: 5px; background: transparent; }")

    def validator(self):
        pass
