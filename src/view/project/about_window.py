from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.data_title = r"<h1>Graph Filter<\h1>"
        self.data_version = r"<h2>Version 2.0.0<\h2>"
        self.data_text = "The welcome goal of this software is to give assistance to Graph Theory and Spectral Graph " \
                         "Theory researchers to establish or refute conjectures quickly and simply, providing for " \
                         "visualization a filtered list of graphs according to the properties given by the user."
        self.data_page = r'<h3> Page: <\h3> \n <a href={0}>{0}</a>'.format('sistemas.jf.ifsudestemg.edu.br/graphfilter')
        self.data_github = r'<h3> GitHub: <\h3>  \n <a href={0}>{0}</a>'.format('github.com/GraphFilter/GraphFilter.py')

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setWindowTitle("About")

        self.setMinimumWidth(700)
        self.setMinimumHeight(200)

        self.setWindowFlag(QtCore.Qt.Tool)

        # self.about.setWindowFlags(QtCore.Qt.WindowFlags(
        # QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # )

    def set_up_layout(self):
        about_title = QLabel(self.data_title)
        about_version = QLabel(self.data_version)
        about_text = QLabel(self.data_text)
        about_text.setWordWrap(True)
        about_page = QLabel(self.data_page)
        about_github = QLabel(self.data_github)

        about_layout = QVBoxLayout()
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_text)
        about_layout.addWidget(about_page)
        about_layout.addWidget(about_github)
        about_layout.addWidget(about_version)

        self.setLayout(about_layout)
