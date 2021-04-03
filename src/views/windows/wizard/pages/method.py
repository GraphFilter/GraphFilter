import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Method(QWizardPage):

    def __init__(self):
        super().__init__()

        self.method = ''

        button_layout = QHBoxLayout()

        self.filter_button = QPushButton("  Filter Graphs")
        self.filter_button.setIcon(QIcon("views/resources/icons/filter_filled_tool_symbol.png"))
        self.filter_button.setMinimumHeight(50)
        self.filter_button.setMinimumWidth(300)
        self.filter_button.setCheckable(True)
        self.filter_button.setObjectName('filter')
        self.filter_button.clicked.connect(self.method_clicked)

        self.counter_example_button = QPushButton("  Find Counter Example")
        self.counter_example_button.setIcon(QIcon("views/resources/icons/zoom.png"))
        self.counter_example_button.setMinimumHeight(50)
        self.counter_example_button.setMinimumWidth(300)
        self.counter_example_button.setCheckable(True)
        self.counter_example_button.setObjectName('counterexample')
        self.counter_example_button.clicked.connect(self.method_clicked)

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

    def method_clicked(self):
        self.filter_button.setChecked(False)
        self.counter_example_button.setChecked(False)
        button = QPushButton().sender()
        button.setChecked(True)
        if 'filter' in button.objectName():
            self.method = 'filter'
        else:
            self.method = 'counterexample'
        self.completeChanged.emit()

    def isComplete(self):
        if self.method:
            return True
        else:
            return False


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Method()
    sys.exit(App.exec())
