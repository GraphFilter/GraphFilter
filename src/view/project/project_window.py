from PyQt5.QtWidgets import *
from src.view.resources.qicons import Icon


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Project Name - Visualize"

        self.icon = Icon("hexagon")

        self.width = 1200
        self.height = 900

        self.new_action = QAction("New Project")
        self.open_action = QAction("Open...")
        self.save_action = QAction("Save")
        # self.settings_action = QAction("Settings")
        # self.print_action = QAction(Icon("print"), "Print")
        self.exit_action = QAction("Exit")

        self.visualize_action = QAction("visualize")
        self.restore_default_layout_action = QAction("Restore Default Layout")

        self.dictionary_action = QAction("dictionary")
        self.about_action = QAction("About...")

        self.set_content_attributes()
        self.create_menu_bar()

    def set_content_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setMinimumSize(self.width, self.height)

        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        # file_menu.addAction(self.settings_action)
        # file_menu.addSeparator()
        # file_menu.addAction(self.print_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        view_menu = menu_bar.addMenu("&View")
        view_menu.addAction(self.visualize_action)
        view_menu.addSeparator()
        view_menu.addAction(self.restore_default_layout_action)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.dictionary_action)
        help_menu.addSeparator()
        help_menu.addAction(self.about_action)
