from PyQt5.QtWidgets import *
from source.view.components.icon import Icon
from source.domain.utils import set_view_size


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.icon = Icon("hexagon")

        self.width = 0
        self.height = 0
        set_view_size(self, 1.4)

        self.new_action = QAction("New Project")
        self.open_action = QAction("Open...")
        self.export_png_action = QAction("Image (.png)")
        self.export_pdf_action = QAction("Image (.pdf)")
        self.export_tikz_action = QAction("LaTeX Tikz (.tex)")
        self.export_g6_action = QAction("graph6 (.txt)")
        self.export_sheet_action = QAction("Sheet (.xlsx)")
        self.save_action = QAction("Save")

        # self.print_action = QAction(Icon("print"), "Print")
        self.exit_action = QAction("Exit")

        self.visualize_action = QAction("Visualize")
        self.invariants_check_action = QAction("Invariants Check")
        self.graph_info_action = QAction("Graph Info")
        self.visualize_tree_action = QAction("Files")

        self.dictionary_action = QAction("Dictionary")
        self.about_action = QAction("About...")

        self.restore_layout_action = QAction("Restore default layout")

        self.set_content_attributes()
        self.create_menu_bar()

    def set_content_attributes(self):
        self.setWindowIcon(self.icon)

        self.setMinimumSize(self.width, self.height)

    def set_title_bar(self, project_name):
        self.setWindowTitle(f"Graph Filter - {project_name}")

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addSeparator()

        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        view_menu = menu_bar.addMenu("&View")
        view_menu.addAction(self.visualize_action)
        view_menu.addAction(self.invariants_check_action)
        view_menu.addAction(self.graph_info_action)
        view_menu.addAction(self.visualize_tree_action)
        view_menu.addAction(self.restore_layout_action)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.dictionary_action)
        help_menu.addAction(self.about_action)
