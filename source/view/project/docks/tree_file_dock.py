from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from source.store.project_information_store import project_information_store


class TreeFileDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.tree = QTreeView()
        self.model = None
        self.path = None
        self.setWindowTitle("Files")

        self.menu = QMenu()
        self.load_file = QAction("Load File")
        self.delete_file = QAction("Delete")
        #self.delete_empty_folder = QAction("Delete empty folder")
        self.widget = QWidget()
        self.create_tree()
        self.populate_context_menu()

    def create_tree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(["*.g6", "*.txt", "*.json"])

        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.tree.customContextMenuRequested.connect(self.context_menu)

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))

        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)

        self.setWidget(self.tree)


    def populate_context_menu(self):
        self.menu.addAction(self.load_file)
        self.menu.addAction(self.delete_file)