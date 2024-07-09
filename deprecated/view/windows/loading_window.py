from PyQt6 import QtCore
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QDialog, QWidget, QLabel, QHBoxLayout, QApplication


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
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def set_up_layout(self):
        self.label = QLabel(self.central_widget)
        self.label.setGeometry(QRect(25, 25, 100, 100))
        self.label.setMovie(self.movie)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        self.adjustSize()
        self.setLayout(layout)

    def start_animation(self):
        self.movie.start()

    def closeEvent(self, event):
        if event.spontaneous():
            QApplication.closeAllWindows()
        else:
            pass
