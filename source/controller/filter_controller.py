from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication


class FilterController:

    def __init__(self):

        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()

    def show_window(self):
        #self.loading_window.progressBar.setMaximum(self.filter_list.total)
        self.loading_window.show()

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.graph_files)
        self.loading_window.set_maximum(len(g6_list))
        self.show_window()
        if project_information_store.method == 'filter':
            self.filter_list.start_filter(g6_list, project_information_store.equation,
                                          project_information_store.conditions,
                                          self.update)
        else:
            self.filter_list.start_find_counterexample(g6_list, project_information_store.equation,
                                          project_information_store.conditions,
                                          self.update)

        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()

        self.loading_window.close()

    def update(self):
        self.loading_window.increase_step()
        # QApplication.processEvents()
