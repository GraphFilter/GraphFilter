from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.conditions.setMinimumWidth(150)
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

        mode = QGroupBox("Mode")
        mode.setFixedHeight(200)
        mode_layout = QVBoxLayout()
        mode_layout.addWidget(QRadioButton("Filter Graphs"))
        mode_layout.addWidget(QRadioButton("Find counter example"))
        mode.setLayout(mode_layout)

        # TODO: learn how to control better the spacing in vbox items

        sider_layout = QVBoxLayout()
        sider_layout.addStretch(3)
        sider_layout.addWidget(math_tab)
        sider_layout.addStretch(5)
        sider_layout.addWidget(self.equation)
        sider_layout.addStretch(45)
        sider_layout.addWidget(mode)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.conditions)
        main_layout.addLayout(sider_layout)

        self.setLayout(main_layout)

    def create_conditions(self):

        # TODO: groupbox with scroll bar

        conditions_layout = QVBoxLayout()
        checkbox = QCheckBox("Checkbox")
        checkbox.clicked.connect(lambda: self.checked(checkbox))
        conditions_layout.addWidget(checkbox)
        self.conditions.setLayout(conditions_layout)

        # NOTE: this code generate multiples checkboxes
        # for i in range(1, 20):
        #    checkbox = QCheckBox("Checkbox")
        #    checkbox.clicked.connect(lambda: self.checked(checkbox))
        #    conditions_layout.addWidget(checkbox)
        # self.conditions.setLayout(conditions_layout)

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
