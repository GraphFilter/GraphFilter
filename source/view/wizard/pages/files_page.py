from PyQt5.QtWidgets import *
from source.store import help_button_text
from source.view.components.icon import Icon
from PyQt5 import QtCore


class FilesPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False
        self.incomplete_message = "Invalid graph file"
        self.alert_text = help_button_text.files

        self.files_input = QLineEdit()

        self.open_file = QPushButton("...")
        self.add_file = QPushButton("+")

        self.download_button = QPushButton(" get .g6 graph")

        self.form = QFormLayout()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.download_button.setIcon(Icon('download'))
        self.download_button.setFixedWidth(120)
        self.download_button.setFixedHeight(40)

        self.add_file.setEnabled(False)

    def set_up_layout(self):
        self.setTitle("Files")

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .g6 file:"))
        file_line.addWidget(self.files_input)
        file_line.addWidget(self.open_file)
        file_line.addWidget(self.add_file)

        self.form.addRow(file_line)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addLayout(self.form)
        layout.addStretch(10)
        layout.addWidget(self.download_button, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
