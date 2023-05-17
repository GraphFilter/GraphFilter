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

        self.export_png_action = QAction("Image (.png)")
        self.export_pdf_action = QAction("Image (.pdf)")
        self.export_tikz_action = QAction("LaTeX (.tikz)")
        self.export_g6_action = QAction("graph6 list (.txt)")
        self.export_sheet_action = QAction("Sheet (.xlsx): graph6 and invariants")

        self.widget = QWidget()
        self.create_tree()
        self.populate_context_menu()

    def create_tree(self):
        self.path = project_information_store.get_file_directory()

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

        prev_menu_export = self.menu.addMenu('Export all graphs to')
        prev_menu_export.addAction(self.export_png_action)
        prev_menu_export.addAction(self.export_tikz_action)
        prev_menu_export.addAction(self.export_g6_action)
        prev_menu_export.addAction(self.export_pdf_action)
        prev_menu_export.addAction(self.export_sheet_action)