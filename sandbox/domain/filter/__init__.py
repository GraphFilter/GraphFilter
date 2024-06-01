import sys
import numpy as np
import networkx as nx
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from source.domain.filter import Filter
from source.view.windows.progress_window import ProgressWindow


class GraphWorker(QThread):
    result_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        print("Quebrando a lista")
        list_graphs = [self.create_random_graph() for _ in range(1000000)]
        self.result_signal.emit(list_graphs)

    def create_random_graph(self):
        n = np.random.randint(10, 20)
        p = np.random.uniform(0.1, 0.5)
        return nx.erdos_renyi_graph(n, p)


class ProgressOnlyWindow:
    def __init__(self):
        self.progress_window = ProgressWindow()
        self.worker = GraphWorker()
        self.worker.result_signal.connect(self.handle_results)
        self.first_time = True
        self.list_graphs = []

    def update_progress_window(self, value: int):
        print(value)
        if self.first_time:
            self.progress_window.progress_bar.setMinimum(0)
            self.progress_window.progress_bar.setMaximum(len(self.list_graphs))
            self.progress_window.progress_bar.setValue(value)
            self.first_time = False
        self.progress_window.progress_bar.setValue(value)
        # QApplication.processEvents()

    def handle_results(self, list_graphs):
        self.list_graphs = list_graphs
        filtered_graphs = Filter().process_manager(
            list_graphs,
            self.update_progress_window,
            "N(G) > 0",
            self.progress_window.close
        )
        # Handle the filtered graphs (e.g., store them, update UI, etc.)

    def show_progress_window(self):
        self.progress_window.show()
        QApplication.processEvents()

    def start_worker(self):
        self.worker.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    progress_only_window = ProgressOnlyWindow()
    progress_only_window.show_progress_window()
    progress_only_window.start_worker()
    sys.exit(app.exec_())
