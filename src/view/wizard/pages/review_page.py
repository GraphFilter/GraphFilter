from PyQt5.QtWidgets import *
from src.domain.utils import clear_layout
from PyQt5 import QtCore
from src.view.resources.qicons import Icon
from src.view.resources.help_buttons_text import tip_review


class ReviewPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.project_name = QLabel()
        self.project_location = QLabel()
        self.conditions = {}
        self.graph_files = []
        self.method = QLabel()
        self.equation = QLabel("<b>Equation:</b>")

        self.help_button = QPushButton()

        self.conditions_and_graphs_layout = QHBoxLayout()

        self.conditions_layout = ReviewConditionsLayout(self.conditions)
        self.graph_files_layout = ReviewGraphFilesLayout(self.graph_files)

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setObjectName("review")

        self.help_button.setFixedHeight(80)
        self.help_button.setFixedWidth(80)
        self.help_button.setToolTip(tip_review)
        self.help_button.setIcon(Icon('help'))
        self.help_button.setStyleSheet("background: transparent")

    def set_up_layout(self):
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("<h3>Review</h3>"))
        title_layout.addWidget(self.help_button, alignment=QtCore.Qt.AlignRight)

        project_name_layout = QHBoxLayout()
        project_name_layout.setSpacing(0)
        project_name_layout.addWidget(self.project_name)

        project_location_layout = QHBoxLayout()
        project_location_layout.setSpacing(0)
        project_location_layout.addWidget(self.project_location)

        project_layout = QHBoxLayout()
        project_layout.addLayout(project_name_layout)
        project_layout.addLayout(project_location_layout)

        self.conditions_and_graphs_layout.addLayout(self.conditions_layout)
        self.conditions_and_graphs_layout.addLayout(self.graph_files_layout)

        layout = QVBoxLayout()
        layout.addLayout(title_layout)
        # layout.addWidget(QLabel("<h3>Review</h3>"))
        layout.addStretch(1)
        layout.addLayout(project_layout)
        layout.addStretch(1)
        layout.addWidget(self.equation)
        layout.addStretch(1)
        layout.addWidget(self.method)
        layout.addStretch(1)
        layout.addLayout(self.conditions_and_graphs_layout)
        layout.setContentsMargins(80, 10, 80, 50)

        self.setLayout(layout)

    def set_project_name(self, project_name):
        self.project_name.setText(f"<b>Project Name:</b> {project_name}")

    def set_project_location(self, project_location):
        self.project_location.setText(f"<b>Project Location:</b> {project_location}")

    def set_method(self, method):
        self.method.setText(f"<b>Method:</b> {'Filter Graphs' if method == 'filter' else 'Find Counter Example'}")

    def set_equation(self, equation):
        self.equation.setText(f"<b>Equation:</b>  {equation}")

    def set_conditions(self, conditions):
        self.conditions = conditions
        self.update_conditions_and_graphs_layout()

    def set_graph_files(self, graph_files):
        self.graph_files = graph_files
        self.update_conditions_and_graphs_layout()

    def update_conditions_and_graphs_layout(self):
        clear_layout(self.conditions_layout)
        clear_layout(self.graph_files_layout)
        clear_layout(self.conditions_and_graphs_layout)

        self.conditions_layout = ReviewConditionsLayout(self.conditions)
        self.graph_files_layout = ReviewGraphFilesLayout(self.graph_files)

        self.conditions_and_graphs_layout.addLayout(self.conditions_layout)
        self.conditions_and_graphs_layout.addStretch(2)
        self.conditions_and_graphs_layout.addLayout(self.graph_files_layout)


class ReviewConditionsLayout(QVBoxLayout):
    def __init__(self, conditions):
        super().__init__()
        self.conditions = conditions
        self.addWidget(QLabel("<b>Conditions</b>"))

        if len(self.conditions) <= 10:
            aux_layout = QVBoxLayout()
            for condition, value in self.conditions.items():
                aux_layout.addWidget(QLabel(f"{condition}: {value}"))
            aux_layout.addStretch(1)
            aux_widget = QWidget()
            aux_widget.setMinimumHeight(200)
            aux_widget.setLayout(aux_layout)
            self.addWidget(aux_widget)
        else:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFrameShape(QFrame.NoFrame)
            scroll_area.setMaximumHeight(200)
            scroll_area.setMinimumWidth(230)
            scroll_area.setMaximumWidth(230)

            vertical_layout_aux = QVBoxLayout()
            for condition, value in self.conditions.items():
                vertical_layout_aux.addWidget(QLabel(f"{condition}: {value}"))

            widget_aux = QWidget()
            widget_aux.setLayout(vertical_layout_aux)
            scroll_area.setWidget(widget_aux)
            self.addWidget(scroll_area)


class ReviewGraphFilesLayout(QVBoxLayout):
    def __init__(self, graph_files):
        super().__init__()
        self.graph_files = graph_files

        self.addWidget(QLabel("<b>Graph Files</b>"))
        if len(self.graph_files) <= 10:
            aux_layout = QVBoxLayout()
            for file in self.graph_files:
                aux_layout.addWidget(QLabel(file))
            aux_layout.addStretch(1)
            aux_widget = QWidget()
            aux_widget.setMinimumHeight(200)
            aux_widget.setLayout(aux_layout)
            self.addWidget(aux_widget)
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
            self.addWidget(scroll_area)
