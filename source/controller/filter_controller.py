from source.domain.filter_list import FilterList
from source.domain.utils import *
from source.store.project_information_store import project_information_store
from source.view.loading.loading_window import LoadingWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from source.controller.project_controller import ProjectController

class FilterController(QObject):

    def __init__(self):
        super().__init__()

        self.loading_window = LoadingWindow()

        self.project_controller = ProjectController()
        # self.thread.finished.connect(self.thread.deleteLater)

    def show_loading_window(self):
        self.loading_window.show()

    def run_worker(self):
        self.loading_window.progressBar.setMaximum(len(extract_files_to_list(project_information_store.graph_files)))
        self.show_loading_window()
        # self.thread = QThread()
        # self.worker = Worker()
        # self.worker.moveToThread(self.thread)
        #
        # self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(lambda: self.show_project_contrtoller(self))
        # self.worker.progress.connect(self.reportProgress)

        self.thread = Worker()
        self.thread.finished.connect(self.show_project_contrtoller)
        self.thread.start()

        # self.project_controller = ProjectController()
        # self.project_controller.show_window()
        # self.loading_window.close()



    def show_project_contrtoller(self):
        self.loading_window.close()
        self.project_controller.show_window()
        self.thread.deleteLater()


class Worker(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        filter_list = FilterList()
        g6_list = extract_files_to_list(project_information_store.graph_files)
        if project_information_store.method == 'filter':
            filter_list.start_filter(g6_list,
                                     project_information_store.equation,
                                     project_information_store.conditions,
                                     self.update)
        else:
            filter_list.start_find_counterexample(g6_list,
                                                  project_information_store.equation,
                                                  project_information_store.conditions,
                                                  self.update)

        # TODO: Use the percentage returned by filtering
        project_information_store.filtered_graphs = filter_list.list_out
        project_information_store.save_project()
        self.finished.emit()
    # filter_controller.thread.quit()

    def update(self):
        pass

# def update(filter_controller):
#     filter_controller.loading_window.increase_step()
#     QApplication.processEvents()



