from PyQt5.QtWidgets import *
from source.store.help_buttons_text import tip_files
from source.view.resources.components.help_button import HelpButton
from source.view.resources.components.icon import Icon
from PyQt5 import QtCore


class GraphFilesPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.graph_files_input = QLineEdit()

        self.open_graph_file = QPushButton("...")
        self.add_graph_file = QPushButton("+")

        self.help_button = HelpButton(tip_files)

        self.hog_page = QPushButton(" get .g6 graph")

        self.complete = False

        self.form = QFormLayout()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setObjectName("graph_files")
        self.hog_page.setIcon(Icon('download'))
        self.hog_page.setFixedWidth(120)
        self.hog_page.setFixedHeight(40)

        self.add_graph_file.setEnabled(False)

    def set_up_layout(self):
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("<h3>Input Graphs</h3>"))
        title_layout.addWidget(self.help_button, alignment=QtCore.Qt.AlignRight)



        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .g6 file:"))
        file_line.addWidget(self.graph_files_input)
        file_line.addWidget(self.open_graph_file)
        file_line.addWidget(self.add_graph_file)

        self.form.addRow(file_line)

        layout = QVBoxLayout()
        layout.addLayout(title_layout)
        layout.addStretch(1)
        layout.addLayout(self.form)
        layout.addStretch(10)
        layout.addWidget(self.hog_page, alignment=QtCore.Qt.AlignRight)
        layout.setContentsMargins(80, 10, 80, 30)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
