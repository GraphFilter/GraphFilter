from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # TODO: get project name from wizard
        # TODO: create classes for each widget
        self.title_bar = "Project Name - Visualize"
        self.icon = QtGui.QIcon("views/resources/icons/hexagon.png")

        self.width = 1200
        self.height = 900

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self._create_actions()
        self.connect_actions()
        self.create_menu_bar()
        self.create_tool_bar()
        self._create_dock()
        self.init_window()

    def init_window(self):
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title_bar)
        self.setMinimumSize(self.width, self.height)

    def _create_actions(self):
        self.new_action = QAction("New Project")
        self.open_action = QAction("Open...")
        self.save_action = QAction("Save")
        self.settings_action = QAction("Settings")
        self.exit_action = QAction("Exit")

        self.copy_action = QAction("Copy")
        self.paste_action = QAction("Paste")
        self.cut_action = QAction("Cut")

        self.visualize_action = QAction("Visualize")
        self.resize_action = QAction("Resize")
        self.zoom_in_action = QAction(QtGui.QIcon("views/resources/icons/zoom_in.png"), "Zoom in")
        self.zoom_out_action = QAction(QtGui.QIcon("views/resources/icons/zoom_out.png"), "Zoom out")
        self.zoom_fit_action = QAction(QtGui.QIcon("views/resources/icons/zoom.png"), "Zoom fit")
        self.print_action = QAction(QtGui.QIcon("views/resources/icons/print.png"), "Print")

        self.dictionary_action = QAction("Dictionary")
        self.about_action = QAction("About...")

    def connect_actions(self):
        #     self.new_action.triggered.connect()
        #     self.open_action.triggered.connect()
        #     self.save_action.triggered.connect()
        #     self.settings_action.triggered.connect()
        #     self.exit_action.triggered.connect()
        self.exit_action.triggered.connect(self.on_exit)

        #     self.copy_action.triggered.connect()
        #     self.paste_action.triggered.connect()
        #     self.cut_action.triggered.connect()

        #     self.visualize_action.triggered.connect()
        #     self.resize_action.triggered.connect()
        #     self.zoom_in_action.triggered.connect()
        #     self.zoom_out_action.triggered.connect()
        #     self.zoom_fit_action.triggered.connect()
        self.print_action.triggered.connect(self.on_print)

        #     self.dictionary_action.triggered.connect()
        #     self.about_action.triggered.connect()

    def on_exit(self):
        self.close()

    def on_print(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            pass

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
        view_menu.addAction(self.print_action)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.dictionary_action)
        help_menu.addSeparator()
        help_menu.addAction(self.about_action)

        self.layout.addWidget(menu_bar)

    def create_tool_bar(self):
        tool_bar = self.addToolBar("Tool Bar")
        tool_bar.layout().setSpacing(30)
        tool_bar.layout().setContentsMargins(15, 10, 20, 20)
        tool_bar.setMovable(False)
        tool_bar.addWidget(QLabel("Graphs"))
        tool_bar.addWidget(QComboBox())
        tool_bar.addSeparator()
        tool_bar.addAction(self.zoom_in_action)
        tool_bar.addAction(self.zoom_out_action)
        tool_bar.addAction(self.zoom_fit_action)
        tool_bar.addAction(self.print_action)

    def _create_dock(self):
        self.graph = QDockWidget("Graph", self)
        self.graph.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.graph.setWidget(QTextEdit())

        self.info = QDockWidget("Info", self)
        self.info.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        # TODO: learn how to add items to TableView
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Invariants', 'Results'])
        self.table = QTableView()
        self.table.setModel(model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.info.setWidget(self.table)

        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.graph)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.info)
