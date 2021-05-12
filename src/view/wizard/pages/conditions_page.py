from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.store.help_buttons_text import tip_conditions
from src.view.resources.components.help_button import HelpButton


class ConditionsPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.structural_invariants_group: ComboBoxesGroup
        self.spectral_invariants_group: ComboBoxesGroup
        self.help_button = HelpButton(tip_conditions)

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setObjectName("conditions")

    def set_up_layout(self):
        center_layout = QHBoxLayout()
        center_layout.addWidget(self.structural_invariants_group)
        center_layout.addStretch(2)
        center_layout.addWidget(self.spectral_invariants_group)

        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("<h3>Conditions</h3>"))
        title_layout.addWidget(self.help_button, alignment=Qt.AlignRight)

        layout = QVBoxLayout()
        layout.addLayout(title_layout)
        layout.addLayout(center_layout)
        layout.setContentsMargins(80, 10, 80, 50)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete


class ComboBoxesGroup(QGroupBox):
    def __init__(self, title, dictionary, update_conditions):
        super().__init__()

        self.title = title
        self.dictionary = dictionary
        self.update_conditions = update_conditions

        self.conditions_layout = QGridLayout()
        self.scroll_area = QScrollArea()

        self.button_group = QGroupBox()

        self.set_content_attributes()
        self.set_up_layout()
        self.fill_combos()

    def set_content_attributes(self):
        self.setTitle(self.title)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(350)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)

        self.conditions_layout.setHorizontalSpacing(20)

        self.button_group.setFlat(True)

    def set_up_layout(self):
        grid_layout_aux = QGridLayout()
        grid_layout_aux.setColumnMinimumWidth(0, 200)
        grid_layout_aux.addWidget(QLabel("true"), 0, 1, Qt.AlignCenter)
        grid_layout_aux.addWidget(QLabel("false"), 0, 2, Qt.AlignCenter)
        self.button_group.setLayout(grid_layout_aux)
        self.conditions_layout.addWidget(self.button_group, 0, 0)

    def fill_combos(self):
        for i, key in enumerate(self.dictionary):
            button_group = QGroupBox()
            button_group.setFlat(True)
            button_group.setObjectName(f"{key}")

            grid_layout_aux = QGridLayout()
            grid_layout_aux.addWidget(QLabel(f"{key}"), i + 1, 0)
            grid_layout_aux.setColumnMinimumWidth(0, 200)

            true = QRadioButton()
            true.clicked.connect(self.update_conditions)
            true.setObjectName("true")

            false = QRadioButton()
            false.clicked.connect(self.update_conditions)
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
