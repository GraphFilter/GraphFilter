from PyQt5 import QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import *

from src.store.operations_and_invariants.invariants import UtilsToInvariants


class GraphInformationDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.model = QtGui.QStandardItemModel()

        self.table = QTableView()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Info")
        self.setObjectName("Info")

        self.setMinimumHeight(50)
        self.setMinimumWidth(500)

        self.setFeatures(QDockWidget.DockWidgetClosable |
                         QDockWidget.DockWidgetMovable |
                         QDockWidget.DockWidgetFloatable
                         )

        self.model.setHorizontalHeaderLabels(['Invariants', 'Results'])

        self.table.setWordWrap(False)
        self.table.setModel(self.model)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, self.width())
        self.setWidget(self.table)

    def update_table(self, invariants_selected):
        self.model.removeRows(0, self.model.rowCount())
        max_width_to_column = 0
        for key, value in invariants_selected.items():
            row = []
            invariant_name = QtGui.QStandardItem(str(key))
            invariant_name.setEditable(False)
            value_formated = UtilsToInvariants.print(value)
            invariant_value = QtGui.QStandardItem(value_formated)
            invariant_value.setEditable(False)

            max_width_to_column = max(UtilsToInvariants.max_line_of_string(value_formated), max_width_to_column)

            row.append(invariant_name)
            row.append(invariant_value)
            self.model.appendRow(row)
        self.table.resizeRowsToContents()
        if 5.1*max_width_to_column > self.table.columnWidth(1):
            self.table.resizeColumnToContents(1)
