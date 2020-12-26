from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title_bar = "Project Name - Visualize"
        self.icon = QtGui.QIcon("views/resources/icons/hexagono.png")

        self.width = 1200
        self.height = 900

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.create_menu_bar()
        self.init_window()

    def init_window(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setFixedSize(self.width, self.height)

    def create_menu_bar(self):

        # TODO: how to add separator to the menu bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        file_menu.addAction("New Project")
        file_menu.addAction("Open...")

        save = file_menu.addAction("Save")
        save.setShortcut("Ctrl+s")

        file_menu.addAction("Settings")

        file_menu.addAction("Exit")

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Cut")

        view_menu = menu_bar.addMenu("View")
        view_menu.addAction("Visualize")
        view_menu.addAction("Resize")
        view_menu.addAction("Zoom in")
        view_menu.addAction("Zoom out")
        view_menu.addAction("Zoom fit")
        view_menu.addAction("Print")
        export = view_menu.addMenu("Export")
        export.addAction("PDF")

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("Dictionary")
        help_menu.addAction("About...")

        self.layout.addWidget(menu_bar)