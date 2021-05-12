from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class InvariantsCheckDock(QDockWidget):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.invariants = []

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Invariants")
        self.setObjectName("Invariants")

        self.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable
        )

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
