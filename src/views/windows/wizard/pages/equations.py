import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Equations(QWizardPage):

    def __init__(self, filter_backend):
        super().__init__()

        self.filter_backend = filter_backend
        self.dict_num_invariant = {}
        self.dict_graph_operation = {}
        self.dict_math_operation = {}
        self.dict_bool_invariant = {}
        self.dict_text_equation = {}
        self.build_dic_invariants()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.conditions.setMinimumWidth(200)

        self.create_conditions()

        self.radios = {}

        self.method = ''

        #TODO: set scroll area in tabs
        self.TabNumericInvariant = TabNumericInvariant(self)
        self.TabGraphOperation = TabGraphOperation(self)
        self.TabMathOperation = TabMathOperation(self)

        math_tab = QTabWidget()
        math_tab.addTab(self.TabNumericInvariant, "Numeric Invariants")
        math_tab.addTab(self.TabGraphOperation, "Graph Operations")
        math_tab.addTab(self.TabMathOperation, "Math Operations")
        math_tab.setMinimumWidth(700)

        self.equation = QLineEdit()
        self.equation.setPlaceholderText("placeholder...")
        self.equation.setFont(QFont("Cambria Math", 12))
        self.equation.setMaximumHeight(30)
        self.equation.textEdited.connect(lambda: self.update_line_text())

        box_method = QGroupBox("Method")
        box_method.setFixedHeight(200)
        method_layout = QVBoxLayout()
        self.radio_filter = QRadioButton("Filter Graphs")
        self.radio_counter = QRadioButton("Find counter example")
        self.radio_filter.clicked.connect(self.method_clicked)
        self.radio_counter.clicked.connect(self.method_clicked)
        method_layout.addWidget(self.radio_filter)
        method_layout.addWidget(self.radio_counter)
        box_method.setLayout(method_layout)

        # TODO: learn how to control better the spacing in vbox items

        aside_layout = QVBoxLayout()
        aside_layout.addStretch(3)
        aside_layout.addWidget(math_tab)
        aside_layout.addStretch(5)
        aside_layout.addWidget(self.equation)
        aside_layout.addStretch(45)
        aside_layout.addWidget(box_method)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.conditions)
        main_layout.addLayout(aside_layout)

        self.setLayout(main_layout)

    def build_dic_invariants(self):

        for inv in self.filter_backend.invariant_num.all:
            self.dict_num_invariant[inv.name] = inv.code

        for op in self.filter_backend.operations_graph.all:
            self.dict_graph_operation[op.name] = op.code

        for op in self.filter_backend.operations_math.all:
            self.dict_math_operation[op.name] = op.code

        for inv in self.filter_backend.invariant_bool.all:
            self.dict_bool_invariant[inv.name] = inv

        self.dict_text_equation = {**self.dict_num_invariant, **self.dict_graph_operation, **self.dict_math_operation}

    def method_clicked(self):
        choice = QPushButton().sender().text()
        if 'filter' in choice.lower():
            self.method = 'filter'
        else:
            self.method = 'counterexample'
        self.completeChanged.emit()

    def create_conditions(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)

        conditions_layout = QGridLayout()
        conditions_layout.setHorizontalSpacing(20)

        button_group = QGroupBox()
        button_group.setFlat(True)

        glayout_aux = QGridLayout()
        glayout_aux.setColumnMinimumWidth(0, 50)
        glayout_aux.addWidget(QLabel("true"), 0, 1, Qt.AlignCenter)
        glayout_aux.addWidget(QLabel("false"), 0, 2, Qt.AlignCenter)
        button_group.setLayout(glayout_aux)
        conditions_layout.addWidget(button_group, 0, 0)

        # NOTE: this code generate multiples radio buttons
        for i, key in enumerate(self.dict_bool_invariant):
            button_group = QGroupBox()
            button_group.setFlat(True)
            button_group.setObjectName(f"{key}")

            glayout_aux = QGridLayout()
            glayout_aux.addWidget(QLabel(f"{key}"), i+1, 0)
            glayout_aux.setColumnMinimumWidth(0, 50)

            true = QRadioButton()
            true.clicked.connect(self.checked)
            true.setObjectName("true")

            false = QRadioButton()
            false.clicked.connect(self.checked)
            false.setObjectName("false")

            glayout_aux.addWidget(true, i+1, 1, Qt.AlignCenter)
            glayout_aux.addWidget(false, i+1, 2, Qt.AlignCenter)
            button_group.setLayout(glayout_aux)
            conditions_layout.addWidget(button_group, i+1, 0)

        vlayout_aux = QVBoxLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(conditions_layout)
        scroll_area.setWidget(widget_aux)
        vlayout_aux.addWidget(scroll_area)
        self.conditions.setLayout(vlayout_aux)

    def set_line_text(self):
        button_clicked = QPushButton().sender()
        self.equation.setText(self.equation.text() + self.dict_text_equation[button_clicked.text()])
        self.completeChanged.emit()

    def update_line_text(self):
        text_equation = self.equation.text()
        for text, symbol in self.dict_text_equation.items():
            text_equation = text_equation.replace(text, symbol)
        self.equation.setText(text_equation)
        self.completeChanged.emit()

    def checked(self):
        radio = QRadioButton().sender()
        groupbox = radio.parentWidget()

        if groupbox.objectName() in self.radios.keys():
            if self.radios.get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                self.radios.pop(groupbox.objectName())
                print(self.radios)
                return

        self.radios[groupbox.objectName()] = radio.objectName()

        self.completeChanged.emit()

        print(self.radios)

    def isComplete(self):
        if (not self.equation.text() and not self.radios) or (not self.method):
            print('not text')
            return False
        else:
            print('text')
            return True

    def extract_filtering_data(self):
        list_inv_bool_choices = []
        for inv_name in self.radios.keys():
            if self.radios[inv_name] == "true":
                list_inv_bool_choices.append((self.dict_bool_invariant[inv_name], True))
            elif self.radios[inv_name] == "false":
                list_inv_bool_choices.append((self.dict_bool_invariant[inv_name], False))
        return self.equation.text(), list_inv_bool_choices, self.method


class TabNumericInvariant(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(equations.dict_num_invariant):
            button = QPushButton(key)
            button.setText(key)
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(f'{key} : {equations.dict_num_invariant[key]}')
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


class TabGraphOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(equations.dict_graph_operation):
            button = QPushButton(key)
            button.setText(key)
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(f'{key} : {equations.dict_graph_operation[key]}')  # key and name of invariant or operation
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


class TabMathOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(equations.dict_math_operation):
            button = QPushButton(key)
            button.setText(key)
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(f'{key} : {equations.dict_math_operation[key]}')
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Equations()
    sys.exit(App.exec())
