from PyQt5 import QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import *

from source.store.operations_and_invariants.invariants import UtilsToInvariants


class GraphInformationDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.model = QtGui.QStandardItemModel()

        self.table = QTableView()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Info")
        self.setObjectName("Info")

        self.setFeatures(QDockWidget.DockWidgetClosable |
                         QDockWidget.DockWidgetMovable |
                         QDockWidget.DockWidgetFloatable
                         )

        self.model.setHorizontalHeaderLabels(['Invariants', 'Results'])
        self.table.setModel(self.model)

        self.table.setWordWrap(False)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.table.setColumnWidth(1, 400)
        self.setWidget(self.table)

    def update_table(self, invariants_selected):
        self.model.removeRows(0, self.model.rowCount())
        column_max_width = 0
        for key, value in invariants_selected.items():
            row = []
            invariant_name = QtGui.QStandardItem(str(key))
            invariant_name.setEditable(False)

            value_formatted = UtilsToInvariants.print(value)
            invariant_value = QtGui.QStandardItem(value_formatted)
            invariant_value.setEditable(False)

            current_column_max_width = 0
            current_column_max_width = max(UtilsToInvariants.max_line_of_string(value_formatted), current_column_max_width)
            if current_column_max_width > column_max_width:
                column_max_width = current_column_max_width

            row.append(invariant_name)
            row.append(invariant_value)
            self.model.appendRow(row)
            self.table.resizeColumnToContents(1)

        if 5.1 * column_max_width < self.table.columnWidth(1):
            self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            self.table.setColumnWidth(0, 200)
        elif 5.1 * column_max_width > self.table.columnWidth(1):
            self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
            self.table.setColumnWidth(0, 200)
