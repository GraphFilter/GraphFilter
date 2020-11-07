import sys
from PyQt5.QtWidgets import *
from src.views.form import Form


class FilterGraphs(QWidget):

    def __init__(self):
        super().__init__()

        self.right = self.invariants_list()

        self.ui_components()

    def ui_components(self):
        layout = QHBoxLayout(self)
        layout.addWidget(Form())
        layout.addWidget(self.right)

    def invariants_list(self):
        group_box = QGroupBox("Dictionary of invariants")
        invariants = QVBoxLayout(self)
        invariants.setSpacing(0)
        invariants.addWidget(QLabel("ac - Algebraic Connectivity"))
        invariants.addWidget(QLabel("mu1 - Largest Lapla Eigen"))
        invariants.addWidget(QLabel("mu2 - Second Largest Lapla"))
        group_box.setLayout(invariants)
        return group_box
