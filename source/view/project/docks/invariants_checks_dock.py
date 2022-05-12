from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class InvariantsCheckDock(QDockWidget):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.invariantsWidget = []

        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.update_display)

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
        conditions_layout.setAlignment(Qt.AlignTop)
        self.widget.setLayout(conditions_layout)

        for key in conditions.keys():
            checkbox = QCheckBox(f"{key}")
            checkbox.clicked.connect(event)
            conditions_layout.addWidget(checkbox)
            self.invariantsWidget.append(checkbox)

        layout_aux = QVBoxLayout()

        layout_search = QHBoxLayout()
        layout_search.addWidget(QLabel("Find: "))
        layout_search.addWidget(self.searchbar)

        widget_aux = QWidget()
        scroll_area = QScrollArea()
        widget_aux.setLayout(conditions_layout)
        scroll_area.setWidget(widget_aux)
        layout_aux.addLayout(layout_search)

        layout_aux.addWidget(scroll_area)
        self.widget.setLayout(layout_aux)

    def update_display(self, text):

        for widget in self.invariantsWidget:
            if text.lower() in widget.text().lower():
                widget.show()
            else:
                widget.hide()
