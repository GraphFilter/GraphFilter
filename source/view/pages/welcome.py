import configparser

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QDesktopWidget

from source.domain.objects.nameable_object import NameableObject
from source.view.elements.buttons.default_button import DefaultButton
from source.view.items.logo import Logo
from source.view.items.typography import H1, H2
from source.view.utils.constants.icons import Icons


config = configparser.ConfigParser()
config.read('config.ini')


class Welcome(QWidget):
    def __init__(self):
        super().__init__()

        self.logo = Logo("resources/logos/graph_filter.png")

        self.open_button = DefaultButton(NameableObject("Open"), Icons.FILE)
        self.new_filter_project = DefaultButton(NameableObject("New Filter Project"), Icons.PLUS)
        self.new_blank_project = DefaultButton(NameableObject("New Blank Project"), Icons.PLUS)

        self.open_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.new_filter_project.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.new_blank_project.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

    def set_up_layout(self):
        layout = QVBoxLayout(self)
        layout.addStretch(3)
        layout.addWidget(self.logo)
        layout.addStretch(2)
        layout.addWidget(H1("Graph Filter"))
        layout.addWidget(H2(config['software']['version']))
        layout.addStretch(3)
        layout.addWidget(self.open_button)
        layout.addStretch(1)
        layout.addWidget(self.new_filter_project)
        layout.addStretch(3)
        layout.addStretch(1)
        layout.addWidget(self.new_blank_project)
        layout.addStretch(3)
