import math
import os
import os.path

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

from source.domain.utils import validate_file_name, add_vertex
from source.view.components.new_graph_dialog import NewGraphDialog
from source.store.project_information_store import project_information_store
import networkx as nx


class NewGraphStore:
    name = None

    def __init__(self):
        self.all = NewGraphStore.__subclasses__()
        self.dic_name_new_graph: {str: NewGraphStore} = {}
        for new_graph in self.all:
            self.dic_name_new_graph[new_graph.name] = new_graph
        self.graph = None
        self.file_path = None
        self.layout = 'spring'
        self.radio_option = 0

    def set_graph(self, graph):
        self.graph = graph

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_radio_option(self, option):
        self.radio_option = option

    def set_layout(self, layout):
        self.layout = layout

    def reset_attributes(self):
        self.graph = None
        self.file_path = None
        self.layout = 'spring'
        self.radio_option = 0

    @staticmethod
    def open_url(url):
        QDesktopServices.openUrl(QUrl(url))

    @staticmethod
    def open_new_dialog(dialog):
        dialog.dict['name'].textEdited.connect(lambda: NewGraphStore.verify_file_name(dialog))
        dialog.new_file_radio.clicked.connect(lambda: NewGraphStore.verify_file_name(dialog))
        dialog.insert_final_radio.clicked.connect(lambda: NewGraphStore.verify_file_name(dialog))

        if os.path.isdir(project_information_store.file_path) or \
                project_information_store.get_file_type() in ['.gml', '.json']:
            dialog.insert_final_radio.setEnabled(False)

        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_file_path(project_information_store.get_file_directory() +
                                      f"{dialog.dict['name'].text()}.gml")

        dialog.close()

    @staticmethod
    def verify_file_name(dialog):
        new_graph_store.set_radio_option(1 if dialog.insert_final_radio.isChecked() else 0)
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if new_graph_store.radio_option == 1:
            dialog.create_button.setEnabled(True)
            dialog.dict['name'].setStyleSheet('background-color: white;')
            return
        if validate_file_name(dialog.dict['name'].text()):
            dialog.create_button.setEnabled(True)
            dialog.dict['name'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['name'].setStyleSheet('background-color: #EF5350;')

    @staticmethod
    def verify_natural_number(dialog, param, limit_max=60):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict[param].text().isnumeric() and 1 <= int(dialog.dict[param].text()) <= limit_max:
            dialog.create_button.setEnabled(True)
            dialog.dict[param].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict[param].setStyleSheet('background-color: #EF5350;')

    @staticmethod
    def verify_mxn_values(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict['m'].text().isnumeric() and dialog.dict['n'].text().isnumeric() and \
                1 <= (int(dialog.dict['m'].text()) * int(dialog.dict['n'].text())) <= 60:
            dialog.create_button.setEnabled(True)
            dialog.dict['m'].setStyleSheet('background-color: white;')
            dialog.dict['n'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['m'].setStyleSheet('background-color: #EF5350;')
            dialog.dict['n'].setStyleSheet('background-color: #EF5350;')

    @staticmethod
    def is_other_params_empty(dialog):
        if new_graph_store.radio_option == 0 and dialog.dict['name'] == "":
            return True
        for key, value in dialog.dict.items():
            if key != 'name' and value.text() == "":
                dialog.create_button.setDisabled(True)
                return True

        return False


class EmptyGraph(NewGraphStore):
    name = "Empty Graph"
    dict_attributes_names = {}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(EmptyGraph.dict_attributes_names, name=EmptyGraph.name)
        dialog.create_button.setEnabled(True)
        dialog.create_button.clicked.connect(lambda: EmptyGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Null_graph"))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.Graph())
        NewGraphStore.create_graph(dialog)


class GraphFromGraph6(NewGraphStore):
    name = "Graph from graph6"
    dict_attributes_names = {"g6": "Graph from g6", "conditions": "graph6 code"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(GraphFromGraph6.dict_attributes_names, name=GraphFromGraph6.name, g6='')
        dialog.create_button.clicked.connect(lambda: GraphFromGraph6.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("http://users.cecs.anu.edu.au/~bdm/data/formats.txt"))
        dialog.dict['g6'].textEdited.connect(lambda: GraphFromGraph6.reset_line_edit(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        try:
            new_graph_store.set_graph(nx.from_graph6_bytes(str(dialog.dict['g6'].text()).encode('utf-8')))
        except nx.NetworkXError:
            dialog.dict['g6'].setStyleSheet('background-color: #EF5350;')
            return

        NewGraphStore.create_graph(dialog)

    @staticmethod
    def reset_line_edit(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        dialog.create_button.setEnabled(True)
        dialog.dict['g6'].setStyleSheet('background-color: white;')


class CycleGraph(NewGraphStore):
    name = "Cycle Graph"
    dict_attributes_names = {"n": "Number of nodes, n", "conditions": "1 \u2264 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(CycleGraph.dict_attributes_names, name=CycleGraph.name, n='')
        dialog.create_button.clicked.connect(lambda: CycleGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Cycle_graph"))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_natural_number(dialog, 'n'))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.cycle_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_layout('circular')
        NewGraphStore.create_graph(dialog)


class PathGraph(NewGraphStore):
    name = "Path Graph"
    dict_attributes_names = {"n": "Number of nodes, n", "conditions": "1 \u2264 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(PathGraph.dict_attributes_names, name=PathGraph.name, n='')
        dialog.create_button.clicked.connect(lambda: PathGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Path_graph"))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_natural_number(dialog, 'n'))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.path_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_layout('circular')
        NewGraphStore.create_graph(dialog)


class CompleteGraph(NewGraphStore):
    name = "Complete Graph"
    dict_attributes_names = {"n": "Number of nodes, n", "conditions": "1 \u2264 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(CompleteGraph.dict_attributes_names, name=CompleteGraph.name, n='')
        dialog.create_button.clicked.connect(lambda: CompleteGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Complete_graph"))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_natural_number(dialog, 'n'))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.complete_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_layout('circular')
        NewGraphStore.create_graph(dialog)


class StarGraph(NewGraphStore):
    name = "Star Graph"
    dict_attributes_names = {"n": "Number of leaves, n", "conditions": "1 \u2264 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(StarGraph.dict_attributes_names, name=StarGraph.name, n='')
        dialog.create_button.clicked.connect(lambda: StarGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Star_(graph_theory)"))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_natural_number(dialog, 'n'))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.star_graph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class TuranGraph(NewGraphStore):
    name = "Turan Graph"
    dict_attributes_names = {"n": "Number of nodes, n", "r": "Number of subsets, r",
                             "conditions": "1 \u2264 r \u2264 n & 1 \u2264 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(TuranGraph.dict_attributes_names, name=TuranGraph.name, n='', r='')
        dialog.create_button.clicked.connect(lambda: TuranGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Turán_graph"))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_natural_number(dialog, 'n'))
        dialog.dict['n'].textEdited.connect(lambda: TuranGraph.verify_number_of_subsets(dialog))
        dialog.dict['r'].textEdited.connect(lambda: TuranGraph.verify_number_of_subsets(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.turan_graph(int(dialog.dict['n'].text()), int(dialog.dict['r'].text())))
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def verify_number_of_subsets(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict['r'].text().isnumeric() and dialog.dict['n'].text().isnumeric() and \
                0 < int(dialog.dict['r'].text()) <= int(dialog.dict['n'].text()):
            dialog.create_button.setEnabled(True)
            dialog.dict['r'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['r'].setStyleSheet('background-color: #EF5350;')


class Grid2dGraph(NewGraphStore):
    name = "Grid 2d Graph"
    dict_attributes_names = {"m": "Number of rows, m", "n": "Number of columns, n",
                             "conditions": "1 \u2264 m \u00d7 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(Grid2dGraph.dict_attributes_names, name=Grid2dGraph.name, m='', n='')
        dialog.create_button.clicked.connect(lambda: Grid2dGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Lattice_graph"))
        dialog.dict['m'].textEdited.connect(lambda: NewGraphStore.verify_mxn_values(dialog))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_mxn_values(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.grid_2d_graph(int(dialog.dict['m'].text()), int(dialog.dict['n'].text())))
        layout = {(x, y): (((1.93 / (int(dialog.dict['m'].text()) - 0.99)) * x) + 0.05, (0.96 /
                           (int(dialog.dict['n'].text()) - 0.99) * y) + 0.02)
                  for x, y in new_graph_store.graph.nodes()}
        if len(new_graph_store.graph.nodes) == 1:
            layout = {(0, 0): (1, 1), 0: (1, 1)}
        new_graph_store.set_layout(layout)
        NewGraphStore.create_graph(dialog)


class TriangularLatticeGraph(NewGraphStore):
    name = "Triangular Lattice Graph"
    dict_attributes_names = {"m": "Number of rows, m", "n": "Number of columns, n", "conditions":
                             "1 \u2264 m \u00d7 n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(TriangularLatticeGraph.dict_attributes_names,
                                name=TriangularLatticeGraph.name, m='', n='')
        dialog.create_button.clicked.connect(lambda: TriangularLatticeGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://networkx.org/documentation/stable/reference/generated/networkx."
                                           "generators.lattice.triangular_lattice_graph.html"))
        dialog.dict['m'].textEdited.connect(lambda: NewGraphStore.verify_mxn_values(dialog))
        dialog.dict['n'].textEdited.connect(lambda: NewGraphStore.verify_mxn_values(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.triangular_lattice_graph(int(dialog.dict['m'].text()),
                                                              int(dialog.dict['n'].text())))
        layout = nx.get_node_attributes(new_graph_store.graph, 'pos')
        for key, value in layout.items():
            layout[key] = (((3 / (0.8 * (int(dialog.dict['n'].text()) + 1))) * value[0]) + 0.05,
                           ((1.1 / int(dialog.dict['m'].text())) * value[1]) + 0.02)
        new_graph_store.set_layout(layout)
        NewGraphStore.create_graph(dialog)


class PetersenGraph(NewGraphStore):
    name = "Petersen Graph"
    dict_attributes_names = {}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(PetersenGraph.dict_attributes_names, name=PetersenGraph.name)
        dialog.create_button.setEnabled(True)
        dialog.create_button.clicked.connect(lambda: PetersenGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Petersen_graph"))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.petersen_graph())
        new_graph_store.set_layout(PetersenGraph.calculate_layout())
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def calculate_layout():
        pos = {}

        for i in range(5):
            theta = 2 * math.pi * i / 5 + math.pi / 2
            pos[i] = (((2 * math.cos(theta) + 2) * 0.25) + 0.5, (2 * math.sin(theta) + 2) * 0.24)
            pos[5 + i] = (((math.cos(theta) + 2) * 0.25) + 0.5, (math.sin(theta) + 2) * 0.24)

        return pos


class RandomRegularGraph(NewGraphStore):
    name = "Random Regular Graph"
    dict_attributes_names = {"d": "Degree of nodes, d", "n": "Number of nodes, n", "conditions":
                             "1 \u2264 d < n \u2264 60 & d \u00d7 n = even"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(RandomRegularGraph.dict_attributes_names, name=RandomRegularGraph.name, d='', n='')
        dialog.create_button.clicked.connect(lambda: RandomRegularGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Regular_graph"))
        dialog.dict['d'].textEdited.connect(lambda: RandomRegularGraph.verify_dxn(dialog))
        dialog.dict['n'].textEdited.connect(lambda: RandomRegularGraph.verify_dxn(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_regular_graph(int(dialog.dict['d'].text()), int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def verify_dxn(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict['d'].text().isnumeric() and dialog.dict['n'].text().isnumeric() and \
                (int(dialog.dict['d'].text()) * int(dialog.dict['n'].text())) % 2 == 0 and \
                0 <= int(dialog.dict['d'].text()) < int(dialog.dict['n'].text()):
            dialog.create_button.setEnabled(True)
            dialog.dict['d'].setStyleSheet('background-color: white;')
            dialog.dict['n'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['d'].setStyleSheet('background-color: #EF5350;')
            dialog.dict['n'].setStyleSheet('background-color: #EF5350;')


class RandomCograph(NewGraphStore):
    name = "Random Cograph"
    dict_attributes_names = {"k": "2^k nodes, k", "conditions": " 1 \u2264 k < 6"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(RandomCograph.dict_attributes_names, name=RandomCograph.name, k='')
        dialog.create_button.clicked.connect(lambda: RandomCograph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Cograph"))
        dialog.dict['k'].textEdited.connect(lambda: RandomCograph.verify_k_number(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_cograph(int(dialog.dict['k'].text())))
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def verify_k_number(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict['k'].text().isnumeric() and 1 <= int(dialog.dict['k'].text()) < 6:
            dialog.create_button.setEnabled(True)
            dialog.dict['k'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['k'].setStyleSheet('background-color: #EF5350;')


class CompleteBipartiteGraph(NewGraphStore):
    name = "Complete Bipartite Graph"
    dict_attributes_names = {"m": "Number of nodes for set A, m", "n": "Number of nodes for set B, n",
                             "conditions": "1 \u2264 m + n \u2264 60"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(CompleteBipartiteGraph.dict_attributes_names,
                                name=CompleteBipartiteGraph.name, m='', n='')
        dialog.create_button.clicked.connect(lambda: CompleteBipartiteGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Complete_bipartite_graph"))
        dialog.dict['m'].textEdited.connect(lambda: CompleteBipartiteGraph.verify_m_plus_n(dialog))
        dialog.dict['n'].textEdited.connect(lambda: CompleteBipartiteGraph.verify_m_plus_n(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.complete_multipartite_graph(int(dialog.dict['m'].text()),
                                                                 int(dialog.dict['n'].text())))
        new_graph_store.set_layout('bipartite')
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def verify_m_plus_n(dialog):
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if dialog.dict['m'].text().isnumeric() and dialog.dict['n'].text().isnumeric() and \
                0 <= int(dialog.dict['m'].text()) + int(dialog.dict['n'].text()) <= 60:
            dialog.create_button.setEnabled(True)
            dialog.dict['m'].setStyleSheet('background-color: white;')
            dialog.dict['n'].setStyleSheet('background-color: white;')
        else:
            dialog.create_button.setDisabled(True)
            dialog.dict['m'].setStyleSheet('background-color: #EF5350;')
            dialog.dict['n'].setStyleSheet('background-color: #EF5350;')


class ThresholdGraph(NewGraphStore):
    name = "Threshold Graph"
    dict_attributes_names = {"b": "Binary sequence, b", "conditions": "size of b \u2264 60 and b be a binary sequence"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(ThresholdGraph.dict_attributes_names,
                                name=ThresholdGraph.name, b='')
        dialog.create_button.clicked.connect(lambda: ThresholdGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
                                          ("https://en.wikipedia.org/wiki/Threshold_graph"))
        dialog.dict['b'].textEdited.connect(lambda: ThresholdGraph.verify_binary_sequence(dialog))

        NewGraphStore.open_new_dialog(dialog)

    @staticmethod
    def create_graph(dialog):
        graph = nx.Graph()
        node_positions = {}

        for binary in dialog.dict['b'].text():
            if binary == '1':
                graph, node_positions = add_vertex(graph, node_positions, len(graph), univ=True)
            if binary == '0':
                graph, node_positions = add_vertex(graph, node_positions, len(graph))

        new_graph_store.set_graph(graph)
        NewGraphStore.create_graph(dialog)

    @staticmethod
    def verify_binary_sequence(dialog):
        text = dialog.dict['b'].text()
        size = len(text)
        if NewGraphStore.is_other_params_empty(dialog):
            return
        if size <= 60:
            try:
                int(text, 2)
                dialog.create_button.setEnabled(True)
                dialog.dict['b'].setStyleSheet('background-color: white;')
                return
            except ValueError:
                pass
        dialog.create_button.setDisabled(True)
        dialog.dict['b'].setStyleSheet('background-color: #EF5350;')


new_graph_store = NewGraphStore()

new_graph_dict_name = new_graph_store.dic_name_new_graph
