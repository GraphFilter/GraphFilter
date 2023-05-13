from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication
import threading as td


class FilterController:

    def __init__(self):
        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()
        self.is_running = True

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.temp_graph_input_files)
        self.loading_window.set_maximum(100)
        self.loading_window.show()

        if project_information_store.temp_method == 'filter':
            single_thread = td.Thread(target=self.filter_list.start_filter,
                                      args=(g6_list, project_information_store.temp_equation,
                                            project_information_store.temp_conditions,))
        else:
            single_thread = td.Thread(target=self.filter_list.start_find_counterexample,
                                      args=(g6_list, project_information_store.temp_equation,
                                            project_information_store.temp_conditions))
        single_thread.start()
        while self.is_running:
            value = int(((self.filter_list.update_to_progress_bar.value / len(g6_list)) * 100))
            self.update(value)
            if value == 100:
                self.is_running = False

        single_thread.join()
        # TODO: Use the percentage returned by filtering
        project_information_store.temp_filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()
        self.loading_window.close()

    def update(self, value):
        self.loading_window.increase_step(value)
        QApplication.processEvents()
