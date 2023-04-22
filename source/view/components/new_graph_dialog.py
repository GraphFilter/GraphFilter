from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class NewGraphDialog(QDialog):
    def __init__(self, attributes_names, **kwargs):
        super().__init__()

        self.dict = kwargs
        self.dict_attributes_names = attributes_names

        self.create_button = QPushButton("Create")
        self.new_file_radio = QRadioButton("New single file:")
        self.insert_final_radio = QRadioButton("Insert in final of the current list")
        self.graph_link = QPushButton("Link to definition")

        self.create_button.setDefault(True)
        self.create_button.setDisabled(True)

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("New Graph")
        layout = None

        for key, value in self.dict.items():
            self.dict[key] = QLineEdit(value)
            if key == "name":
                layout = self.set_initial_layout()
            else:
                layout_aux = QHBoxLayout()
                layout_aux.addWidget(QLabel("  " + self.dict_attributes_names[key] + " ="), 0)
                layout_aux.addWidget(self.dict[key], 1, Qt.AlignRight)
                layout.addRow(layout_aux)

        layout.addRow(self.create_button)

        layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        layout.setLabelAlignment(Qt.AlignLeft)

        self.setLayout(layout)

    def set_initial_layout(self):
        layout = QFormLayout()
        layout_aux = QHBoxLayout()
        name = QLabel(self.dict["name"].text() + " : ")
        attributes = QLabel("Attributes: ")

        self.new_file_radio.setStyleSheet("padding: 0px 0px 0px 10px;")
        self.new_file_radio.setChecked(True)
        self.insert_final_radio.setStyleSheet("padding: 0px 0px 0px 10px;")
        name.setStyleSheet("font-weight: bold")
        attributes.setStyleSheet("font-weight: bold")
        attributes.setContentsMargins(0, 0, 0, 5)

        layout_aux.addWidget(self.new_file_radio, 0)
        layout_aux.addWidget(self.dict["name"], 1)
        layout_aux.setContentsMargins(0, 5, 0, 0)

        layout.addRow(QLabel("New graph will be insert in: "))
        layout.addRow(layout_aux)
        layout.addRow(self.insert_final_radio)

        layout_aux = QHBoxLayout()

        layout_aux.addWidget(name)
        layout_aux.addWidget(self.graph_link, 1)
        layout_aux.setContentsMargins(0, 5, 0, 0)

        layout.addRow(layout_aux)

        if self.dict_attributes_names is not None:
            layout.addRow(attributes)

        return layout
