import unittest
import networkx as nx

from source.domain.entities import BooleanStructuralInvariants
from source.domain.filter import Filter, FindAnExample


class TestFilter(unittest.TestCase):
    def setUp(self):
        self.graph1 = nx.petersen_graph()
        self.graph2 = nx.tetrahedral_graph()
        self.graph3 = nx.complete_graph(5)
        self.graph4 = nx.complete_graph(7)
        self.graphs = [self.graph1, self.graph2, self.graph3, self.graph4]

    def test_filter_with_equation(self):
        equation = "n(G) < 7"
        filter_obj = Filter(self.graphs, equation=equation)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, [self.graph2, self.graph3])

    def test_filter_with_conditions(self):
        conditions = {True: {BooleanStructuralInvariants.Planar()}}
        filter_obj = Filter(self.graphs, conditions=conditions)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, [self.graph2])

    def test_filter_with_equation_and_conditions(self):
        equation = "n(G) < 7"
        conditions = {True: {BooleanStructuralInvariants.Planar()}}
        filter_obj = Filter(self.graphs, equation, conditions)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, [self.graph2])

    def test_find_an_example_with_equation(self):
        equation = "n(G) < 7"
        filter_obj = FindAnExample(self.graphs, equation=equation)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, self.graph2)

    def test_find_an_example_with_conditions(self):
        conditions = {False: {BooleanStructuralInvariants.Planar()}}
        filter_obj = FindAnExample(self.graphs, conditions=conditions)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, self.graph1)

    def test_find_an_example_with_equation_and_conditions(self):
        equation = "n(G) < 7"
        conditions = {False: {BooleanStructuralInvariants.Planar()}}
        filter_obj = FindAnExample(self.graphs, equation, conditions)

        filtered_graphs = filter_obj.filter()
        self.assertEqual(filtered_graphs, self.graph3)


if __name__ == "__main__":
    unittest.main()
