import json

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from source.view.project.project_tool_bar import ProjectToolBar
from source.controller.filter_controller import FilterController

from PyQt5.QtWidgets import *

from source.store.project_information_store import project_information_store


class TreeFileDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.tree = QTreeView()
        self.model = None
        self.path = None
        self.setWindowTitle("Files")

        self.widget = QWidget()
        self.createTree()

    def createTree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)

        #self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.tree.customContextMenuRequested.connect(self.context_menu)

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))

        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)

        self.setWidget(self.tree)

    #def context_menu(self):
    #    menu = QMenu()
    #    load_file = menu.addAction("Load File on Graph Filter")
    #    load_file.triggered.connect(self.handle_double_click)
    #    cursor = QCursor()
    #    menu.exec(cursor.pos())

