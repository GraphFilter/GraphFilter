from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication
from time import sleep
import threading as td


class FilterController:

    def __init__(self):
        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()
        self.is_running = True

    def start_filter(self):
        g6_list = extract_files_to_list(project_information_store.graph_files)
        self.loading_window.set_maximum(100)
        self.loading_window.show()

        if project_information_store.method == 'filter':
            single_process = td.Thread(target=self.filter_list.start_filter,
                                       args=(g6_list, project_information_store.equation,
                                             project_information_store.conditions,
                                             self.update(0),))
        else:
            single_process = td.Thread(target=self.filter_list.start_find_counterexample,
                                       args=(g6_list, project_information_store.equation,
                                             project_information_store.conditions,
                                             self.update(0)))
        single_process.start()
        while self.is_running:
            valor = int(((self.filter_list.valor_teste.value / len(g6_list)) * 100) + 1)
            self.update(valor)
            if valor == 100:
                self.is_running = False

            if valor == 101:
                self.is_running = False

        sleep(2)
        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = self.filter_list.list_out
        project_information_store.save_project()
        self.loading_window.close()

    def update(self, valor):
        self.loading_window.increase_step(valor)
        QApplication.processEvents()
