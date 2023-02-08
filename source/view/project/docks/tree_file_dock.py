from PyQt5.QtWidgets import *

from source.store.project_information_store import project_information_store


class TreeFileDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.tree = None
        self.model = None
        self.path = None
        self.setWindowTitle("Files")

        self.widget = QWidget()
        self.create_tree()

    def create_tree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(["*.g6", "*.txt", "*.json"])

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))

        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)

        self.setWidget(self.tree)
