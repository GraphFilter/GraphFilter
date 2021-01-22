import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

# note the dicts will be imported from backend
dict_invariant = {'alpha': '\u03b1', 'betha': '\u03b2', 'gamma': '\u03b3'}
dict_math_operation = {'sin': 'sin', 'cos': 'cos', 'sqrt': '\u221A'}
dict_graph_operation = {'complement': 'c', 'line': '\u2113'}
dict_union= {**dict_invariant, **dict_graph_operation, **dict_math_operation}

class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.conditions.setMinimumWidth(150)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.create_conditions()

        self.checkboxes = []

        self.TabNumericInvariant = TabNumericInvariant(self)
        self.TabGraphOperation = TabGraphOperation(self)
        self.TabMathOperation = TabMathOperation(self)

        math_tab = QTabWidget()
        math_tab.addTab(self.TabNumericInvariant, "Numeric Invariants")
        math_tab.addTab(self.TabGraphOperation, "Graph Operations")
        math_tab.addTab(self.TabMathOperation, "Math Operations")

        self.equation = QLineEdit()
        self.equation.setPlaceholderText("placeholder...")
        self.equation.setFont(QFont("Cambria Math", 12))
        self.equation.textEdited.connect(lambda: self.update_line_text())

        method = QGroupBox("Method")
        method.setFixedHeight(200)
        method_layout = QVBoxLayout()
        method_layout.addWidget(QRadioButton("Filter Graphs"))
        method_layout.addWidget(QRadioButton("Find counter example"))
        method.setLayout(method_layout)

        # TODO: learn how to control better the spacing in vbox items

        aside_layout = QVBoxLayout()
        aside_layout.addStretch(3)
        aside_layout.addWidget(math_tab)
        aside_layout.addStretch(5)
        aside_layout.addWidget(self.equation)
        aside_layout.addStretch(45)
        aside_layout.addWidget(method)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.conditions)
        main_layout.addLayout(aside_layout)

        self.setLayout(main_layout)

    def create_conditions(self):

        # TODO: groupbox with scroll bar

        conditions_layout = QVBoxLayout()
        checkbox = QCheckBox("Checkbox")
        checkbox.clicked.connect(lambda: self.checked(checkbox))
        conditions_layout.addWidget(checkbox)

        self.conditions.setLayout(conditions_layout)

        # NOTE: this code generate multiples checkboxes
        # for i in range(1, 80):
        #     checkbox = QCheckBox("Checkbox")
        #     checkbox.clicked.connect(lambda: self.checked(checkbox))
        #     conditions_layout.addWidget(checkbox)
        # self.conditions.setLayout(conditions_layout)

        layout_aux = QVBoxLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(conditions_layout)
        self.scroll_area.setWidget(widget_aux)
        layout_aux.addWidget(self.scroll_area)
        self.conditions.setLayout(layout_aux)

    def set_line_text(self, text):
        self.equation.setText(self.equation.text() + text)

    def update_line_text(self):
        textEquation = self.equation.text()
        for text, symbol in dict_union.items():
            textEquation = textEquation.replace(text, symbol)
        self.equation.setText(textEquation)

    def checked(self, checkbox):
        if checkbox.isChecked():
            print(checkbox.isChecked())
            self.checkboxes.append(checkbox.text())
        else:
            self.checkboxes.remove(checkbox.text())
        print(self.checkboxes)


class TabNumericInvariant(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()
        i = 0
        for key in dict_invariant:
            button = QPushButton(dict_invariant[key])
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(key)  # key and name
            button.clicked.connect(lambda: equations.set_line_text(dict_invariant[key]))
            layout.addWidget(button, 0, i)
            i = i + 1
            # todo: bug - the buttons always prints betha

        self.setLayout(layout)


class TabGraphOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()
        i = 0
        for key in dict_graph_operation:
            button = QPushButton(dict_graph_operation[key])
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(f'{key} : -invariant-')  # key and name of invariant or operation
            button.clicked.connect(lambda: equations.set_line_text(dict_graph_operation[key]))
            layout.addWidget(button, 0, i)
            i = i + 1
            # todo: bug - the buttons always prints betha

        self.setLayout(layout)


class TabMathOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()
        i = 0
        for key in dict_math_operation:
            button = QPushButton(dict_math_operation[key])
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(key)  # key and name
            button.clicked.connect(lambda: equations.set_line_text(dict_math_operation[key]))
            layout.addWidget(button, 0, i)
            i = i + 1
            # todo: bug - the buttons always prints betha

        self.setLayout(layout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Equations()
    sys.exit(App.exec())
