from PyQt5.QtWidgets import *
from source.view.components.icon import Icon
from PyQt5 import QtCore


class ProjectToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.filtered_graphs_label = QLabel("  Graph at \n selected file")
        self.features_info_label = QLabel(" Graph editing \n features")

        self.left_button = QPushButton()
        self.right_button = QPushButton()
        self.features_info_button = QAction()
        self.refresh_button = QAction()
        self.graph_button = QAction()
        self.save_button = QAction()
        self.delete_button = QAction()
        self.revert_button = QAction()
        self.forward_button = QAction()

        self.operations_menu_bar = QMenuBar()
        self.insert_menu_bar = QMenuBar()

        self.line_graph = QAction("Line Graph")
        self.inverse_line_graph = QAction("Inverse Line Graph")
        self.complement = QAction("Complement")
        self.clique_graph = QAction("Clique Graph")

        self.cycle_graph_button = QAction("Cycle Graph")

        self.create_menu_bar()

        self.combo_graphs = QComboBox()
        self.combo_operations = QComboBox()

        self.current_graph = None

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.layout().setSpacing(15)
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

        self.addWidget(self.operations_menu_bar)
        self.addWidget(self.insert_menu_bar)
        self.addSeparator()

        self.addAction(self.graph_button)
        self.addAction(self.save_button)
        self.addAction(self.delete_button)
        self.addAction(self.revert_button)
        self.addAction(self.forward_button)

    def create_menu_bar(self):
        self.operations_menu_bar.setMaximumSize(95, 28)
        self.operations_menu_bar.setStyleSheet("background-color: none; font-size: 16px;"
                                               "border: 1px solid gray;")

        file_menu = QMenu("&Operations", self)
        self.operations_menu_bar.addMenu(file_menu)

        file_menu.addAction(self.line_graph)
        file_menu.addAction(self.inverse_line_graph)
        file_menu.addAction(self.complement)
        file_menu.addAction(self.clique_graph)

        self.insert_menu_bar.setMaximumSize(93, 28)
        self.insert_menu_bar.setStyleSheet("background-color: none; font-size: 16px;"
                                           "border: 1px solid gray;")

        self.file_insert_menu = QMenu("&Insert         ", self)
        self.insert_menu_bar.addMenu(self.file_insert_menu)

        self.file_insert_menu.addAction(self.cycle_graph_button)
        self.file_insert_menu.addAction("Cycle")

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


class EditingFeatures(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Information")

        self.tableWidget = QTableWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.verticalHeader().hide()

        self.tableWidget.setHorizontalHeaderLabels(["Keymap", "Function"])

        label_list = [" Insert or +", " Delete or -", " Control + Left-Click", " Left-Click", " Left-Click",
                      " Left-Click"]

        for i, label_item in enumerate(label_list):
            label = QLabel(label_item)
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 0, label)

        self.tableWidget.setCellWidget(0, 1, QLabel(" Insert a new node"))
        self.tableWidget.setCellWidget(1, 1, QLabel(" Delete a node"))
        self.tableWidget.setCellWidget(2, 1, QLabel(" Multiple nodes and or edges can "
                                                    "be selected by holding control while clicking"))
        self.tableWidget.setCellWidget(3, 1, QLabel(" Double clicking on two nodes"
                                                    " successively will create an edge between them"))
        self.tableWidget.setCellWidget(4, 1, QLabel(" Individual nodes and edges can"
                                                    " be selected using the left-click"))
        self.tableWidget.setCellWidget(5, 1, QLabel(" Selected plot elements can be dragged"
                                                    " around by holding left-click on a selected artist"))

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setMaximumHeight((self.tableWidget.rowHeight(0) * 7) - 5)
        self.tableWidget.setColumnWidth(0, 150)

    def set_up_layout(self):
        self.setMinimumSize(750, 250)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
