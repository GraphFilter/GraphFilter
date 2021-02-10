from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Equations(QWizardPage):

    def __init__(self):
        super().__init__()

        self.conditions = QGroupBox("Conditions")
        self.conditions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.conditions.setMinimumWidth(200)

        self.create_conditions()

        self.radios = {}

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
        self.equation.setText(self.equation.text() + text)

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
