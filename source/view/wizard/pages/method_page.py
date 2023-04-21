from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from source.view.components.icon import Icon
from source.store import help_button_text


class MethodPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.incomplete_message = "Select the filtering method"
        self.alert_text = help_button_text.method

        self.filter_button = QPushButton()
        self.counter_example_button = QPushButton()
        self.blank_project =QPushButton()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):

        self.filter_button.setText("  Filter Graphs")
        self.filter_button.setIcon(Icon("filter"))
        self.filter_button.setMinimumHeight(50)
        self.filter_button.setMinimumWidth(50)
        self.filter_button.setCheckable(True)
        self.filter_button.setObjectName('filter')

        self.counter_example_button.setText("  Find Counterexample")
        self.counter_example_button.setIcon(Icon("zoom"))
        self.counter_example_button.setMinimumHeight(50)
        self.counter_example_button.setMinimumWidth(50)
        self.counter_example_button.setCheckable(True)
        self.counter_example_button.setObjectName('counterexample')

        self.blank_project.setText(" Blank project \n "
                                   " Drawn your own graphs")
        
        self.blank_project.setIcon(Icon("edit"))
        self.blank_project.setMinimumHeight(50)
        self.blank_project.setMinimumWidth(100)
        self.blank_project.setCheckable(True)
        self.blank_project.setObjectName("blank")


    def set_up_layout(self):
        self.setTitle("Method")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.filter_button)
        button_layout.addWidget(self.counter_example_button)

        second_button_layout = QHBoxLayout()
        second_button_layout.addWidget(self.blank_project)
        #second_button_layout.setAlignment(Qt.AlignCenter)
        second_button_layout.setContentsMargins(150,0,150,0)
        #second_button_layout.

        layout = QVBoxLayout()
        layout.addStretch(3)
        layout.addLayout(button_layout)
        layout.addLayout(second_button_layout)
        layout.addStretch(6)
        layout.setSpacing(30)
        self.setMinimumWidth(330)

        layout.setContentsMargins(50, 0, 50, 0)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
