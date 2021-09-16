
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class LoadingWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel("loading...")

        layout = QHBoxLayout()

        # self.label.setGeometry(QRect(25, 25, 200, 200))
        # self.label.setMinimumSize(QSize(250, 250))
        # self.label.setMaximumSize(QSize(250, 250))

        self.movie = QMovie("loading.gif")
        self.label_animation.setMovie(self.movie)

        layout.addWidget(self.label_animation)
        self.setLayout(layout)

    def start_animation(self):
        self.movie.start()
        self.show()

    def stop_animation(self):
        self.movie.stop()
        self.close()


