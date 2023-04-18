from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class NewGraphDialog(QDialog):
    def __init__(self, attributes_names, **kwargs):
        super().__init__()

        self.dict = kwargs
        self.dict_attributes_names = attributes_names

        self.dialog_next_button = QPushButton("Create")
        self.new_file_radio = QRadioButton("New single file:")
        self.insert_final_radio = QRadioButton("Insert in final of the current list")
        self.graph_link = QPushButton("Link to definition")

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("New Graph")
        layout = QFormLayout()

        layout.addRow(QLabel("New graph will be insert in: "))
        for key, value in self.dict.items():
            self.dict[key] = QLineEdit(value)
            if key == "name":
                layout.addRow(self.new_file_radio, self.dict[key])
                layout.addRow(self.insert_final_radio)
                layout.addRow(QLabel(value), self.graph_link)
                layout.addRow(QLabel("Attributes: "))
            else:
                layout_aux = QFormLayout()
                layout_aux.addRow(" " + self.dict_attributes_names[key] + " =", self.dict[key])
                layout.addRow(layout_aux)

        layout.addRow(self.dialog_next_button)

        layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        layout.setLabelAlignment(Qt.AlignLeft)

        self.setLayout(layout)
