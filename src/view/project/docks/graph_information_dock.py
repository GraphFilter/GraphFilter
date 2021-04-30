from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class GraphInformationDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.model = QtGui.QStandardItemModel()

        self.table = QTableView()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Info")
        self.setObjectName("Info")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

        self.model.setHorizontalHeaderLabels(['Invariants', 'Results'])

        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWidget(self.table)

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
