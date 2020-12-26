from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import pathlib


class ProjectFiles(QWizardPage):

    def __init__(self):
        super().__init__()

        self.project_name_input = QLineEdit()
        self.project_name_input.returnPressed.connect(self.save_project_name)

        #  NOTE: this is to prevent user to click next without filling this input
        # self.registerField('project_name*', self.project_name_input)

        self.project_location_input = QLineEdit()
        self.project_location_input.setText(str(pathlib.Path().absolute()))

        project_location_button = QPushButton("...")
        project_location_button.clicked.connect(self.open_file)

        file_line = QHBoxLayout()
        file_line.addWidget(QLabel("Project location:"))
        file_line.addWidget(self.project_location_input)
        file_line.addWidget(project_location_button)

        form = QFormLayout()
        form.addRow(QLabel("Project Name:"), self.project_name_input)
        form.addRow(file_line)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.addLayout(form)
        layout.addStretch()

        # NOTE: this is for when we have two project options
        # draw_graph = QToolButton()
        # draw_graph.setIcon(QIcon("views/resources/icons/edit.png"))
        # draw_graph.setText("Draw Graph")
        # draw_graph.setMinimumHeight(100)
        # draw_graph.setMinimumWidth(100)
        # draw_graph.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # draw_graph.setIconSize(QtCore.QSize(40, 40))
        #
        # filter_graphs = QToolButton()
        # filter_graphs.setIcon(QIcon("views/resources/icons/filtro.png"))
        # filter_graphs.setText("New Project")
        # filter_graphs.setMinimumHeight(100)
        # filter_graphs.setMinimumWidth(100)
        # filter_graphs.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # filter_graphs.setIconSize(QtCore.QSize(40, 40))
        #
        # group_button = QHBoxLayout()
        # group_button.setSpacing(60)
        # group_button.setAlignment(QtCore.Qt.AlignCenter)
        # group_button.addWidget(draw_graph)
        # group_button.addWidget(filter_graphs)
        #
        # layout.addLayout(group_button)
        # layout.addStretch()

        self.setLayout(layout)

    def open_file(self):
        file_dialog = QFileDialog()
        directory_path = file_dialog.getExistingDirectory()
        self.project_location_input.setText(directory_path)

    def save_project_name(self):
        print(self.project_name_input.text())
