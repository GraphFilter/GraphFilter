import os

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
        self.createTree()

    def createTree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))

        self.setWidget(self.tree)
