from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from source.view.components.icon import Icon


class HelpButton(QPushButton):

    def __init__(self, help_text):
        super().__init__()

        self.help_text = help_text

        self.setToolTip(help_text)
        self.setIcon(Icon('help'))
        self.setIconSize(QSize(30, 30))
        self.setStyleSheet("background: transparent")
        self.setCursor(Qt.WhatsThisCursor)
