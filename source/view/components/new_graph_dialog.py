from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class NewGraphDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__()

        self.dict = kwargs

        self.dialog_next_button = QPushButton("Next")
        self.new_file_radio = QRadioButton("New single file:")
        self.insert_final_radio = QRadioButton("Insert in final of the current list")

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Attributes")
        layout = QFormLayout()

        layout.addRow(QLabel("New graph will be insert in: "))
        for key, value in self.dict.items():
            self.dict[key] = QLineEdit(value)
            if key == "name":
                layout.addRow(self.new_file_radio, self.dict[key])
                layout.addRow(self.insert_final_radio)
            else:
                layout_aux = QFormLayout()
                layout_aux.addRow(" " + key + "=", self.dict[key])
                layout.addRow(layout_aux)

        layout.addRow(self.dialog_next_button)

        layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        layout.setLabelAlignment(Qt.AlignLeft)

        self.setLayout(layout)
