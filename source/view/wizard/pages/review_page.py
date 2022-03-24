from PyQt5.QtWidgets import *

from source.domain.utils import clear_layout
from source.store import help_button_text


class ReviewPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.incomplete_message = "Fill all required information"
        self.alert_text = help_button_text.review

        self.project_name = QLabel()
        self.project_location = QLabel()
        self.conditions = {}
        self.graph_files = []
        self.method = QLabel()
        self.equation = QLabel('none')

        self.conditions_and_graphs_layout = QHBoxLayout()

        self.graph_files_layout = QListWidget()

        self.set_up_layout()

    def set_up_layout(self):
        self.setTitle("Review")

        self.project_layout = QGridLayout()
        self.project_layout.setVerticalSpacing(20)

        self.project_layout.addWidget(QLabel(
            "Review the information below and click 'Start' to create your new project. Use the 'Previous' button to "
            "make changes."), 0, 0)

        self.project_layout.addWidget(QLabel("<b>Project Name:</b>"), 1, 0)
        self.project_layout.addWidget(self.project_name, 1, 1)

        self.project_layout.addWidget(QLabel("<b>Project location:</b>"), 2, 0)
        self.project_layout.addWidget(self.project_location, 2, 1)

        self.project_layout.addWidget(QLabel("<b>Method Selected:</b>"), 3, 0)
        self.project_layout.addWidget(self.method, 3, 1)

        self.project_layout.addWidget(QLabel("<b>Equation:</b>"), 4, 0)
        self.project_layout.addWidget(self.equation, 4, 1)

        self.project_layout.addWidget(QLabel("<b>Conditions:</b>"), 5, 0)
        self.conditions_layout = QVBoxLayout()

        self.project_layout.addWidget(QLabel("<b>Graph files:</b>"), 6, 0)
        self.graph_files_layout.setSelectionMode(QListView.NoSelection)

        self.setLayout(self.project_layout)

    def set_project_name(self, project_name):
        self.project_name.setText(project_name)

    def set_project_location(self, project_location):
        self.project_location.setText(project_location)

    def set_method(self, method):
        self.method.setText(f"{'Filter Graphs' if method == 'filter' else 'Find Counter Example'}")

    def set_equation(self, equation):
        self.equation.setText(equation)

    def set_conditions(self, conditions):
        self.conditions = conditions
        self.update_conditions_view()

    def set_graph_files(self, graph_files):
        self.graph_files = graph_files
        self.update_files_view()

    def update_conditions_view(self):
        clear_layout(self.conditions_layout)
        widget_aux = QWidget()
        true_conditions = ''
        false_conditions = ''
        for condition, value in self.conditions.items():
            if value == 'true':
                true_conditions = true_conditions + f", {condition}"
            else:
                false_conditions = false_conditions + f", {condition}"
        true_widget_text = QLabel()
        true_widget_text.setWordWrap(True)
        false_widget_text = QLabel()
        false_widget_text.setWordWrap(True)

        if true_conditions == '' and false_conditions == '':
            self.conditions_layout.addWidget(QLabel("no bollean condition selected"))
        elif true_conditions == '':
            false_widget_text.setText(f"<b>graph not is</b>: {false_conditions[2:]}")
            self.conditions_layout.addWidget(false_widget_text)
        elif false_conditions == '':
            true_widget_text.setText(f"<b>graph is</b>: {true_conditions[2:]}")
            self.conditions_layout.addWidget(true_widget_text)
        else:
            true_widget_text.setText(f"<b>graph is</b>: {true_conditions[2:]}")
            false_widget_text.setText(f"<b>graph not is</b>: {false_conditions[2:]}")
            self.conditions_layout.addWidget(true_widget_text)
            self.conditions_layout.addWidget(false_widget_text)
        widget_aux.setLayout(self.conditions_layout)
        self.project_layout.addWidget(widget_aux, 5, 1)
        self.setLayout(self.project_layout)

    def update_files_view(self):
        self.graph_files_layout.clear()
        for file in self.graph_files:
            self.graph_files_layout.addItem(file)
        self.project_layout.addWidget(self.graph_files_layout, 6, 1)
        self.setLayout(self.project_layout)