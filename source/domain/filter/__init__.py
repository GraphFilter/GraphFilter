import os
from abc import ABC, abstractmethod
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import Dict, List, Set

import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

from source.commons.objects.translation_object import TranslationObject
from source.domain.boolean_expression_solver import Properties, BooleanExpressionSolver
from source.domain.entities import Invariant
import networkx as nx

NUMBER_CORES = int(np.ceil((1 / 3) * os.cpu_count()))


class GraphWorker(QThread):
    progress_signal = pyqtSignal(int)
    result_signal = pyqtSignal(list)

    def __init__(self,
                 graphs_list: List[nx.Graph],
                 update_progress=None,
                 equation: str = None,
                 conditions: Dict[bool, Set[Invariant]] = None):
        super().__init__()
        self.graphs_list = graphs_list
        self.was_canceled = False
        self.equation = equation
        self.conditions = conditions

    def run(self):
        filter_part = partial(_validate_graph, self.equation, self.conditions)

        print("Comecando filtragem")
        with ProcessPoolExecutor(max_workers=NUMBER_CORES) as executor:
            for step, graph in enumerate(executor.map(filter_part, self.graphs_list)):
                print("buceta dentro")
                self.progress_signal.emit(step)
                QApplication.processEvents()
                if graph:
                    Filter().execute(graph)
                if self.was_canceled:
                    break

        self.result_signal.emit([])
        # return Filter().finalize(self.update_progress)


def _validate_graph(equation: str, conditions: Dict[bool, Invariant], graph: nx.Graph) -> nx.Graph | None:
    print("buceta")
    if _validate_equation(graph, equation) and _validate_conditions(graph, conditions):
        return graph
    else:
        return None


def _validate_equation(graph: nx.Graph, equation: str) -> bool:
    return BooleanExpressionSolver(equation, Properties(names={"G": graph, "g": graph})).solver()


def _validate_conditions(graph: nx.Graph, conditions: dict) -> bool:
    if conditions is None:
        return True
    for invariant, selected in conditions.items():
        return invariant.calculate(graph) == selected


class GenericFilter(TranslationObject, ABC):
    update_signal = QtCore.pyqtSignal(int, str)

    def __init__(self, name: str = ""):
        super().__init__(name=name)
        self.update_progress = None
        self.was_canceled = False
        self.graphs_output_list = []

    def set_was_canceled(self, was_canceled):
        self.was_canceled = was_canceled

    def process_manager(self,
                        graphs_list: List[nx.Graph],
                        update_progress=None,
                        equation: str = None,
                        finaliza=None,
                        conditions: Dict[bool, Set[Invariant]] = None):
        self.update_progress = update_progress
        self.worker = GraphWorker(graphs_list, update_progress, equation, conditions)
        self.worker.result_signal.connect(finaliza)
        self.worker.progress_signal.connect(update_progress)
        self.worker.start()
        print("process_manager")
        # filter_part = partial(_validate_graph, equation, conditions, update_progress)
        #
        # with ProcessPoolExecutor(max_workers=NUMBER_CORES) as executor:
        #     for step, graph in enumerate(executor.map(filter_part, graphs_list)):
        #         # update_progress(step, "Filtering...")
        #         if graph:
        #             self.execute(graph)
        #         if self.was_canceled:
        #             break
        #
        # return self.finalize(update_progress)

    @abstractmethod
    def execute(self, graph):
        pass

    @abstractmethod
    def finalize(self, update_progress):
        return None


class Filter(GenericFilter):
    def __init__(self, name: str = "Filter"):
        super().__init__(name=name)
        self.was_canceled = False

    def execute(self, graph):
        self.graphs_output_list.append(graph)

    def finalize(self, update_progress):
        return self.graphs_output_list


class FindAnExample(GenericFilter):
    def __init__(self):
        super().__init__("Find an Example")

    def execute(self, graph):
        self.graphs_output_list.append(graph)
        self.was_canceled = True

    def finalize(self, update_progress):
        update_progress(-1)
        return self.graphs_output_list[0]
