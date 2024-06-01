from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

from source.commons import extract_files_to_nx_list
from source.view.windows.progress_window import ProgressWindow
from source.view.windows.project_window import ProjectWindow
from source.view.windows.welcome_window import WelcomeWindow
from source.view.windows.wizard_window import WizardWindow


class GraphWorker(QThread):
    result_signal = pyqtSignal(list)

    def __init__(self, files):
        super().__init__()
        self.files = files

    def run(self):
        print("Quebrando a lista")
        list_graphs = extract_files_to_nx_list(self.files)
        self.result_signal.emit(list_graphs)


class Controller:
    def __init__(self):
        self.welcome_window = WelcomeWindow()
        self.wizard_window = WizardWindow()
        self.project_window = ProjectWindow()
        self.progress_window = ProgressWindow()
        self.first_time = True
        self.list_graphs = []
        self.connect_events()

    def start(self):
        self.welcome_window.show()

    def connect_events(self):
        self.welcome_window.new_project.clicked.connect(self.show_wizard_window)
        self.wizard_window.cancel_button.clicked.connect(self.close_wizard_window)
        self.wizard_window.close_signal.connect(self.close_wizard_window)
        self.wizard_window.start_button.clicked.connect(self.start_filter)
        # self.progress_window.progress_bar.canceled.connect(self.cancel_filter)

    def close_wizard_window(self):
        self.wizard_window.close()
        self.wizard_window = WizardWindow()
        self.connect_events()
        self.welcome_window.show()

    def show_wizard_window(self):
        self.welcome_window.close()
        self.wizard_window.show()

    def start_filter(self):
        self.show_progress_window()
        self.worker = GraphWorker(self.wizard_window.field("files"))
        self.worker.result_signal.connect(self.start_process)
        self.worker.start()
        print("Processo principal")

        # filtered_graphs = self.wizard_window.field("method").process_manager(
        #     extract_files_to_nx_list(self.wizard_window.field("files")),
        #     self.update_progress_window,
        #     self.wizard_window.field("equation"),
        #     self.wizard_window.field("conditions"))
        # if filtered_graphs is not None:
        #     save_nx_list_to_files(filtered_graphs, self.wizard_window.field("location"), self.wizard_window.field("name"))
        #     self.show_project_window()

    def start_process(self, list_graphs):
        self.list_graphs = list_graphs
        filter_process = self.wizard_window.field("method").process_manager(list_graphs,
                                                                            self.update_progress_window,
                                                                            self.wizard_window.field("equation"),
                                                                            self.progress_window.close,
                                                                            self.wizard_window.field("conditions")
                                                                            )

    def show_progress_window(self):
        self.progress_window.show()
        QApplication.processEvents()

    def cancel_filter(self):
        self.wizard_window.field("method").set_was_canceled(True)
        self.wizard_window.show()

    def update_progress_window(self, value: int):
        print(value)
        if self.first_time:
            self.progress_window.progress_bar.setMinimum(0)
            self.progress_window.progress_bar.setMaximum(len(self.list_graphs))
            self.progress_window.progress_bar.setValue(value)
            self.first_time = False
        self.progress_window.progress_bar.setValue(value)
        # QApplication.processEvents()

    def show_project_window(self):
        self.project_window.showMaximized()
