from PyQt5.QtWidgets import *


class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setFixedWidth(200)
        self.create_conditions()

        math_tab = QTabWidget()
        math_tab.setFixedHeight(200)
        math_tab.addTab(Tab0(), "Tab0")
        math_tab.addTab(Tab1(), "Tab1")

        equation = QLineEdit()

        mode = QGroupBox("Mode")
        mode.setFixedHeight(200)
        mode_layout = QVBoxLayout()
        mode_layout.addWidget(QRadioButton("Filter Graphs"))
        mode_layout.addWidget(QRadioButton("Find counter example"))
        mode.setLayout(mode_layout)

        sider_layout = QVBoxLayout()
        sider_layout.setSpacing(80)
        sider_layout.addWidget(math_tab)
        sider_layout.addWidget(equation)
        sider_layout.addWidget(mode)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.conditions)
        main_layout.addLayout(sider_layout)

        self.setLayout(main_layout)

    def create_conditions(self):
        conditions_layout = QVBoxLayout()
        for i in range(1, 20):
            conditions_layout.addWidget(QCheckBox("Checkbox"))
        self.conditions.setLayout(conditions_layout)


class Tab0(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        for i, n in enumerate(range(0, 9)):
            layout.addWidget(QPushButton("%"), 0, n)
            layout.addWidget(QPushButton("%"), 1, n)

        self.setLayout(layout)


class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        for i, n in enumerate(range(0, 9)):
            layout.addWidget(QPushButton("%"), 0, n)
            layout.addWidget(QPushButton("%"), 1, n)

        self.setLayout(layout)
