from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import *


from source.store.project_information_store import project_information_store
class TreeFileDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Files")
        self.createTree()


    def createTree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
