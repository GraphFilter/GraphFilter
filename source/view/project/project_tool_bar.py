from PyQt5.QtWidgets import *
from source.view.components.icon import Icon
from PyQt5 import QtCore


class ProjectToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.filtered_graphs_label = QLabel("  List of graphs filtered")

        self.left_button = QPushButton()
        self.right_button = QPushButton()
        self.features_info_button = QPushButton()
        self.refresh_button = QPushButton()
        self.graph_button = QPushButton()
        self.save_button = QPushButton()
        self.delete_button = QPushButton()
        self.revert_button = QPushButton()
        self.forward_button = QPushButton()

        self.combo_graphs = QComboBox()
        self.combo_operations = QComboBox()

        self.current_graph = None

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.layout().setSpacing(35)
        self.layout().setContentsMargins(15, 10, 20, 20)
        self.setMinimumHeight(45)
        self.setMovable(False)

        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)
        self.combo_graphs.setMinimumWidth(200)

        self.features_info_button.setText(" Graph editing features")
        self.features_info_button.setIcon(Icon("help"))
        self.features_info_button.setIconSize(QtCore.QSize(20, 20))

        self.right_button.setIcon(Icon("right_arrow_key"))
        self.right_button.setIconSize(QtCore.QSize(20, 20))
        self.right_button.setDisabled(False)

        self.left_button.setIcon(Icon("left_arrow_key"))
        self.left_button.setIconSize(QtCore.QSize(20, 20))
        self.left_button.setDisabled(True)

        self.refresh_button.setIcon(Icon("refresh"))
        self.refresh_button.setIconSize(QtCore.QSize(20, 20))

        self.graph_button.setIcon(Icon("graph"))
        self.graph_button.setIconSize(QtCore.QSize(20, 20))

        self.save_button.setIcon(Icon("save"))
        self.save_button.setIconSize(QtCore.QSize(20, 20))

        self.delete_button.setIcon(Icon("delete"))
        self.delete_button.setIconSize(QtCore.QSize(20, 20))

        self.revert_button.setIcon(Icon("revert"))
        self.revert_button.setIconSize(QtCore.QSize(20, 20))

        self.forward_button.setIcon(Icon("forward"))
        self.forward_button.setIconSize(QtCore.QSize(20, 20))
        self.forward_button.setDisabled(True)

    def reset_combo_graphs(self):
        self.combo_graphs.clear()

    def set_up_layout(self):
        self.addWidget(self.features_info_button)
        self.addSeparator()

        self.addWidget(self.filtered_graphs_label)
        self.addWidget(self.combo_graphs)
        self.addWidget(self.left_button)
        self.addWidget(self.right_button)
        self.addSeparator()

        self.addWidget(self.refresh_button)
        self.addWidget(self.combo_operations)
        self.addSeparator()

        self.addWidget(self.graph_button)
        self.addWidget(self.save_button)
        self.addWidget(self.delete_button)
        self.addSeparator()

        self.addWidget(self.revert_button)
        self.addWidget(self.forward_button)

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
