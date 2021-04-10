from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Review(QWizardPage):

    def __init__(self, parent):
        super().__init__()

        self.setObjectName("review")

        self.parent = parent

        self.project_name = ""
        self.project_location = ""
        self.conditions = {}
        self.graph_files = []
        self.method = ""
        self.equation = ""

    def fill(self):
        self.project_name = self.parent.project_files.project_name_input.text()
        self.project_location = self.parent.project_files.project_location_input.text()
        self.conditions = self.parent.conditions.dict_inv_bool_choices
        self.graph_files = self.parent.graph_files.files_added
        self.method = self.parent.method.method
        self.equation = self.parent.equations.equation.text()

        project_name_layout = QVBoxLayout()
        project_name_layout.addWidget(QLabel("<b>Project Name:</b>"))
        project_name_layout.addWidget(QLabel(self.project_name))

        project_location_layout = QVBoxLayout()
        project_location_layout.setSpacing(0)
        project_location_layout.addWidget(QLabel("<b>Project Location:</b>"))
        project_location_layout.addWidget(QLabel(self.project_location))

        project_layout = QHBoxLayout()
        project_layout.addLayout(project_name_layout)
        project_layout.addLayout(project_location_layout)

        conditions_layout = QVBoxLayout()
        conditions_layout.addWidget(QLabel("<b>Conditions</b>"))
        self.fill_conditions(conditions_layout)

        graph_files_layout = QVBoxLayout()
        graph_files_layout.addWidget(QLabel("<b>Graph Files</b>"))
        self.fill_graph_files(graph_files_layout)

        center_layout = QHBoxLayout()
        center_layout.addLayout(conditions_layout)
        center_layout.addStretch(2)
        center_layout.addLayout(graph_files_layout)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h3>Review</h3>"))
        layout.addStretch(1)
        layout.addLayout(project_layout)
        layout.addStretch(1)
        layout.addWidget(QLabel(f"<b>Equation:</b>  {self.equation}"))
        layout.addStretch(1)
        layout.addWidget(QLabel(f"<b>Method:</b> {self.method}"))
        layout.addStretch(1)
        layout.addLayout(center_layout)
        layout.setContentsMargins(80, 30, 80, 50)

        self.setLayout(layout)

    def fill_graph_files(self, layout):
        if len(self.graph_files) <= 10:
            aux_layout = QVBoxLayout()
            for file in self.graph_files:
                aux_layout.addWidget(QLabel(file))
            aux_layout.addStretch(1)
            aux_widget = QWidget()
            aux_widget.setMinimumHeight(200)
            aux_widget.setLayout(aux_layout)
            layout.addWidget(aux_widget)
        else:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFrameShape(QFrame.NoFrame)
            scroll_area.setMaximumHeight(200)
            scroll_area.setMinimumWidth(600)

            vertical_layout_aux = QVBoxLayout()
            for file in self.graph_files:
                vertical_layout_aux.addWidget(QLabel(file))

            widget_aux = QWidget()
            widget_aux.setLayout(vertical_layout_aux)
            scroll_area.setWidget(widget_aux)
            layout.addWidget(scroll_area)

    def fill_conditions(self, layout):
        if len(self.conditions) <= 10:
            aux_layout = QVBoxLayout()
            for condition, value in self.conditions.items():
                aux_layout.addWidget(QLabel(f"{condition}: {value}"))
            aux_layout.addStretch(1)
            aux_widget = QWidget()
            aux_widget.setMinimumHeight(200)
            aux_widget.setLayout(aux_layout)
            layout.addWidget(aux_widget)
        else:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFrameShape(QFrame.NoFrame)
            scroll_area.setMaximumHeight(200)
            scroll_area.setMinimumWidth(230)

            vertical_layout_aux = QVBoxLayout()
            vertical_layout_aux.addWidget(QLabel("true"))
            for condition, value in self.conditions.items():
                vertical_layout_aux.addWidget(QLabel(f"{condition}: {value}"))

            widget_aux = QWidget()
            widget_aux.setLayout(vertical_layout_aux)
            scroll_area.setWidget(widget_aux)
            layout.addWidget(scroll_area)
