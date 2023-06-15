from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.data_title = r"<h1>Graph Filter</h1>"
        self.data_version = r"<h2>Version 3.0.0</h2>"
        self.data_text = r" <p align='justify'> The goal of this software is to help researchers of Graph Theory and " \
                         r"Graph Spectral Theory establish or refute conjectures. The program allows, in an intuitive " \
                         r"way, the visualization and manipulation of graphs, using operations and a diversity of " \
                         r"invariants. It also allows performing graph filtering according to properties given by " \
                         r"the user. </p>"
        self.data_page = \
            r'<h3> Page <\h3> <br> <a href={0}>{0}</a>'.format('sistemas.jf.ifsudestemg.edu.br/graphfilter')
        self.data_github = \
            r'<h3> GitHub <\h3>  <br> <a href={0}>{0}</a>'.format('github.com/GraphFilter/GraphFilter.py')

        self.data_authors = r"<b>Authors</b>" \
                                 r"<ul> <li>Átila A. Jones </b><i>(v1.0 forward)</i> -" \
                            r" atila.jones@ifsudestemg.edu.br </li>"\
                                 r"<li>Lavínia Beghini de Castro </b><i>(v2.0 forward)</i> </li>" \
                                 r"<li>Fernando S. Pimenta </b><i>(v2.0 forward)</i> </li>" \
                                 r"<li>Igor Rosa F. Pinto </b><i>(v2.0 forward)</i> </li>" \
                                 r"<li>Denilson P. O. Ribeiro </b><i>(v1.0)</i> </ul>"

        self.data_text2 = r"<p align='justify'> This program is the result of research projects at Instituto Federal " \
                          r"do Sudeste de Minas Gerais, Juiz de Fora - MG, Brazil. With financial support from the " \
                          "institution, as well as FAPEMIG and CNPq.</p>"

        self.logo_cnpq = QLabel()
        self.logo_fapemig = QLabel()
        self.logo_if = QLabel()

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
        about_text.setWordWrap(True)
        about_page = QLabel(self.data_page)
        about_github = QLabel(self.data_github)
        about_text2 = QLabel(self.data_text2)
        about_text2.setWordWrap(True)


        self.logo_cnpq.setPixmap(QPixmap("resources/logos/cnpq.png").scaled(190, 190, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.logo_fapemig.setPixmap(QPixmap("resources/logos/fapemig.png").scaled(160, 160, QtCore.Qt.KeepAspectRatio,
                                                                            QtCore.Qt.SmoothTransformation))
        self.logo_if.setPixmap(QPixmap("resources/logos/if_sudeste_mg.png").scaled(220, 220, QtCore.Qt.KeepAspectRatio,
                                                                            QtCore.Qt.SmoothTransformation))

        about_layout = QVBoxLayout()
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_version)
        about_layout.addWidget(about_text)
        about_layout.addWidget(about_authors)
        about_layout.addWidget(about_page)
        about_layout.addWidget(about_github)
        about_layout.addWidget(about_text2)

        logo_layout = QHBoxLayout()
        logo_layout.addWidget(self.logo_if)
        logo_layout.addWidget(self.logo_fapemig)
        logo_layout.addWidget(self.logo_cnpq)
        logo_layout.setAlignment(QtCore.Qt.AlignCenter)

        about_layout.addLayout(logo_layout)
        self.setLayout(about_layout)
