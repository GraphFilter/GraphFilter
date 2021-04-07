from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from src.views.windows.project.visualize.visualize import Visualize
from src.views.windows.project.dictionary.dictionary import Dictionary
import src.views.windows.project.about.about as about_data


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # TODO: get project name from wizard
        self.title_bar = "Project Name - Visualize"

        self.icon = QtGui.QIcon("views/resources/icons/hexagon.png")

        self.width = 1200
        self.height = 900

        self.about = QDialog()
        self.about.setMinimumWidth(700)
        self.about.setMinimumHeight(200)
        # self.about.setWindowFlags(QtCore.Qt.WindowFlags(
        # QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # )

        self._create_actions()
        self.create_menu_bar()
        self.connect_actions()

        self.init_window()

        self.visualize = Visualize(self)

    def init_window(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setMinimumSize(self.width, self.height)

    def _create_actions(self):
        self.new_action = QAction("New Project")
        self.open_action = QAction("Open...")
        self.save_action = QAction("Save")
        self.settings_action = QAction("Settings")
        self.print_action = QAction(QtGui.QIcon("views/resources/icons/print.png"), "Print")
        self.exit_action = QAction("Exit")

        self.copy_action = QAction("Copy")
        self.paste_action = QAction("Paste")
        self.cut_action = QAction("Cut")

        self.visualize_action = QAction("Visualize")
        self.resize_action = QAction("Resize")
        self.zoom_in_action = QAction(QtGui.QIcon("views/resources/icons/zoom_in.png"), "Zoom in")
        self.zoom_out_action = QAction(QtGui.QIcon("views/resources/icons/zoom_out.png"), "Zoom out")
        self.zoom_fit_action = QAction(QtGui.QIcon("views/resources/icons/zoom.png"), "Zoom fit")
        self.restore_default_layout_action = QAction("Restore Default Layout")

        self.dictionary_action = QAction("Dictionary")
        self.about_action = QAction("About...")

    def create_menu_bar(self):
        # TODO: remove icons from menus
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.settings_action)
        file_menu.addSeparator()
        file_menu.addAction(self.print_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        edit_menu.addAction(self.cut_action)

        view_menu = menu_bar.addMenu("&View")
        view_menu.addAction(self.visualize_action)
        view_menu.addSeparator()
        view_menu.addAction(self.resize_action)
        view_menu.addAction(self.zoom_in_action)
        view_menu.addAction(self.zoom_out_action)
        view_menu.addAction(self.zoom_fit_action)
        view_menu.addSeparator()
        view_menu.addAction(self.restore_default_layout_action)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.dictionary_action)
        help_menu.addSeparator()
        help_menu.addAction(self.about_action)

    def connect_actions(self):
        # NOTE: actions to be uncomment when the triggered functions are implemented

        # self.new_action.triggered.connect()
        # self.open_action.triggered.connect()
        # self.save_action.triggered.connect()
        # self.settings_action.triggered.connect()
        self.print_action.triggered.connect(self.on_print)
        # self.exit_action.triggered.connect()
        self.exit_action.triggered.connect(self.on_exit)

        # self.copy_action.triggered.connect()
        # self.paste_action.triggered.connect()
        # self.cut_action.triggered.connect()

        self.visualize_action.triggered.connect(self.on_visualize)
        # self.resize_action.triggered.connect()
        # self.zoom_in_action.triggered.connect()
        # self.zoom_out_action.triggered.connect()
        # self.zoom_fit_action.triggered.connect()
        self.restore_default_layout_action.triggered.connect(self.on_restore)

        self.dictionary_action.triggered.connect(self.on_dictionary)
        self.about_action.triggered.connect(self.on_about)

# menu bar actions
    def on_exit(self):
        self.close()

    def on_print(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            pass

    def on_visualize(self):
        self.setCentralWidget(None)
        self.visualize.remove_docks()
        self.visualize.create_docks()
        self.visualize.create_tool_bar()

    def on_dictionary(self):
        self.visualize.remove_docks()
        self.removeToolBar(self.visualize.tool_bar)
        self.setCentralWidget(Dictionary(self))
        self.visualize.tool_bar = None

    def on_about(self):
        self.about.setWindowTitle("About")

        about_title = QLabel(about_data.title)
        about_version = QLabel(about_data.version)
        about_text = QLabel(about_data.text)
        about_text.setWordWrap(True)
        about_page = QLabel(about_data.page)
        about_github = QLabel(about_data.github)

        about_layout = QVBoxLayout()
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_text)
        about_layout.addWidget(about_page)
        about_layout.addWidget(about_github)
        about_layout.addWidget(about_version)

        self.about.setLayout(about_layout)

        self.about.setWindowFlag(QtCore.Qt.Tool)

        self.about.open()

    def on_restore(self):
        self.visualize.remove_docks()
        self.visualize.create_docks()
