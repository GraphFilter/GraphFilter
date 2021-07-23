from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication


class FilterController:

    def __init__(self):

        self.filter_list = FilterList()
        self.loading_window = LoadingWindow(self.filter_list.total)

    def show_window(self):
        #self.loading_window.progressBar.setMaximum(self.filter_list.total)
        self.loading_window.show()

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.graph_files)
        self.filter_list.set_inputs(g6_list, project_information_store.equation, project_information_store.conditions,
                                    self.update)
        self.show_window()
        if project_information_store.method == 'filter':
            self.filter_list.run_filter()
        else:
            self.filter_list.run_find_counterexample()

        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()

        self.loading_window.close()

    def update(self):
        self.loading_window.increase_step()
        QApplication.processEvents()
