from PyQt5.QtWidgets import *


class ProjectFilesWizardPage(QWizardPage):

    def __init__(self):
        super().__init__()

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
        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Project location:"))
        file_line.addWidget(self.project_location_input)
        file_line.addWidget(self.project_location_button)

        form = QFormLayout()
        form.addRow(QLabel("Project Name:"), self.project_name_input)
        form.addRow(file_line)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.addLayout(form)
        layout.addStretch()

        self.setLayout(layout)

    def isComplete(self):
        return self.complete_project_name and self.complete_project_location
