from PyQt6.QtCore import QThread, pyqtSignal, QObject

from source.commons import extract_files_to_nx_list
from source.worker import ProgressLabels


class ExtractGraphs(QThread):
    result_signal = pyqtSignal(list, object)
    start_signal = pyqtSignal(str)

    def __init__(self, files: list[str], parent_window: QObject, finalize_method):
        super().__init__(parent_window)
        self.files = files
        self.finalize_method = finalize_method
        self.connect_signals()

    def connect_signals(self):
        self.result_signal.connect(self.finalize_method)
        self.start_signal.connect(self.parent().setLabelText)

    def run(self):
        self.start_signal.emit(ProgressLabels.EXTRACT_GRAPHS)
        list_graphs = extract_files_to_nx_list(self.files)
        self.result_signal.emit(list_graphs, self.parent())
