from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from typing import List
from PyQt6.QtCore import QThread, pyqtSignal
from source.view.windows.progress_window import ProgressConfigurations
from source.worker import ProgressLabels
import networkx as nx
import numpy as np
import os

NUMBER_CORES = int(np.ceil((1 / 3) * os.cpu_count()))


class FilterWorker(QThread):
    progress_signal = pyqtSignal(int, str, object)
    result_signal = pyqtSignal(list)

    def __init__(self, graphs_list: List[nx.Graph], method, parent):
        super().__init__(parent)
        self.graphs_list = graphs_list
        self.method = method
        self.configurations = ProgressConfigurations(False, len(self.graphs_list) - 1)
        self.executor = None
        self.connect_signals()

    def connect_signals(self):
        self.progress_signal.connect(self.parent().update_progress)
        self.result_signal.connect(self.parent().finish.emit)
        self.parent().canceled.connect(self.terminate)

    def run(self):
        self.executor = ProcessPoolExecutor(max_workers=NUMBER_CORES)
        try:
            futures = [
                self.executor.submit(self.method.validate_graph, graph)
                for graph in self.graphs_list
            ]
            for step, future in enumerate(wait(futures, return_when=ALL_COMPLETED).done):
                graph = future.result()
                self.progress_signal.emit(step, ProgressLabels.FILTERING, self.configurations)
                if graph:
                    self.method.execute(graph)
                if self.method.was_finalized:
                    self.progress_signal.emit(len(self.graphs_list) - 1, "", self.configurations)
                    break

            self.result_signal.emit(self.method.finalize())
        finally:
            self.executor.shutdown(wait=True)

    def terminate(self):
        if self.executor:
            self.executor.shutdown(wait=False)
        super().terminate()

    def get_chunk_size(self):
        return int(len(self.graphs_list) / NUMBER_CORES)
