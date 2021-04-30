from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import networkx as nx


class InvariantsCheckDock(QDockWidget):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.invariants = []

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Invariants")
        self.setObjectName("Invariants")

        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.setWidget(self.widget)

    def create_conditions(self, conditions, event):
        conditions_layout = QVBoxLayout()

        self.widget.setLayout(conditions_layout)

        for key in conditions.keys():
            checkbox = QCheckBox(f"{key}")
            checkbox.clicked.connect(event)
            conditions_layout.addWidget(checkbox)
        layout_aux = QVBoxLayout()
        widget_aux = QWidget()
        scroll_area = QScrollArea()
        widget_aux.setLayout(conditions_layout)
        scroll_area.setWidget(widget_aux)
        layout_aux.addWidget(scroll_area)
        self.widget.setLayout(layout_aux)

    def update_graph_to_table(self):
        if self.visualize.current_graph is not None:
            g = nx.from_graph6_bytes(self.visualize.current_graph.encode('utf-8'))
        else:
            g = None

        for key in self.visualize.invariants_selected.keys():
            if g is not None:
                self.visualize.invariants_selected[key] = self.visualize.dic_invariants[key].calculate(g)
            else:
                self.visualize.invariants_selected[key] = 'None'
        self.visualize.info.update_table()
