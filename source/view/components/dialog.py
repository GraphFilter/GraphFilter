from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


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
        self.input_field_rows.textEdited.connect(self.validate_input)
        self.input_field_cols.textEdited.connect(self.validate_input)

    def set_up_layout(self):
        self.layout.addWidget(self.label_rows)
        self.layout.addWidget(self.input_field_rows)
        self.layout.addWidget(self.label_cols)
        self.layout.addWidget(self.input_field_cols)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def validate_input(self):
        sender = self.sender()
        text = sender.text()
        try:
            value = int(text)
            if value <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "The value must be an integer greater than 0")
            sender.clear()

    def get_number_rows(self):
        return int(self.input_field_rows.text())

    def get_number_cols(self):
        return int(self.input_field_cols.text())
