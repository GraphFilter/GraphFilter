from PyQt5.QtCore import QThread

from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication
import multiprocessing as mp

class FilterController(QThread):

    def __init__(self):
        super.__init__()
        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()
        self.is_running = True

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.graph_files)
        self.loading_window.set_maximum(len(g6_list))
        self.loading_window.show()
        if project_information_store.method == 'filter':
            single_process = mp.Process(target=self.filter_list.start_filter,
                                        args=(g6_list, project_information_store.equation,
                                          project_information_store.conditions,
                                          self.update,))
        else:
            single_process = mp.Process(target=self.filter_list.start_find_counterexample,
                                        args=(g6_list, project_information_store.equation,
                                          project_information_store.conditions,
                                          self.update,))
        single_process.start()

        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()
        # self.progress_window.close()

    def update(self):
        pass
         # self.progress_window.increase_step()
         # QApplication.processEvents()