import configparser
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget, QApplication

from source.commons.objects.nameable_object import NameableObject
from source.view.elements.buttons.default_button import DefaultButton
from source.view.items.logo import SoftwareLogo
from source.view.items.typography import H1, H2
from source.view.utils.icons import Icons

config = configparser.ConfigParser()
config.read('config.ini')


class Welcome(QWidget):
    def __init__(self):
        super().__init__()

        self.logo = SoftwareLogo(120, 120)

        self.open_button = DefaultButton(NameableObject("Open"), Icons.FILE)
        self.blank_project = DefaultButton(NameableObject("Blank Project"), Icons.PLUS)
        self.new_filter_project = DefaultButton(NameableObject("New Filter Project"), Icons.PLUS)

        self.set_up_layout()
        self.set_content_attributes()
        self.resize_window()
        self.center_window()

    def set_content_attributes(self):
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.open_button.setStyleSheet(self.open_button.styleSheet() + "text-align: center;")
        self.blank_project.setStyleSheet(self.blank_project.styleSheet() + "text-align: center;")
        self.new_filter_project.setStyleSheet(self.new_filter_project.styleSheet() + "text-align: center;")

        margin = self.layout().getContentsMargins()[0] * 2

        self.open_button.setFixedWidth(self.open_button.sizeHint().width() + margin)
        self.blank_project.setFixedWidth(self.blank_project.sizeHint().width() + margin)
        self.new_filter_project.setFixedWidth(self.new_filter_project.sizeHint().width() + margin)

    def set_up_layout(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(self.logo)
        layout.addStretch(1)
        layout.addWidget(H1("Graph Filter"))
        layout.addWidget(H2(config['software']['version']))
        layout.addStretch(1)
        self.add_centered_widget(layout, self.open_button)
        self.add_centered_widget(layout, self.blank_project)
        self.add_centered_widget(layout, self.new_filter_project)
        layout.addStretch(1)

    @staticmethod
    def add_centered_widget(layout, widget):
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        container_layout.setContentsMargins(3, 3, 3, 3)
        container_layout.addWidget(widget, alignment=Qt.AlignCenter)
        layout.addWidget(container_widget, alignment=Qt.AlignCenter)

    def resize_window(self):
        screen_rect = QApplication.desktop().screenGeometry()
        new_width = int(screen_rect.width() * 0.3)
        new_height = int(screen_rect.height() * 0.6)
        self.setFixedSize(new_width, new_height)

    def center_window(self):
        frame_rect = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_rect.moveCenter(center_point)
        self.move(frame_rect.topLeft())
