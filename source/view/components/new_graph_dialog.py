from PyQt5.QtWidgets import *


class NewGraphDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__()

        self.dict = kwargs

        self.dialog_next_button = QPushButton("Next")

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Attributes")
        layout = QVBoxLayout()
        for key, value in self.dict.items():
            layout.addWidget(QLabel(key))
            self.dict[key] = QLineEdit(value)
            layout.addWidget(self.dict[key])

        layout.addWidget(self.dialog_next_button)
        self.setLayout(layout)
