from PyQt6.QtWidgets import QWidget


class PairWidgets:
    def __init__(self, key: QWidget, value: QWidget):
        self.key = key
        self.value = value
