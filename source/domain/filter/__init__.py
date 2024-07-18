from abc import ABC, abstractmethod
from source.commons.objects.translation_object import TranslationObject
from source.worker.boolean_expression_solver import Properties, BooleanExpressionSolver
import networkx as nx

from source.worker.import_graphs_worker import ImportGraphsWorker
from source.worker.filter_worker import FilterWorker


class GenericFilter(TranslationObject, ABC):
    def __init__(self, name: str = ""):
        super().__init__(name=name)
        self.was_finalized = False
        self.equation = None
        self.conditions = None
        self.graphs_output_list = []

    def process(self, files: list[str], parent_window):
        extract_graphs = ImportGraphsWorker(files, parent_window, self.run)
        extract_graphs.start()

    def run(self, graphs_list, parent_window):
        worker = FilterWorker(graphs_list, self, parent_window)
        worker.start()

    def set_attributes(self, equation, conditions):
        self.equation = equation
        self.conditions = conditions

    def validate_graph(self, graph: nx.Graph):
        if self._validate_equation(graph) and self._validate_conditions(graph):
            return graph
        else:
            return None

    def _validate_equation(self, graph: nx.Graph) -> bool:
        return BooleanExpressionSolver(self.equation, Properties(names={"G": graph, "g": graph})).solver()

    def _validate_conditions(self, graph: nx.Graph) -> bool:
        if self.conditions is None:
            return True
        for invariant, selected in self.conditions.items():
            return invariant.calculate(graph) == selected

    @abstractmethod
    def execute(self, graph):
        pass

    def finalize(self):
        self.was_finalized = True
        return self.graphs_output_list


class Filter(GenericFilter):
    def __init__(self, name: str = "Filter"):
        super().__init__(name=name)

    def execute(self, graph):
        self.graphs_output_list.append(graph)


class FindAnExample(GenericFilter):
    def __init__(self):
        super().__init__("Find an Example")

    def execute(self, graph):
        self.graphs_output_list.append(graph)
        self.was_finalized = True
