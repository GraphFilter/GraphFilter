from PyQt5.QtWidgets import *
from source.store import help_button_text


class ProjectInformationWizardPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.incomplete_message = "Fill all required information"
        self.alert_text = help_button_text.project

        self.project_name_input = QLineEdit()
        self.project_location_input = QLineEdit()
        self.project_location_button = QPushButton("...")

        self.complete_project_name = False
        self.complete_project_location = True

        self.set_content_attributes()
        self.define_layout()

    def set_content_attributes(self):
        self.setObjectName("project_files")

    def define_layout(self):

        self.setTitle("Basic Information")
        file_line = QHBoxLayout()
        file_line.addWidget(self.project_location_input)
        file_line.addWidget(self.project_location_button)

        form = QFormLayout()
        form.addRow(QLabel("Project Name"), self.project_name_input)

        form.addRow(QLabel("Project location"), file_line)

        self.setLayout(form)

    def isComplete(self):
        return self.complete_project_name and self.complete_project_location
