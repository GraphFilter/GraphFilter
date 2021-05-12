from PyQt5.QtWidgets import *
from src.view.resources.components.icon import Icon
from PyQt5 import QtCore


class ProjectToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.filtered_graphs_label = QLabel("List of graphs filtered")

        self.left_button = QPushButton()
        self.right_button = QPushButton()

        self.combo_graphs = QComboBox()

        self.current_graph = None

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.layout().setSpacing(30)
        self.layout().setContentsMargins(15, 10, 20, 20)
        self.setMovable(False)

        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)
        self.combo_graphs.setMinimumWidth(200)

        self.right_button.setIcon(Icon("right_arrow_key"))
        self.right_button.setIconSize(QtCore.QSize(20, 20))
        self.right_button.setDisabled(False)

        self.left_button.setIcon(Icon("left_arrow_key"))
        self.left_button.setIconSize(QtCore.QSize(20, 20))
        self.left_button.setDisabled(True)

    def reset_combo_graphs(self):
        self.combo_graphs.clear()

    def set_up_layout(self):
        self.addWidget(self.filtered_graphs_label)
        self.addWidget(self.combo_graphs)
        self.addWidget(self.left_button)
        self.addWidget(self.right_button)

    def fill_combo_graphs(self, graphs):
        for i, line in enumerate(graphs):
            self.combo_graphs.addItem(f'Graph {i} - {line}')
        if self.combo_graphs.count() < 2:
            self.left_button.setDisabled(True)
            self.right_button.setDisabled(True)
        else:
            self.right_button.setDisabled(False)
        if len(graphs) == 0:
            return None

        return graphs[0]
