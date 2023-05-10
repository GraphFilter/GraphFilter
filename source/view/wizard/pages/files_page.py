from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from source.store import help_button_text
from source.view.components.icon import Icon


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
        self.download_button_hog = QPushButton("House of Graphs")
        self.download_button_mckay = QPushButton("By Brendan McKay")
        self.label_download = QLabel("Download graphs \n in g6 code", )

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.download_button_hog.setIcon(Icon('download'))
        self.download_button_hog.setFixedHeight(40)
        self.download_button_mckay.setIcon(Icon('download'))
        self.download_button_mckay.setFixedHeight(40)

        self.label_download.setFont(QFont('Arial', 10))
        self.label_download.setAlignment(Qt.AlignCenter)
        self.remove_file.setEnabled(False)
        self.update_file.setEnabled(False)
        self.remove_all_files.setEnabled(False)

    def set_up_layout(self):
        self.setTitle("Input Graphs")

        layout = QHBoxLayout()
        layout.addWidget(self.list_files_input)

        buttons = QVBoxLayout()
        buttons.addWidget(self.add_file)
        buttons.addWidget(self.remove_file)
        buttons.addWidget(self.update_file)
        buttons.addWidget(self.remove_all_files)
        buttons.addStretch(5)
        buttons.addWidget(self.label_download)
        buttons.addWidget(self.download_button_hog)
        buttons.addWidget(self.download_button_mckay)
        layout.addLayout(buttons)

        # layout.addStretch(10)
        # layout.addWidget(self.download_button, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
