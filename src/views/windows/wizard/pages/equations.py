import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.domain.filter_list import FilterList


class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        filter_backend = FilterList()

        self.filter_backend = filter_backend
        self.dict_num_invariant = filter_backend.invariant_num.dic_name_code
        self.dict_graph_operation = filter_backend.operations_graph.dic_name_code
        self.dict_math_operation = filter_backend.operations_math.dic_name_code
        self.dict_bool_invariant = filter_backend.invariant_bool.dic_name_inv
        self.dict_text_equation = {**self.dict_num_invariant, **self.dict_graph_operation, **self.dict_math_operation}
        self.dict_inv_bool_choices = {}

        self.TabNumericInvariant = TabOperations(self, self.dict_num_invariant)
        self.TabGraphOperation = TabOperations(self, self.dict_graph_operation)
        self.TabMathOperation = TabOperations(self, self.dict_math_operation)

        math_tab = QTabWidget()
        math_tab.addTab(self.TabNumericInvariant, "Numeric Invariants")
        math_tab.addTab(self.TabGraphOperation, "Graph Operations")
        math_tab.addTab(self.TabMathOperation, "Math Operations")
        math_tab.setMinimumWidth(500)
        math_tab.setMaximumHeight(300)

        self.equation = QLineEdit()
        self.equation.setPlaceholderText("insert your equation here...")
        self.equation.setFont(QFont("Cambria Math", 12))
        self.equation.setMaximumHeight(30)
        self.equation.textEdited.connect(self.update_line_text)
        self.valid_equation = True

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h3>Equations</h3>"))
        layout.addStretch(2)
        layout.addWidget(self.equation)
        layout.addStretch(5)
        layout.addWidget(math_tab)
        layout.setContentsMargins(80, 30, 80, 30)

        self.setLayout(layout)

    def set_line_text(self):
        button_clicked = QPushButton().sender()
        self.equation.setText(self.equation.text() + self.dict_text_equation[button_clicked.text()])
        self.completeChanged.emit()

    def update_line_text(self):
        text_equation = self.equation.text()
        for text, symbol in self.dict_text_equation.items():
            text_equation = text_equation.replace(text, symbol)
        self.equation.setText(text_equation)
        self.valid_equation = self.filter_backend.validate_expression(self.equation.text())
        self.completeChanged.emit()


class TabOperations(QWidget):
    def __init__(self, equations, dictionary):
        super().__init__()

        layout = QGridLayout()

        count_lines = 0
        count_quantity = 0

        for i, key in enumerate(dictionary):
            button = QPushButton(key)
            button.setText(key)
            button.setMinimumWidth(len(key))
            button.setFont(QtGui.QFont("Cambria Math", 9))
            button.setToolTip(f'{key} : {dictionary[key]}')
            button.setMaximumHeight(30)
            button.clicked.connect(equations.set_line_text)
            if count_quantity == 4:
                count_lines += 1
                count_quantity = 0
            count_quantity += 1
            layout.addWidget(button, count_lines, count_quantity)

        self.setLayout(layout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Equations()
    sys.exit(App.exec())
