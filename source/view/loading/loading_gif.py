import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QHBoxLayout, QApplication


class LoadingGif(QDialog):

    def __init__(self):
        super().__init__()
        self.movie = QMovie(f"resources/gifs/loading.gif")
        self.central_widget = QWidget()
        self.label = QLabel()
        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setWindowTitle("Loading...")
        self.setFixedSize(250, 250)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowContextHelpButtonHint | Qt.WindowCloseButtonHint)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

    def set_up_layout(self):
        self.label = QLabel(self.central_widget)
        self.label.setGeometry(QRect(25, 25, 200, 200))
        self.label.setMovie(self.movie)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def start_animation(self):
        self.movie.start()

    def closeEvent(self, event):
        if event.spontaneous():
            QApplication.closeAllWindows()
        else:
            pass
