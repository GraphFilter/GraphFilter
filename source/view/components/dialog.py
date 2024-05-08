from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Configuration")
        self.layout = QVBoxLayout(self)
        self.label_rows = QLabel("Enter number of rows:")
        self.input_field_rows = QLineEdit()
        self.label_cols = QLabel("Enter number of columns:")
        self.input_field_cols = QLineEdit()
        self.button = QPushButton("OK")
        self.set_up_layout()
        self.button.clicked.connect(self.accept)

    def set_up_layout(self):
        self.layout.addWidget(self.label_rows)
        self.layout.addWidget(self.input_field_rows)
        self.layout.addWidget(self.label_cols)
        self.layout.addWidget(self.input_field_cols)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def get_number_rows(self):
        return int(self.input_field_rows.text())

    def get_number_cols(self):
        return int(self.input_field_cols.text())
