# import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.domain.filter_list import FilterList


class Conditions(QWizardPage):

    def __init__(self, previous_page):
        super().__init__()

        self.setObjectName("conditions")

        filter_backend = FilterList()

        self.previous_page = previous_page

        self.dict_bool_invariant = filter_backend.invariant_bool.dic_name_inv

        self.structural_invariants_group = ComboBoxesGroup("Structural", self.dict_bool_invariant, self)
        self.spectral_invariants_group = ComboBoxesGroup("Spectral", self.dict_bool_invariant, self)

        self.dict_inv_bool_choices = {}

        center_layout = QHBoxLayout()
        center_layout.addWidget(self.structural_invariants_group)
        center_layout.addStretch(2)
        center_layout.addWidget(self.spectral_invariants_group)

        hint_button = QPushButton()
        hint_button.setStyleSheet("border-radius: 50")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h3>Conditions</h3>"))
        layout.addStretch(5)
        layout.addLayout(center_layout)
        layout.setContentsMargins(80, 30, 80, 50)

        self.setLayout(layout)

    def isComplete(self):
        if len(self.dict_inv_bool_choices) < 1 and self.previous_page.equation.text() == "":
            return False
        else:
            return True


class ComboBoxesGroup(QGroupBox):
    def __init__(self, title, dictionary, conditions):
        super().__init__()

        self.setTitle(title)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.dictionary = dictionary
        self.conditions_layout = QGridLayout()
        self.scroll_area = QScrollArea()
        self.setMinimumWidth(350)
        self.conditions = conditions

        self.create_layout()
        self.fill_combos()

    def create_layout(self):
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)

        self.conditions_layout.setHorizontalSpacing(20)

        button_group = QGroupBox()
        button_group.setFlat(True)

        grid_layout_aux = QGridLayout()
        grid_layout_aux.setColumnMinimumWidth(0, 200)
        grid_layout_aux.addWidget(QLabel("true"), 0, 1, Qt.AlignCenter)
        grid_layout_aux.addWidget(QLabel("false"), 0, 2, Qt.AlignCenter)
        button_group.setLayout(grid_layout_aux)
        self.conditions_layout.addWidget(button_group, 0, 0)

    def fill_combos(self):
        for i, key in enumerate(self.dictionary):
            button_group = QGroupBox()
            button_group.setFlat(True)
            button_group.setObjectName(f"{key}")

            grid_layout_aux = QGridLayout()
            grid_layout_aux.addWidget(QLabel(f"{key}"), i + 1, 0)
            grid_layout_aux.setColumnMinimumWidth(0, 200)

            true = QRadioButton()
            true.clicked.connect(self.checked)
            true.setObjectName("true")

            false = QRadioButton()
            false.clicked.connect(self.checked)
            false.setObjectName("false")

            grid_layout_aux.addWidget(true, i + 1, 1, Qt.AlignCenter)
            grid_layout_aux.addWidget(false, i + 1, 2, Qt.AlignCenter)
            button_group.setLayout(grid_layout_aux)
            self.conditions_layout.addWidget(button_group, i + 1, 0)

        vertical_layout_aux = QVBoxLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(self.conditions_layout)
        self.scroll_area.setWidget(widget_aux)
        vertical_layout_aux.addWidget(self.scroll_area)
        self.setLayout(vertical_layout_aux)

    def checked(self):
        radio = QRadioButton().sender()
        groupbox = radio.parentWidget()
        if groupbox.objectName() in self.conditions.dict_inv_bool_choices.keys():
            if self.conditions.dict_inv_bool_choices.get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                self.conditions.dict_inv_bool_choices.pop(groupbox.objectName())
                print(self.conditions.dict_inv_bool_choices)
                self.conditions.completeChanged.emit()
                return
        self.conditions.dict_inv_bool_choices[groupbox.objectName()] = radio.objectName()
        self.conditions.completeChanged.emit()

        print(self.conditions.dict_inv_bool_choices)
