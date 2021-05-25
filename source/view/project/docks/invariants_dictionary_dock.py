import json
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class InvariantsDictionaryDock(QDockWidget):
    def __init__(self):
        super().__init__()
        self.invariants_dictionary = InvariantsDictionary()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setWindowTitle("Dictionary")
        self.setObjectName("Dictionary")

        self.setFeatures(QDockWidget.DockWidgetFloatable |
                         QDockWidget.DockWidgetMovable |
                         QDockWidget.DockWidgetClosable)

        self.setWidget(self.invariants_dictionary)

        self.setMinimumHeight(800)


class InvariantsDictionary(QWidget):

    def __init__(self):
        super().__init__()

        self.concepts = QGroupBox("Concepts")
        self.concepts_list = QListWidget()
        self.dictionary = []
        self.title = QLabel()
        self.definitions = QLabel()
        self.usages = QLabel()
        self.implementations = QLabel()
        self.references = QLabel()

        self.set_content_attributes()
        self.set_up_layout()
        self.create_concepts()

    def set_content_attributes(self):
        self.concepts.setMaximumWidth(250)
        self.setVisible(False)
        f = open('resources/data/data_dictionary.json')
        data = json.load(f)

        self.dictionary = data['dic']

        self.title.setFont(QtGui.QFont("Arial", 20))
        self.title.setWordWrap(True)

        self.definitions.setWordWrap(True)
        self.definitions.setFont(QtGui.QFont("Cambria", 14))

        self.usages.setWordWrap(True)
        self.usages.setFont(QtGui.QFont("Cambria", 14))

        self.implementations.setWordWrap(True)
        self.implementations.setFont(QtGui.QFont("Arial", 14))

        self.references.setWordWrap(True)
        self.references.setFont(QtGui.QFont("Arial", 14))

    def set_up_layout(self):
        aside_layout = QVBoxLayout()

        aside_layout.addWidget(self.title)
        aside_layout.addSpacing(30)

        aside_layout.addWidget(QLabel("<h2>Definitions</h2>"))
        aside_layout.addSpacing(10)
        aside_layout.addWidget(self.definitions)
        aside_layout.addSpacing(30)

        aside_layout.addWidget(QLabel("<h2>Usages</h2>"))
        aside_layout.addSpacing(10)
        aside_layout.addWidget(self.usages)
        aside_layout.addSpacing(30)

        aside_layout.addWidget(QLabel("<h2>Implementations</h2>"))
        aside_layout.addSpacing(10)
        aside_layout.addWidget(self.implementations)
        aside_layout.addSpacing(30)

        aside_layout.addWidget(QLabel("<h2>References</h2>"))
        aside_layout.addWidget(self.references)
        aside_layout.addStretch(0)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.concepts)
        main_layout.addLayout(aside_layout)

        self.setLayout(main_layout)

    def create_concepts(self):
        concepts_layout = QVBoxLayout()

        # NOTE: this code generate multiples items
        for i, concept in enumerate(self.dictionary):
            self.concepts_list.insertItem(i, concept['name'])

        self.concepts_list.itemSelectionChanged.connect(self.on_clicked_concept)

        concepts_layout.addWidget(self.concepts_list)
        self.concepts.setLayout(concepts_layout)
        self.concepts_list.setCurrentItem(self.concepts_list.item(0))
        self.on_clicked_concept()

    def on_clicked_concept(self):
        line_sheet = self.concepts_list.currentRow()
        self.title.setText(self.concepts_list.currentItem().text())
        self.definitions.setText(self.dictionary[line_sheet]['definition'])
        self.usages.setText(self.dictionary[line_sheet]['usage'])
        self.implementations.setText(self.dictionary[line_sheet]['implementation'])
        self.references.setOpenExternalLinks(True)
        self.references.setText('<a href={0}>{0}</a>'.format(self.dictionary[line_sheet]['link']))
