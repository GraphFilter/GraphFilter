from PyQt5.QtWidgets import *

from source.domain.utils import clear_layout
from source.store import help_button_text
from PyQt5 import QtCore


class ReviewPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.incomplete_message = "Fill all required information"
        self.alert_text = help_button_text.review

        self.project_name = QLabel()
        self.project_name.setWordWrap(True)
        self.project_location = QLabel()
        self.project_location.setWordWrap(True)
        self.project_description = QLabel('<i>none</i>')
        self.project_description.setWordWrap(True)
        self.conditions = {}
        self.graph_files = []
        self.method = QLabel()
        self.equation = QLabel('<i>none</i>')

        self.scroll_area = QScrollArea()
        self.project_layout = QFormLayout()
        self.project_layout.setVerticalSpacing(20)
        self.graph_files_layout = QListWidget()
        self.conditions_layout = QVBoxLayout()

        self.set_up_layout()

    def set_up_layout(self):
        self.setTitle("Review")
        self.setSubTitle("Review the information below and click 'Start' to create your new project. \n"
                         "Use the 'Previous' button to ake changes.")

        #TODO: scrool bar still not working
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setLayout(self.project_layout)

        self.project_layout.addRow("<b>Project Name:</b>", self.project_name)
        self.project_layout.addRow("<b>Project location:</b>", self.project_location)
        self.project_layout.addRow("<b>Project description:</b>", self.project_description)
        self.project_layout.addRow("<b>Method Selected:</b>", self.method)
        self.project_layout.addRow("<b>(In)equations:</b>", self.equation)
        self.project_layout.addRow("<b>Conditions:</b>", self.conditions_layout)
        self.project_layout.addRow("<b>Graph files:</b>", self.graph_files_layout)
        self.graph_files_layout.setSelectionMode(QAbstractItemView.NoSelection)

        self.setLayout(self.project_layout)

    def set_project_name(self, project_name):
        self.project_name.setText(project_name)

    def set_project_location(self, project_location):
        self.project_location.setText(project_location)

    def set_project_description(self, project_description):
        self.project_description.setText(project_description)

    def set_method(self, method):
        self.method.setText(f"{'Filter Graphs' if method == 'filter' else 'Find Counter Example'}")

    def set_equation(self, equation):
        self.equation.setWordWrap(True)
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
        self.setLayout(self.project_layout)

    def update_files_view(self):
        self.graph_files_layout.clear()
        for file in self.graph_files:
            self.graph_files_layout.addItem(file)
        self.setLayout(self.project_layout)
