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

        self.list_files_input = QListWidget()

        self.add_file = QPushButton("Add file")
        self.remove_file = QPushButton("Remove file")
        self.update_file = QPushButton("Change file")


        self.download_button = QPushButton(" get .g6 graph")

        self.form = QFormLayout()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.download_button.setIcon(Icon('download'))
        self.download_button.setFixedWidth(120)
        self.download_button.setFixedHeight(40)

        self.remove_file.setEnabled(False)
        self.update_file.setEnabled(False)

    def set_up_layout(self):
        self.setTitle("Graph files")

        buttons = QHBoxLayout()
        buttons.addWidget(self.add_file)
        buttons.addWidget(self.remove_file)
        buttons.addWidget(self.update_file)
        self.form.addRow(buttons)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addLayout(self.form)
        layout.addWidget(self.list_files_input)
        layout.addStretch(10)
        layout.addWidget(self.download_button, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
