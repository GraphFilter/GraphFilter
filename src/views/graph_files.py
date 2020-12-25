from PyQt5.QtWidgets import *


class GraphFiles(QWizardPage):

    def __init__(self):
        super().__init__()

        self.graph_files_input = QLineEdit()
        graph_files_button = QPushButton("...")
        graph_files_add = QPushButton("+")

        graph_files_button.clicked.connect(self.open_file)

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .q6 file:"))
        file_line.addWidget(self.graph_files_input)
        file_line.addWidget(graph_files_button)
        file_line.addWidget(graph_files_add)

        self.form = QFormLayout()
        self.form.addRow(file_line)

        self.setLayout(self.form)

    def open_file(self):
        file_dialog = QFileDialog()
        file_name = file_dialog.getOpenFileName(self, 'OpenFile')
        self.graph_files.setText(file_name[0])
