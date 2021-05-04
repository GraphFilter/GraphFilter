from PyQt5.QtWidgets import *
from src.view.resources.qicons import Icon
from src.view.resources.help_buttons_text import tip_files
from PyQt5 import QtCore


class GraphFilesPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.graph_files_input = QLineEdit()

        self.open_graph_file = QPushButton("...")
        self.add_graph_file = QPushButton("+")

        self.help_button = QPushButton()

        self.complete = False

        self.form = QFormLayout()

        self.set_content_attributes()
        self.define_layout()

    def set_content_attributes(self):
        self.setObjectName("graph_files")

        self.add_graph_file.setEnabled(False)

        self.help_button.setFixedHeight(80)
        self.help_button.setFixedWidth(80)
        self.help_button.setToolTip(tip_files)
        self.help_button.setIcon(Icon('help'))
        self.help_button.setStyleSheet("background: transparent")

    def define_layout(self):
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("<h3>Input Graphs</h3>"))
        title_layout.addWidget(self.help_button, alignment=QtCore.Qt.AlignRight)
        self.form.addRow(title_layout)

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .g6 file:"))
        file_line.addWidget(self.graph_files_input)
        file_line.addWidget(self.open_graph_file)
        file_line.addWidget(self.add_graph_file)

        self.form.addRow(file_line)

        self.form.setContentsMargins(80, 10, 80, 50)

        self.setLayout(self.form)

    def isComplete(self):
        return self.complete
