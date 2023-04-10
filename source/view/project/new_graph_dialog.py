from PyQt5.QtWidgets import *


class NewGraphDialog(QMessageBox):
    def __init__(self, **kwargs):
        super().__init__()

        self.dict = kwargs

        self.dialog_next_button = QDialogButtonBox(QDialogButtonBox.Ok)

        self.set_content_attributes()

    def set_content_attributes(self):
        for key, value in self.dict.items():
            self.layout().addWidget(QLabel(key))
            self.dict[key] = QLineEdit(value)
            self.layout().addWidget(self.dict[key])
