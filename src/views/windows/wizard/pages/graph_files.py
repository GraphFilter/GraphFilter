from PyQt5.QtWidgets import *


class GraphFiles(QWizardPage):

    def __init__(self):
        super().__init__()

        self.setObjectName("graph_files")

        self.files_added = []

        graph_files_input = QLineEdit()
        self.registerField('graph_files*', graph_files_input)

        graph_files_button = QPushButton("...")

        self.graph_files_add = QPushButton("+")
        self.graph_files_add.setEnabled(False)
        self.graph_files_add.clicked.connect(self.add_file)

        graph_files_button.clicked.connect(self.open_file)

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Graph .q6 file:"))
        file_line.addWidget(graph_files_input)
        file_line.addWidget(graph_files_button)
        file_line.addWidget(self.graph_files_add)

        self.form = QFormLayout()
        self.form.addRow(file_line)

        self.setLayout(self.form)

    def open_file(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Graph Filter (*.g6)"])
        file_path = file_dialog.getOpenFileName(filter="Graph Filter (*.g6)")
        if file_path[0] not in self.files_added and file_path[0] != '':
            input_file[-1].setText(file_path[0])
            self.files_added.append(file_path[0])
            self.graph_files_add.setEnabled(True)
        print(self.files_added)

    def add_file(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        if input_file[-1].text() != '':
            input_file = QLineEdit()
            button = QPushButton("...")
            remove = QPushButton("-")

            button.clicked.connect(self.open_file)

            layout = QHBoxLayout()
            layout.addWidget(QLabel("Graph .q6 file:"))
            layout.addWidget(input_file)
            layout.addWidget(button)
            layout.addWidget(remove)

            self.form.addRow(layout)

            remove.clicked.connect(lambda: self.remove_row(layout, input_file))
            self.graph_files_add.setEnabled(False)

    def return_files(self):
        return self.files_added

    def remove_row(self, layout, input_file):
        text = input_file.text()
        if text in self.files_added:
            self.files_added.remove(input_file.text())
        print(self.files_added)
        self.form.removeRow(layout)
        self.graph_files_add.setEnabled(True)
