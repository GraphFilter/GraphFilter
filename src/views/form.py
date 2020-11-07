import sys
from PyQt5.QtWidgets import *


def file_area():
    group_box = QGroupBox("Files")
    files = QGridLayout()
    files.setSpacing(0)
    files.addWidget(QPushButton("Open .q6 file"), 0, 0)
    files.addWidget(QLineEdit(), 0, 1)
    files.addWidget(QPushButton("Output .q6"), 1, 0)
    files.addWidget(QLineEdit(), 1, 1)
    group_box.setLayout(files)
    return group_box


def condition_area():
    group_box = QGroupBox("Condition")
    condition = QGridLayout()
    condition.addWidget(QCheckBox("Regular"), 0, 0)
    condition.addWidget(QCheckBox("Regular with order: "), 1, 0)
    condition.addWidget(QCheckBox("Connected"), 2, 0)
    condition.addWidget(QCheckBox("Hamiltonian"), 0, 1)
    condition.addWidget(QCheckBox("Planar"), 1, 1)
    condition.addWidget(QCheckBox("Acyclic"), 2, 1)
    group_box.setLayout(condition)
    return group_box


class EquationsArea(QWidget):

    def __init__(self):
        super().__init__()

        self.group_box = QGroupBox("Equations")
        self.equations = QHBoxLayout()
        self.text = QLineEdit(self)
        self.text.returnPressed.connect(self.on_pressed)

        self.equations.addWidget(self.text)
        self.group_box.setLayout(self.equations)

    def on_pressed(self):
        print(self.text.text())

    def build(self):
        return self.group_box


class Form(QWidget):

    def __init__(self):
        super().__init__()

        self.ui_components()

    def ui_components(self):
        layout = QVBoxLayout(self)
        layout.addWidget(file_area())
        layout.addWidget(condition_area())
        layout.addWidget(EquationsArea().build())
