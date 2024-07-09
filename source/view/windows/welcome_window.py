from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QWidget

from source.view.elements.file_dialog import FileDialog
from source.view.items.logo import SoftwareLogo
from source.view.pages.welcome import Welcome


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title_bar = "Graph Filter"
        content = Welcome()

        self.open_button = content.open_button
        self.new_project = content.new_filter_project
        self.blank_project = content.blank_project

        self.file_dialog = FileDialog()

        self.set_window_attributes()
        self.set_content(content)
        self.resize_window()
        self.center_window()

    def set_window_attributes(self):
        self.setWindowIcon(QIcon(SoftwareLogo().pixmap))
        self.setWindowTitle(self.title_bar)
        self.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint
                            | QtCore.Qt.WindowType.WindowTitleHint
                            | QtCore.Qt.WindowType.WindowCloseButtonHint
                            )

    def set_content(self, content: QWidget):
        self.setCentralWidget(content)

    def resize_window(self):
        screen_rect = QGuiApplication.primaryScreen().geometry()
        new_width = int(screen_rect.width() * 0.3)
        new_height = int(screen_rect.height() * 0.6)
        self.setFixedSize(new_width, new_height)

    def center_window(self):
        screen_rect = QGuiApplication.primaryScreen().geometry()
        window_rect = self.frameGeometry()
        window_rect.moveCenter(screen_rect.center())
        self.move(window_rect.topLeft())

    def _connect_buttons(self):
        self.open_button.clicked.connect(self.open_file_selector)

    def open_file_selector(self):
        self.file_dialog.get_open_file_names()
