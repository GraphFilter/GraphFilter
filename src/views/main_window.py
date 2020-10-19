import sys
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Graph Filter")