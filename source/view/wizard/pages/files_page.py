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
        self.list_files_input.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.add_file = QPushButton("Add files")
        self.remove_file = QPushButton("Remove files")
        self.update_file = QPushButton("Change file")
        self.remove_all_files = QPushButton("Remove all")
        self.download_button = QPushButton(" Download .g6 graph")

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.download_button.setIcon(Icon('download'))
        self.download_button.setFixedHeight(40)

        self.remove_file.setEnabled(False)
        self.update_file.setEnabled(False)
        self.remove_all_files.setEnabled(False)

    def set_up_layout(self):
        self.setTitle("Input Graphs")

        layout = QHBoxLayout()
        #layout.addLayout(self.form)
        layout.addWidget(self.list_files_input)

        buttons = QVBoxLayout()
        buttons.addWidget(self.add_file)
        buttons.addWidget(self.remove_file)
        buttons.addWidget(self.update_file)
        buttons.addWidget(self.remove_all_files)
        buttons.addStretch(5)
        buttons.addWidget(self.download_button)
        layout.addLayout(buttons)

        layout.setContentsMargins(25, 25, 25, 25)
        # layout.addStretch(10)
        # layout.addWidget(self.download_button, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
