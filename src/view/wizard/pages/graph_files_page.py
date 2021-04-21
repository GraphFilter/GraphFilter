from PyQt5.QtWidgets import *


class GraphFilesPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.graph_files_input = QLineEdit()
        self.registerField('graph_files*', self.graph_files_input)

        self.open_graph_file = QPushButton("...")
        self.add_graph_file = QPushButton("+")

        self.form = QFormLayout()

        self.set_content_attributes()
        self.define_layout()

    def set_content_attributes(self):
        self.setObjectName("graph_files")

        self.add_graph_file.setEnabled(False)

    def define_layout(self):
        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .g6 file:"))
        file_line.addWidget(self.graph_files_input)
        file_line.addWidget(self.open_graph_file)
        file_line.addWidget(self.add_graph_file)

        self.form.addRow(file_line)

        self.setLayout(self.form)
