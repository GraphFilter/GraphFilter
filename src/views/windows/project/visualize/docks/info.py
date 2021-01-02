from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Info(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize

        self.setWindowTitle("Info")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Invariants', 'Results'])
        table = QTableView()
        table.setModel(model)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWidget(table)
