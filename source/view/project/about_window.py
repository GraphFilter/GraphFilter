from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.data_title = r"<h1>Graph Filter<\h1>"
        self.data_version = r"<h2>Version 3.0.0<\h2>"
        self.data_text = "The goal of this software is to help researchers of Graph Theory and Graph Spectral " \
                         "Theory establish or refute conjectures. The program allows, in an intuitive way, the" \
                         " visualization and manipulation of graphs, using operations and a diversity of invariants. " \
                         "It also allows performing graph filtering according to properties given by the user."
        self.data_page = \
            r'<h3> Page <\h3> <br> <a href={0}>{0}</a>'.format('sistemas.jf.ifsudestemg.edu.br/graphfilter')
        self.data_github = \
            r'<h3> GitHub <\h3>  <br> <a href={0}>{0}</a>'.format('github.com/GraphFilter/GraphFilter.py')

        self.data_authors = r"<h3>Authors<\h3> <br> " \
                                 r"Átila A. Jones <i>(v1.0 forward)</i>: atila.jones@ifsudestemg.edu.br <br>" \
                                 r"Lavínia Beghini de Castro <i>(v2.0 forward)</i> <br>" \
                                 r"Fernando S. Pimenta <i>(v2.0 forward)</i> <br>" \
                                 r"Igor Rosa F. Pinto <i>(v2.0 forward)</i> <br>" \
                                 r"Denilson P. O. Ribeiro  <i>(v1.0)</i>"

        self.data_text2 = "This program is the result of research projects carried out at the Instituto Federal do" \
                          "Sudeste de Minas Gerais, Juiz de Fora - MG, Brazil. With financial support from the " \
                          "institution, as well as FAPEMIG and CNPq."


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
        about_authors = QLabel(self.data_authors)
        about_text2 = QLabel(self.data_text2)
        about_text.setWordWrap(True)
        about_page = QLabel(self.data_page)
        about_github = QLabel(self.data_github)

        about_layout = QVBoxLayout()
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_text)
        about_layout.addWidget(about_authors)
        about_layout.addWidget(about_text2)
        about_layout.addWidget(about_page)
        about_layout.addWidget(about_github)
        about_layout.addWidget(about_version)

        self.setLayout(about_layout)
