from PyQt5.QtWidgets import *


class GraphFiles(QWizardPage):

    def __init__(self):
        super().__init__()

        graph_files_input = QLineEdit()
        graph_files_button = QPushButton("...")
        graph_files_add = QPushButton("+")
        graph_files_add.clicked.connect(self.add_file)

        graph_files_button.clicked.connect(lambda: self.open_file(graph_files_input))

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .q6 file:"))
        file_line.addWidget(graph_files_input)
        file_line.addWidget(graph_files_button)
        file_line.addWidget(graph_files_add)

        self.form = QFormLayout()
        self.form.addRow(file_line)

        self.setLayout(self.form)

    def open_file(self, input_file):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Graph Filter (*.g6)"])
        file_path = file_dialog.getOpenFileName(filter="Graph Filter (*.g6)")
        input_file.setText(file_path[0])

    def add_file(self):
        input_file = QLineEdit()
        button = QPushButton("...")
        add = QPushButton("+")
        remove = QPushButton("-")

        add.clicked.connect(self.add_file)
        button.clicked.connect(lambda: self.open_file(input_file))

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Graph .q6 file:"))
        layout.addWidget(input_file)
        layout.addWidget(button)
        layout.addWidget(add)
        layout.addWidget(remove)

        self.form.addRow(layout)

        remove.clicked.connect(lambda: self.form.removeRow(layout))
