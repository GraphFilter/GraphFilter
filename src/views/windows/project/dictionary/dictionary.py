from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class Dictionary(QWidget):

    def __init__(self, project_window):
        super().__init__()

        self.project_window = project_window

        self.concepts = QGroupBox("Concepts")
        self.concepts.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.concepts.setMaximumWidth(250)

        self.concepts_list = QListWidget()

        self.title = QLabel()
        self.definitions = QLabel()
        self.usages = QLabel()
        self.references = QLabel()

        self.create_concepts()

        # TODO: learn how to control better the spacing in vbox items

        aside_layout = QVBoxLayout()
        aside_layout.addWidget(self.title)
        aside_layout.addWidget(QLabel("<h2>Definitions</h2>"))
        aside_layout.addWidget(self.definitions)
        aside_layout.addWidget(QLabel("<h2>Usages</h2>"))
        aside_layout.addWidget(self.usages)
        aside_layout.addWidget(QLabel("<h2>References</h2>"))
        aside_layout.addWidget(self.references)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.concepts)
        main_layout.addLayout(aside_layout)

        self.setLayout(main_layout)

    def create_concepts(self):

        concepts_layout = QVBoxLayout()

        # NOTE: this code generate multiples items
        for i in range(1, 20):
            self.concepts_list.insertItem(i, f"Concept {i}")

        self.concepts_list.clicked.connect(self.on_clicked_concept)

        concepts_layout.addWidget(self.concepts_list)
        self.concepts.setLayout(concepts_layout)
        self.concepts_list.setCurrentItem(self.concepts_list.item(0))
        self.title.setText(f"<h1>{self.concepts_list.currentItem().text()}<\h1>")

    def on_clicked_concept(self):
        self.title.setText(f"<h1>{self.concepts_list.currentItem().text()}<\h1>")
