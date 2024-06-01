import os
from concurrent.futures import ProcessPoolExecutor
from typing import List

import networkx as nx
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal

from source.commons import save_nx_list_to_files
from source.view.windows.progress_window import ProgressConfigurations
from source.worker import ProgressLabels

NUMBER_CORES = int(np.ceil((1 / 3) * os.cpu_count()))


class FilterWorker(QThread):
    progress_signal = pyqtSignal(int, str, object)
    result_signal = pyqtSignal(list)

    def __init__(self, graphs_list: List[nx.Graph], method, parent, directory, file_name):
        super().__init__(parent)
        self.graphs_list = graphs_list
        self.method = method
        self.directory = directory
        self.file_name = file_name
        self.configurations = ProgressConfigurations(False, len(self.graphs_list) - 1)
        self.connect_signals()

    def connect_signals(self):
        self.progress_signal.connect(self.parent().update_progress)
        self.result_signal.connect(self.parent().finish.emit)
        self.parent().canceled.connect(self.terminate)

    def run(self):
        with ProcessPoolExecutor(max_workers=NUMBER_CORES) as executor:
            for step, graph in enumerate(executor.map(self.method.validate_graph,
                                                      self.graphs_list,
                                                      chunksize=self.get_chunk_size())):
                self.progress_signal.emit(step, ProgressLabels.FILTERING, self.configurations)
                if graph:
                    self.method.execute(graph)
                if self.method.was_finalized:
                    self.progress_signal.emit(len(self.graphs_list) - 1, "", self.configurations)
                    break

            list_graphs = self.method.finalize()
            save_nx_list_to_files(list_graphs, self.directory, self.file_name)
            self.result_signal.emit(list_graphs)

    def get_chunk_size(self):
        return int(len(self.graphs_list) / NUMBER_CORES)
