from src.view.project.visualize.visualize import Visualize
from src.view.project.project_content_dictionary import Dictionary
from src.view.project.docks.graph_information_dock import Info
from src.view.project.docks.visualize_graph_dock import Graph
from src.view.project.docks.invariants_checks_dock import Invariants
# NOTE: about should export an about window
#  from import src.view.windows.project.about.about import About


class ProjectController:
    def __init__(self, project):
        self.project = project
        self.visualize = Visualize()  # NOTE: Probably Visualize wont be needed anymore
        self.dictionary = Dictionary()

        self.info_dock = Info()
        self.graph_dock = Graph()
        self.invariants_dock = Invariants()

        # NOTE: need to create a file tool_bar
        #  self.tool_bar = ToolBar()

        # NOTE: need to create a file to about
        #  self.about = About()

    def connect_project_window_menu_actions(self):
        pass

    # menu bar actions
    def on_exit(self):
        pass

    def on_print(self):
        pass

    def on_visualize(self):
        pass

    def on_dictionary(self):
        pass

    def on_about(self):
        pass

    def on_restore(self):
        pass


