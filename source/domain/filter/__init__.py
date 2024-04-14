import networkx as nx
from source.commons.objects.translation_object import TranslationObject
from source.domain.boolean_expression_solver import Properties, BooleanExpressionSolver


class Filter(TranslationObject):
    def __init__(self,
                 graphs: list[nx.Graph] = None,
                 equation: str = None,
                 conditions: dict[bool, set] = None,
                 name: str = "Filter"
                 ):
        super().__init__(name=name)
        if conditions is None:
            conditions = {}
        self.graphs = graphs
        self.equation = equation
        self.conditions = conditions

    def filter(self) -> list[nx.Graph]:
        return [graph for graph in self.graphs if self._validate_equation(graph) and self._validate_conditions(graph)]

    def _validate_equation(self, graph: nx.Graph) -> bool:
        return BooleanExpressionSolver(self.equation, Properties(names={"G": graph, "g": graph})).solver()

    def _validate_conditions(self, graph: nx.Graph) -> bool:
        for condition, invariants_set in self.conditions.items():
            for invariant in invariants_set:
                if invariant.calculate(graph) != condition:
                    return False
        return True


class FindAnExample(Filter):
    def __init__(self,
                 graphs: list[nx.Graph] = None,
                 equation: str = None,
                 conditions: dict[bool, set] = None
                 ):
        super().__init__(graphs, equation, conditions, "Find an Example")

    def filter(self) -> nx.Graph:
        return next(
            (graph for graph in self.graphs if self._validate_equation(graph) and self._validate_conditions(graph)),
            None)

    # @staticmethod
    # def extract_files_to_list(files):
    #     list_g6 = []
    #     for file in files:
    #         if file.endswith('.gz'):
    #             file_unzipped = gzip.open(file, 'r')
    #             list_g6.extend([nx.from_graph6_bytes(graph.encode('utf-8')) for graph in
    #                             file_unzipped.read().decode('utf-8').splitlines()])
    #         else:
    #             list_g6.extend(open(file, 'r').read().splitlines())
    #     return list_g6
