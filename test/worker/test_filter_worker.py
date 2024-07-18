import unittest
from concurrent.futures import ProcessPoolExecutor
from unittest.mock import patch
from PyQt6.QtCore import QObject, pyqtSignal
import networkx as nx

from source.domain.entities import BooleanStructuralInvariants
from source.worker.filter_worker import FilterWorker
from source.domain.filter import Filter
import random


def graphs_are_equal(graph1, graph2):
    return (set(graph1.nodes) == set(graph2.nodes) and
            set(graph1.edges) == set(graph2.edges))


def graph_lists_are_equal(graph_list1, graph_list2):
    if len(graph_list1) != len(graph_list2):
        return False

    for graph1 in graph_list1:
        if not any(graphs_are_equal(graph1, graph2) for graph2 in graph_list2):
            return False

    for graph2 in graph_list2:
        if not any(graphs_are_equal(graph1, graph2) for graph1 in graph_list1):
            return False

    return True


def generate_random_graphs(total_graphs):
    num_large = total_graphs // 4
    num_small = total_graphs - num_large

    def generate_planar_graph(num_vertices):
        if num_vertices <= 4:
            return nx.complete_graph(num_vertices)
        size = int(num_vertices ** 0.5)
        return nx.grid_2d_graph(size, size) if size > 1 else nx.complete_graph(num_vertices)

    def generate_non_planar_graph(num_vertices):
        return nx.erdos_renyi_graph(num_vertices, random.uniform(0.1, 0.5))

    graphs = []
    for _ in range(num_large):
        num_vertices = random.randint(6, 10)
        G = generate_planar_graph(num_vertices) if random.choice([True, False]) else generate_non_planar_graph(
            num_vertices)
        graphs.append(G)

    for _ in range(num_small):
        num_vertices = random.randint(1, 5)
        G = generate_planar_graph(num_vertices) if random.choice([True, False]) else generate_non_planar_graph(
            num_vertices)
        graphs.append(G)

    return graphs


def filter_graphs_by_vertices(graphs, min_vertices):
    return [G for G in graphs if len(G.nodes) > min_vertices]


def filter_planar_graphs(graphs):
    return [G for G in graphs if nx.check_planarity(G)[0]]


def filter_large_and_planar_graphs(graphs, min_vertices):
    return [G for G in graphs if len(G.nodes) > min_vertices and nx.check_planarity(G)[0]]


class MockQObject(QObject):
    canceled = pyqtSignal()
    finish = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_graphs = []
        self.finish.connect(self.set_output_graphs)

    def update_progress(self):
        pass

    def set_output_graphs(self, output_graphs):
        self.output_graphs = output_graphs


class TestFilterWorker(unittest.TestCase):

    def setUp(self):
        self.graphs_list = generate_random_graphs(100)
        self.parent = MockQObject()
        self.method = Filter()
        self.worker = FilterWorker(self.graphs_list, self.method, self.parent)

    @patch('source.worker.filter_worker.ProcessPoolExecutor', wraps=ProcessPoolExecutor)
    def test_filter_worker_with_equation(self, MockExecutor):
        filtered_graphs = filter_graphs_by_vertices(self.graphs_list, 5)
        self.method.set_attributes("N(G) > 5", None)
        self.worker.run()
        self.assertTrue(graph_lists_are_equal(filtered_graphs, self.parent.output_graphs))

    @patch('source.worker.filter_worker.ProcessPoolExecutor', wraps=ProcessPoolExecutor)
    def test_filter_worker_with_conditions(self, MockExecutor):
        self.method.set_attributes("", {BooleanStructuralInvariants.Planar(): True})
        filtered_graphs = filter_planar_graphs(self.graphs_list)
        self.worker.run()
        self.assertTrue(graph_lists_are_equal(filtered_graphs, self.parent.output_graphs))

    @patch('source.worker.filter_worker.ProcessPoolExecutor', wraps=ProcessPoolExecutor)
    def test_filter_worker_with_equations_and_conditions(self, MockExecutor):
        self.method.set_attributes("N(G) > 5", {BooleanStructuralInvariants.Planar(): True})
        filtered_graphs = filter_large_and_planar_graphs(self.graphs_list, 5)
        self.worker.run()
        self.assertTrue(graph_lists_are_equal(filtered_graphs, self.parent.output_graphs))


if __name__ == '__main__':
    unittest.main()
