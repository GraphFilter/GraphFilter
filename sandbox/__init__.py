import logging.config
import os
import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLayout
import importlib


class CustomApplication(QApplication):
    def __init__(self):
        super(CustomApplication, self).__init__(sys.argv)
        self.execution_configs()

    def execution_configs(self):
        root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        os.chdir(root_directory)
        self.addLibraryPath(root_directory)
        config_file_path = os.path.abspath(os.path.join(root_directory, 'config.ini'))
        logging.config.fileConfig(config_file_path)


class Sandbox(CustomApplication):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.element = None
        self.source_path = ""
        self.windowed = True

    def add_element(self):
        if self.windowed:
            if isinstance(self.element, QLayout):
                self.window.setLayout(self.element)
            elif isinstance(self.element, QWidget):
                layout = QVBoxLayout()
                layout.addWidget(self.element)
                self.window.setLayout(layout)
        else:
            self.window = self.element

    def instantiate_element(self, *args):

        element_name = self.__class__.__name__.replace("Sandbox", "")

        imported_module = importlib.import_module(get_module_relative_path(self.source_path))
        imported_class = getattr(imported_module, element_name)

        self.element = imported_class(*args)

        return self.element

    def set_initial_size(self):
        screen_rect = QGuiApplication.primaryScreen().geometry()
        target_width = int(screen_rect.width() * 0.6)
        target_height = int(screen_rect.height() * 0.6)

        self.window.resize(target_width, target_height)

    def start(self):
        self.add_element()
        self.window.show()
        sys.exit(self.exec())


def get_module_relative_path(file_path: str):
    directories = file_path.split(os.path.sep)
    relative_directories = directories[directories.index("sandbox"):]

    return '.'.join(relative_directories).replace(".py", "").replace("sandbox_", "").replace("sandbox", "source")