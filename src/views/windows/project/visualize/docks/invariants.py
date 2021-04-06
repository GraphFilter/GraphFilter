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

        self.invariants_selected = {}

        self.dic_invariants = {
            **self.visualize.filter_backend.invariant_num.dic_name_calc,
            **self.visualize.filter_backend.invariant_bool.dic_name_calc
        }

        self.create_conditions()




    def create_conditions(self):
        # TODO: groupbox with scroll bar
        conditions_layout = QVBoxLayout()

        self.widget.setLayout(conditions_layout)

        # NOTE: this code generate multiples checkboxes
        for key in self.dic_invariants.keys():
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

        if check.text() not in self.invariants_selected:
            if g is not None:
                self.invariants_selected[check.text()] = self.dic_invariants[check.text()](g)
            else:
                self.invariants_selected[check.text()] = 'None'
        else:
            del self.invariants_selected[check.text()]
        print(self.invariants_selected)

        self.visualize.info.update_table(self.invariants_selected)

    def change_graph(self):
        pass
