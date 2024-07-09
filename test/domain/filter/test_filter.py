import unittest
from concurrent.futures import ProcessPoolExecutor
from unittest.mock import patch, MagicMock
import networkx as nx

from source.domain.filter import Filter


class TestGraphProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = Filter()
        self.graphs_list = [nx.erdos_renyi_graph(10, 0.5) for _ in range(100000)]

    @patch('source.worker.filter.ProcessPoolExecutor', wraps=ProcessPoolExecutor)
    def test_process_manager(self, MockExecutor):

        result = self.processor.process(self.graphs_list, )

        # Verifica o resultado final
        self.assertEqual(result, "finalizado")

    def test_validate_graph(self):
        graph = self.graphs_list[0]
        result = self.processor._validate_graph(None, None, graph)
        self.assertEqual(graph, result)  # Supondo que a função retorna o mesmo grafo

if __name__ == "__main__":
    unittest.main()
