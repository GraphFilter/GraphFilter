from PyQt5.QtWidgets import *
from src.view.resources.qicons import Icon


class MethodPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.filter_button = QPushButton()
        self.counter_example_button = QPushButton()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setObjectName("method")

        self.filter_button.setText("  Filter Graphs")
        self.filter_button.setIcon(Icon("filter"))
        self.filter_button.setMinimumHeight(50)
        self.filter_button.setMinimumWidth(300)
        self.filter_button.setCheckable(True)
        self.filter_button.setObjectName('filter')

        self.counter_example_button.setText("  Find Counterexample")
        self.counter_example_button.setIcon(Icon("zoom"))
        self.counter_example_button.setMinimumHeight(50)
        self.counter_example_button.setMinimumWidth(300)
        self.counter_example_button.setCheckable(True)
        self.counter_example_button.setObjectName('counterexample')

    def set_up_layout(self):
        button_layout = QHBoxLayout()

        button_layout.addWidget(self.filter_button)
        button_layout.addStretch(1)
        button_layout.addWidget(self.counter_example_button)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h3>Method</h3>"))
        layout.addStretch(2)
        layout.addLayout(button_layout)
        layout.addStretch(6)
        layout.setContentsMargins(80, 30, 80, 30)

        self.setLayout(layout)

    def isComplete(self):
        return self.complete
