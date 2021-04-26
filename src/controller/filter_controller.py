from src.domain.filter_list import FilterList
from src.controller.project_controller import ProjectController
from src.domain.utils import *
from src.store.project_information_store import project_information_store
from src.view.loading.loading_window import LoadingWindow


class FilterController():

    def __init__(self):

        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()
        self.project_controller = ProjectController()

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.graph_files)

        self.filter_list.set_inputs(g6_list, project_information_store.equation, project_information_store.conditions, self.update)
        self.show_window()
        if project_information_store.method == 'filter':
            self.filter_list.run_filter()
        else:
            self.filter_list.run_find_counterexample()

        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()

        self.loading_window.close()
        self.project_controller.show_window()

    def update(self, current_graph, total):
        self.loading_window.increase_step(current_graph / total)

    def show_window(self):
        self.loading_window.show()


