import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

# note the dicts will be imported from backend
dict_invariant = {'alpha': '\u03b1', 'betha': '\u03b2', 'gamma': '\u03b3'}
dict_math_operation = {'sin': 'sin', 'cos': 'cos', 'sqrt': '\u221A'}
dict_graph_operation = {'complement': 'c', 'line': '\u2113'}
dict_union = {**dict_invariant, **dict_graph_operation, **dict_math_operation}


class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.conditions.setMinimumWidth(200)

        self.create_conditions()

        self.radios = {}

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
        for i in range(1, 80):
            button_group = QGroupBox()
            button_group.setFlat(True)
            button_group.setObjectName(f"Condition {i}")

            glayout_aux = QGridLayout()
            glayout_aux.addWidget(QLabel(f"Condition {i}"), i, 0)
            glayout_aux.setColumnMinimumWidth(0, 50)

            true = QRadioButton()
            true.clicked.connect(self.checked)
            true.setObjectName("true")

            false = QRadioButton()
            false.clicked.connect(self.checked)
            false.setObjectName("false")

            glayout_aux.addWidget(true, i, 1, Qt.AlignCenter)
            glayout_aux.addWidget(false, i, 2, Qt.AlignCenter)
            button_group.setLayout(glayout_aux)
            conditions_layout.addWidget(button_group, i, 0)

        vlayout_aux = QVBoxLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(conditions_layout)
        scroll_area.setWidget(widget_aux)
        vlayout_aux.addWidget(scroll_area)
        self.conditions.setLayout(vlayout_aux)

    def set_line_text(self, text):
        button_clicked = QPushButton().sender()
        self.equation.setText(self.equation.text() + button_clicked.text())

    def update_line_text(self):
        text_equation = self.equation.text()
        for text, symbol in dict_union.items():
            text_equation = text_equation.replace(text, symbol)
        self.equation.setText(text_equation)

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

        print(self.radios)


class TabNumericInvariant(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(dict_invariant):
            button = QPushButton(dict_invariant[key])
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(key)  # key and name
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


class TabGraphOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(dict_graph_operation):
            button = QPushButton(dict_graph_operation[key])
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(f'{key} : -invariant-')  # key and name of invariant or operation
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


class TabMathOperation(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()

        for i, key in enumerate(dict_math_operation):
            button = QPushButton(dict_math_operation[key])
            button.setMaximumSize(70, 40)
            button.setFont(QtGui.QFont("Cambria Math", 12))
            button.setToolTip(key)  # key and name
            button.clicked.connect(equations.set_line_text)
            layout.addWidget(button, 0, i)

        self.setLayout(layout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Equations()
    sys.exit(App.exec())
