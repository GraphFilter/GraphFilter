import os
import xlrd
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class Dictionary(QWidget):

    def __init__(self, project_window):
        super().__init__()

        self.project_window = project_window

        self.concepts = QGroupBox("Concepts")
        self.concepts.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.concepts.setMaximumWidth(250)

        self.concepts_list = QListWidget()
        self.sheet = xlrd.open_workbook(os.getcwd() + '/views/resources/data_dictionary.xls').sheet_by_name('dic')
        self.title = QLabel()
        self.title.setFont(QtGui.QFont("Arial", 20))
        self.title.setWordWrap(True)
        self.definitions = QLabel()
        self.definitions.setWordWrap(True)
        self.definitions.setFont(QtGui.QFont("Arial", 14))
        self.usages = QLabel()
        self.usages.setWordWrap(True)
        self.usages.setFont(QtGui.QFont("Arial", 14))
        self.references = QLabel()
        self.references.setWordWrap(True)
        self.references.setFont(QtGui.QFont("Arial", 14))

        self.create_concepts()

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
        for i in range(1, self.sheet.nrows):
            self.concepts_list.insertItem(i, self.sheet.cell_value(i, 0))

        # TODO connect with select from keyboard
        self.concepts_list.clicked.connect(self.on_clicked_concept)

        concepts_layout.addWidget(self.concepts_list)
        self.concepts.setLayout(concepts_layout)
        self.concepts_list.setCurrentItem(self.concepts_list.item(0))
        self.on_clicked_concept()
        # self.title.setText(f"<h1>{self.concepts_list.currentItem().text()}<\h1>")

    def on_clicked_concept(self):
        line_sheet = self.concepts_list.currentRow() + 1
        self.title.setText(self.concepts_list.currentItem().text())
        self.definitions.setText(self.sheet.cell_value(line_sheet, 1))
        self.usages.setText(self.sheet.cell_value(line_sheet, 2))
        self.references.setOpenExternalLinks(True)
        self.references.setText('<a href={0}>{0}</a>'.format(self.sheet.cell_value(line_sheet, 3)))
