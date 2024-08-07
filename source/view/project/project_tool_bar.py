
from PyQt5.QtWidgets import *

from source.store.export_graph_to import dict_name_export_graph_to
from source.store.operations_graph import dict_name_operations_graph
from source.view.components.image import Icon
from source.store.new_graph_store import *
from PyQt5 import QtCore


class ProjectToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.filtered_graphs_label = QLabel("  File \n selected file")
        self.features_info_label = QLabel(" Graph editing \n features")

        self.left_button = QPushButton()
        self.right_button = QPushButton()
        self.features_info_button = QAction()
        self.refresh_button = QAction()
        self.universal_vertex_button = QPushButton()
        self.save_button = QAction()
        self.delete_button = QAction()
        self.revert_button = QAction()
        self.forward_button = QAction()

        self.operations_menu_bar = QPushButton()
        self.new_graph_menu_bar = QPushButton()
        self.export_menu_bar = QPushButton()
        self.operations_menu = QMenu(self)
        self.new_graph_menu = QMenu(self)
        self.export_menu = QMenu(self)

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
        self.features_info_button.setToolTip('View graph editing features')

        self.right_button.setIcon(Icon("right_arrow_key"))
        self.right_button.setToolTip('Go to next graph')
        self.right_button.setIconSize(QtCore.QSize(20, 20))
        self.right_button.setDisabled(False)
        self.right_button.setStyleSheet("background-color: #DCDCDC;"
                                        "border-radius: 10px;")

        self.left_button.setIcon(Icon("left_arrow_key"))
        self.left_button.setToolTip('Go to previous graph')
        self.left_button.setIconSize(QtCore.QSize(20, 20))
        self.left_button.setDisabled(True)
        self.left_button.setStyleSheet("background-color: #DCDCDC;"
                                       "border-radius: 10px;")

        self.refresh_button.setIcon(Icon("refresh"))
        self.combo_operations.addItem(" Operations")

        self.universal_vertex_button.setIcon(Icon("universal_vertex"))
        self.universal_vertex_button.setIconSize(QtCore.QSize(35, 35))
        self.set_button_style(self.universal_vertex_button)

        self.universal_vertex_button.setToolTip('Insert an universal vertex')

        self.save_button.setIcon(Icon("save"))
        self.save_button.setToolTip('Save current graph changes')
        self.delete_button.setIcon(Icon("delete"))
        self.delete_button.setToolTip('Erase current graph. \nIn a list (g6), will remove the current graph')

        self.operations_menu_bar.setIcon(Icon("operations"))
        self.operations_menu_bar.setToolTip('Apply operation on the current graph')
        self.operations_menu_bar.setIconSize(QtCore.QSize(45, 45))
        self.set_button_style(self.operations_menu_bar)

        self.new_graph_menu_bar.setIcon(Icon("new_graph"))
        self.new_graph_menu_bar.setToolTip('Create a new graph')
        self.new_graph_menu_bar.setIconSize(QtCore.QSize(35, 35))
        self.set_button_style(self.new_graph_menu_bar)

        self.export_menu_bar.setIcon(Icon("export"))
        self.export_menu_bar.setToolTip('Export the current graph')
        self.export_menu_bar.setIconSize(QtCore.QSize(30, 30))
        self.set_button_style(self.export_menu_bar)

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
        self.addWidget(self.universal_vertex_button)
        self.addSeparator()

        self.addWidget(self.new_graph_menu_bar)
        self.addAction(self.save_button)
        self.addAction(self.delete_button)
        self.addWidget(self.export_menu_bar)

    def create_menu_bar(self):
        self.operations_menu_bar.setStyleSheet("background-color: none; border: none; margin-left: -10px;")
        self.new_graph_menu_bar.setStyleSheet("background-color: none; border: none; margin-left: -10px;")
        self.export_menu_bar.setStyleSheet("background-color: none; border: none; margin-left: -10px;")

        self.operations_menu_bar.setMenu(self.operations_menu)
        self.new_graph_menu_bar.setMenu(self.new_graph_menu)
        self.export_menu_bar.setMenu(self.export_menu)

        for operation in dict_name_operations_graph:
            self.operations_menu.addAction(operation)

        for new_graph in new_graph_dict_name:
            self.new_graph_menu.addAction(new_graph)

        for formats in dict_name_export_graph_to:
            self.export_menu.addAction(formats)

    def fill_combo_graphs(self, graphs):
        for i, line in enumerate(graphs):
            self.combo_graphs.addItem(f'Graph {i + 1} - {line}')
        if self.combo_graphs.count() < 2:
            self.left_button.setDisabled(True)
            self.right_button.setDisabled(True)
        else:
            self.right_button.setDisabled(False)
        if len(graphs) == 0:
            return None

        return graphs[0]

    def set_file_label(self, file_name):
        self.filtered_graphs_label.setFixedWidth(75)
        self.filtered_graphs_label.setText(f"      File \n {file_name}")
        self.filtered_graphs_label.setToolTip(f"{file_name}")

    @staticmethod
    def set_button_style(button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; 
                border: 0px;
            }
            QPushButton:hover {
                background-color:rgba(135,206,250, 0.2);
            }
        """)


class EditingFeatures(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Information")

        self.tableWidget = QTableWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.verticalHeader().hide()

        self.tableWidget.setHorizontalHeaderLabels(["Keymap", "Function"])

        label_list = [" Insert or + or =", " Delete or - or Backspace", " Control + Left-Click", " Left-Click",
                      " Left-Click", " Left-Click", "Hold and drag left-click"]

        for i, label_item in enumerate(label_list):
            label = QLabel(label_item)
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 0, label)

        self.tableWidget.setCellWidget(0, 1, QLabel(" Insert a new node (this will be adjacent to previously"
                                                    " selected vertices)"))
        self.tableWidget.setCellWidget(1, 1, QLabel(" Delete a node"))
        self.tableWidget.setCellWidget(2, 1, QLabel(" Multiple nodes and or edges can "
                                                    "be selected by holding control while clicking"))
        self.tableWidget.setCellWidget(3, 1, QLabel(" Double clicking on two nodes"
                                                    " successively will create an edge between them"))
        self.tableWidget.setCellWidget(4, 1, QLabel(" Individual nodes and edges can"
                                                    " be selected using the left-click"))
        self.tableWidget.setCellWidget(5, 1, QLabel(" Selected plot elements can be dragged"
                                                    " around by holding left-click on a selected artist"))
        self.tableWidget.setCellWidget(6, 1, QLabel("Select multiple edges and vertices"))

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setMaximumHeight((self.tableWidget.rowHeight(0) * 8) - 5)
        self.tableWidget.setColumnWidth(0, 150)

    def set_up_layout(self):
        self.setMinimumSize(750, 300)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
