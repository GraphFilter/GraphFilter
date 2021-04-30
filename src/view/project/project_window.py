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

        self.visualize_action = QAction("Visualize")
        self.invariants_check_action = QAction("Invariants Check")
        self.graph_info_action = QAction("Graph Info")
        self.dictionary_action = QAction("Dictionary")

        self.about_action = QAction("About...")

        self.restore_layout = QAction("Restore default layout")

        self.set_content_attributes()
        self.create_menu_bar()

    def set_content_attributes(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setMinimumSize(self.width, self.height)

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
        view_menu.addAction(self.invariants_check_action)
        view_menu.addAction(self.graph_info_action)
        view_menu.addAction(self.dictionary_action)

        window_menu = menu_bar.addMenu("Window")
        window_menu.addAction(self.restore_layout)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.about_action)
