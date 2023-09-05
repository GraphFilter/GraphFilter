from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.domain.utils_file import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication
import threading as td


class FilterController:

    def __init__(self):
        self.filter_list = None
        self.loading_window = None
        self.is_complete_filtering = False

    def start_filter(self):
        self.filter_list = FilterList()
        self.loading_window = LoadingWindow()
        g6_list = extract_files_to_list(project_information_store.temp_graph_input_files)
        number_input_graphs = len(g6_list)
        self.loading_window.set_maximum(100)
        self.loading_window.show()

        if project_information_store.temp_method == 'filter':
            single_thread = td.Thread(target=self.filter_list.start_filter,
                                      args=(g6_list, project_information_store.temp_equation,
                                            project_information_store.temp_conditions,))
        else:
            single_thread = td.Thread(target=self.filter_list.start_find_example,
                                      args=(g6_list, project_information_store.temp_equation,
                                            project_information_store.temp_conditions))
        single_thread.start()
        is_running = True
        while is_running:
            if self.loading_window.is_forced_to_close:
                self.filter_list.is_forced_to_terminate.value = 1.0
                single_thread.join()
                return
                # if len(multiprocessing.active_children()) == 0:
                #    print(multiprocessing.current_process())
                #    single_thread.join()
                #    return
            value = int(((self.filter_list.update_to_progress_bar.value / number_input_graphs) * 100))
            self.update(value)
            if value == 100:
                is_running = False

        self.is_complete_filtering = True
        single_thread.join()
        project_information_store.temp_filtered_graphs = self.filter_list.list_out
        generate_pdf_report(project_information_store.temp_project_name, project_information_store.temp_method,
                            project_information_store.temp_equation, project_information_store.temp_conditions,
                            project_information_store.temp_graph_input_files,
                            project_information_store.temp_filtered_graphs, '_report', number_input_graphs,
                            project_information_store.temp_project_description)

        create_g6_file(project_information_store.get_file_directory(),
                       project_information_store.temp_filtered_graphs,
                       project_information_store.temp_project_name, '_graphs')
        project_information_store.file_path = f'{project_information_store.get_file_directory()}/' \
                                              f'{project_information_store.temp_project_name}_graphs.g6'

        self.loading_window.close()

    def update(self, value):
        self.loading_window.increase_step(value)
        QApplication.processEvents()
