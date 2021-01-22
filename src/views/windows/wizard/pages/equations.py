from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


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

        self.Tab0 = Tab0(self)
        self.Tab1 = Tab1()

        math_tab = QTabWidget()
        math_tab.addTab(self.Tab0, "Tab0")
        math_tab.addTab(self.Tab1, "Tab1")

        self.equation = QLineEdit()
        self.equation.setPlaceholderText("placeholder...")
        self.equation.setFont(QFont("Sanserif", 10))

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

    def checked(self, checkbox):
        if checkbox.isChecked():
            print(checkbox.isChecked())
            self.checkboxes.append(checkbox.text())
        else:
            self.checkboxes.remove(checkbox.text())
        print(self.checkboxes)


class Tab0(QWidget):
    def __init__(self, equations):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(20)

        button = QPushButton("%")
        button.clicked.connect(lambda: equations.set_line_text(button.text()))

        layout.addWidget(button, 0, 0)

        self.setLayout(layout)


class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        for i, n in enumerate(range(0, 9)):
            layout.addWidget(QPushButton("%"), 0, n)
            layout.addWidget(QPushButton("%"), 1, n)

        self.setLayout(layout)
