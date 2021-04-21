from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Info(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize

        self.setWindowTitle("Info")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Invariants', 'Results'])
        table = QTableView()
        table.setModel(self.model)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWidget(table)

    def update_table(self):
        self.model.removeRows(0, self.model.rowCount())
        for key, value in self.visualize.invariants_selected.items():
            row = []
            invariant_name = QtGui.QStandardItem(str(key))
            invariant_name.setEditable(False)

            invariant_value = QtGui.QStandardItem(str(value))
            invariant_value.setEditable(False)

            row.append(invariant_name)
            row.append(invariant_value)

            self.model.appendRow(row)
