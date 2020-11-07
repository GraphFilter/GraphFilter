import sys
from PyQt5.QtWidgets import *
from src.views.filter_graphs import FilterGraphs
from src.views.visualization import Visualization


def tab_division():
    tab = QTabWidget()
    tab.addTab(FilterGraphs(), "Filter Graphs")
    tab.addTab(Visualization(), "Visualization")
    return tab


class Tab(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_components()

    def ui_components(self):
        layout = QHBoxLayout(self)
        layout.addWidget(tab_division())
        self.setLayout(layout)
