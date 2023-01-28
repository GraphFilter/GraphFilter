from PyQt5.QtWidgets import *
from source.view.components.icon import Icon
from PyQt5 import QtCore


class ProjectToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.filtered_graphs_label = QLabel("  List of graphs filtered")
        self.features_info_label = QLabel(" Graph editing features")

        self.left_button = QPushButton()
        self.right_button = QPushButton()
        self.features_info_button = QAction()
        self.refresh_button = QAction()
        self.graph_button = QAction()
        self.save_button = QAction()
        self.delete_button = QAction()
        self.revert_button = QAction()
        self.forward_button = QAction()

        self.combo_graphs = QComboBox()
        self.combo_operations = QComboBox()

        self.current_graph = None

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.layout().setSpacing(30)
        self.layout().setContentsMargins(15, 10, 20, 20)
        self.setMinimumHeight(45)
        self.setMovable(False)

        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)
        self.combo_graphs.setMinimumWidth(200)

        self.features_info_button.setIcon(Icon("help"))

        self.right_button.setIcon(Icon("right_arrow_key"))
        self.right_button.setIconSize(QtCore.QSize(20, 20))
        self.right_button.setDisabled(False)
        self.right_button.setStyleSheet("background-color: #DCDCDC;"
                                        "border-radius: 10px;")

        self.left_button.setIcon(Icon("left_arrow_key"))
        self.left_button.setIconSize(QtCore.QSize(20, 20))
        self.left_button.setDisabled(True)
        self.left_button.setStyleSheet("background-color: #DCDCDC;"
                                       "border-radius: 10px;")

        self.refresh_button.setIcon(Icon("refresh"))
        self.combo_operations.addItem(" Operations")

        self.graph_button.setIcon(Icon("graph"))
        self.save_button.setIcon(Icon("save"))
        self.delete_button.setIcon(Icon("delete"))

        self.revert_button.setIcon(Icon("revert"))
        self.forward_button.setIcon(Icon("forward"))
        self.forward_button.setDisabled(True)

    def reset_combo_graphs(self):
        self.combo_graphs.clear()

    def set_up_layout(self):
        self.addAction(self.features_info_button)
        self.addWidget(self.features_info_label)
        self.addSeparator()

        self.addWidget(self.filtered_graphs_label)
        self.addWidget(self.left_button)
        self.addWidget(self.combo_graphs)
        self.addWidget(self.right_button)
        self.addSeparator()

        self.addAction(self.refresh_button)
        self.addWidget(self.combo_operations)
        self.addSeparator()

        self.addAction(self.graph_button)
        self.addAction(self.save_button)
        self.addAction(self.delete_button)
        self.addSeparator()

        self.addAction(self.revert_button)
        self.addAction(self.forward_button)

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


class EditingFeatures(QMessageBox):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Information")

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setText("Insert or + : Insert a new node\n\n"
                     "Delete or - : Delete a node \n\n"
                     "Control + Left-Click : Multiple nodes and or edges can"
                     " be selected by holding control while clicking \n\n"
                     "Left-Click: Double clicking on two nodes successively will create an edge between them \n\n"
                     "Left-Click: Individual nodes and edges can be selected using the left-click. \n\n"
                     "Left-Click: Selected plot elements can be dragged"
                     " around by holding left-click on a selected artist.")
