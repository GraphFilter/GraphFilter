from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel


class H1(QLabel):
    def __init__(self, text: str, alignment: int = QtCore.Qt.AlignCenter):
        super().__init__()
        self.setText(f"<h1>{text}</h1>")
        self.setAlignment(alignment)


class H2(QLabel):
    def __init__(self, text: str, alignment: int = QtCore.Qt.AlignCenter):
        super().__init__()
        self.setText(f"<h2>{text}</h2>")
        self.setAlignment(alignment)


class H3(QLabel):
    def __init__(self, text: str, alignment: int = QtCore.Qt.AlignCenter):
        super().__init__()
        self.setText(f"<h3>{text}</h3>")
        self.setAlignment(alignment)


class H4(QLabel):
    def __init__(self, text: str, alignment: int = QtCore.Qt.AlignCenter):
        super().__init__()
        self.setText(f"<h4>{text}</h4>")
        self.setAlignment(alignment)


class Code(QLabel):
    def __init__(self, text: str, alignment: int = QtCore.Qt.AlignLeft):
        super().__init__()
        self.setText(f"<code>{text}</code>")
        self.setAlignment(alignment)
