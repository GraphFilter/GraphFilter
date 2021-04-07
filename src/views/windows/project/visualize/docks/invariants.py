from PyQt5.QtWidgets import *
import networkx as nx


class Invariants(QDockWidget):

    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Invariants")
        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        self.widget = QWidget()
        self.setWidget(self.widget)

        self.create_conditions()

    def create_conditions(self):
        # TODO: groupbox with scroll bar
        conditions_layout = QVBoxLayout()

        self.widget.setLayout(conditions_layout)

        # NOTE: this code generate multiples checkboxes
        for key in self.visualize.dic_invariants.keys():
            checkbox = QCheckBox(f"{key}")
            checkbox.clicked.connect(self.checked)
            conditions_layout.addWidget(checkbox)

        layout_aux = QVBoxLayout()
        widget_aux = QWidget()
        scroll_area = QScrollArea()
        widget_aux.setLayout(conditions_layout)
        scroll_area.setWidget(widget_aux)
        layout_aux.addWidget(scroll_area)
        self.widget.setLayout(layout_aux)

    def checked(self):
        check = QCheckBox().sender()
        if self.visualize.current_graph is not None:
            g = nx.from_graph6_bytes(self.visualize.current_graph.encode('utf-8'))
        else:
            g = None

        if check.text() not in self.visualize.invariants_selected:
            if g is not None:
                self.visualize.invariants_selected[check.text()] = self.visualize.dic_invariants[check.text()](g)
            else:
                self.visualize.invariants_selected[check.text()] = 'None'
        else:
            del self.visualize.invariants_selected[check.text()]
        print(self.visualize.invariants_selected)

        self.visualize.info.update_table()

    def update_graph_to_table(self):
        if self.visualize.current_graph is not None:
            g = nx.from_graph6_bytes(self.visualize.current_graph.encode('utf-8'))
        else:
            g = None

        for key in self.visualize.invariants_selected.keys():
            if g is not None:
                self.visualize.invariants_selected[key] = self.visualize.dic_invariants[key](g)
            else:
                self.visualize.invariants_selected[key] = 'None'
        self.visualize.info.update_table()
