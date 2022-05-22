from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from source.store import help_button_text


class EquationsPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = True

        self.incomplete_message = "Equation or conditions must be filled"
        self.alert_text = help_button_text.equation

        self.equation = QLineEdit()
        self.equation_validation = QLabel()
        self.math_tab = QTabWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.equation.setPlaceholderText("insert your equation here...")
        self.equation.setFont(QFont("Cambria Math", 12))
        self.equation.setMaximumHeight(30)

        self.math_tab.setMinimumWidth(500)
        self.math_tab.setMaximumHeight(380)

    def set_up_layout(self):
        self.setTitle("Equation")

        layout = QVBoxLayout()

        layout.addStretch(1)
        layout.addWidget(self.equation)
        layout.addWidget(self.equation_validation)
        layout.addStretch(1)
        layout.addWidget(self.math_tab)
        layout.addStretch(1)
        self.setLayout(layout)

    def set_label_validation_equation(self, error_message):
        if len(error_message) == 0:
            self.equation_validation.setText("Valid equation")
            self.equation_validation.setFont(QtGui.QFont("Arial", 8))
            self.equation_validation.setStyleSheet("color: green")
        else:
            self.equation_validation.setText("Invalid Equation: " + str(error_message))
            self.equation_validation.setFont(QtGui.QFont("Arial", 8))
            self.equation_validation.setStyleSheet("color: red")

    def isComplete(self):
        return self.complete


class TabOperations(QWidget):
    def __init__(self, update_line_text, dictionary):
        super().__init__()

        layout = QGridLayout()

        count_lines = 0
        count_quantity = 0

        for i, key in enumerate(dictionary):
            button = QPushButton(key)
            button.setText(key)
            button.setMinimumWidth(len(key))
            button.setFont(QtGui.QFont("Cambria Math", 9))
            button.setToolTip(f'{key} : {dictionary[key].code}')
            button.setMaximumHeight(30)
            button.clicked.connect(update_line_text)
            if count_quantity == 4:
                count_lines += 1
                count_quantity = 0
            count_quantity += 1
            layout.addWidget(button, count_lines, count_quantity)

        self.setLayout(layout)
