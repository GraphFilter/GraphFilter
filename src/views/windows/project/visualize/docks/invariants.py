from PyQt5.QtWidgets import *


class Invariants(QDockWidget):
    def __init__(self, visualize):
        super().__init__()

        self.visualize = visualize
        self.setWindowTitle("Invariants")
        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        self.widget = QWidget()
        self.setWidget(self.widget)

        self.setMaximumWidth(300)

        self.invariants = []

        self.create_conditions()

    def create_conditions(self):
        # TODO: groupbox with scroll bar
        conditions_layout = QVBoxLayout()

        self.widget.setLayout(conditions_layout)

        # NOTE: this code generate multiples checkboxes
        for i in range(1, 80):
            checkbox = QCheckBox(f"Checkbox {i}")
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

        if check.text() not in self.invariants:
            self.invariants.append(check.text())
        else:
            self.invariants.remove(check.text())
        print(self.invariants)
