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

        self.setFixedHeight(23)
        self.setMinimumWidth(23)

        self.setFeatures(QDockWidget.DockWidgetClosable)

        self.model.setHorizontalHeaderLabels(['Invariants', 'Results'])

        self.table.setWordWrap(False)
        self.table.setModel(self.model)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidget(self.table)

    def update_table(self, invariants_selected):
        self.model.removeRows(0, self.model.rowCount())
        if len(invariants_selected) > 0:
            self.setMaximumSize(QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX))
        else:
            self.setFixedHeight(23)
        for key, value in invariants_selected.items():
            row = []
            invariant_name = QtGui.QStandardItem(str(key))
            invariant_name.setEditable(False)
            invariant_value = QtGui.QStandardItem(UtilsToInvariants.print(value))
            invariant_value.setEditable(False)

            row.append(invariant_name)
            row.append(invariant_value)

            self.model.appendRow(row)
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()