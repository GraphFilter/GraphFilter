import abc

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

from source.domain.utils import validate_file_name
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
        self.radio_option = 0

    def set_graph(self, graph):
        self.graph = graph

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_radio_option(self, option):
        self.radio_option = option

    def reset_attributes(self):
        self.graph = None
        self.file_path = None

    @staticmethod
    def open_url(url):
        QDesktopServices.openUrl(QUrl(url))

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")
        new_graph_store.set_radio_option(1 if dialog.insert_final_radio.isChecked() else 0)

        dialog.close()

    @staticmethod
    def verify_and_save_project_name(dialog):
        if validate_file_name(dialog.dict['name'].text()):
            dialog.dialog_next_button.setEnabled(True)
            dialog.dict['name'].setStyleSheet('background-color: white;')
        else:
            dialog.dialog_next_button.setDisabled(True)
            dialog.dict['name'].setStyleSheet('background-color: #EF5350;')


class EmptyGraph(NewGraphStore):
    name = "Empty Graph"
    dict_attributes_names = None

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(EmptyGraph.dict_attributes_names, name=EmptyGraph.name)
        dialog.dialog_next_button.clicked.connect(lambda: EmptyGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Null_graph"))
        dialog.dict['name'].textEdited.connect(lambda: NewGraphStore.verify_and_save_project_name(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.Graph())
        NewGraphStore.create_graph(dialog)


class GraphFromGraph6(NewGraphStore):
    name = "Graph from graph6"
    dict_attributes_names = {"name": "https://en.wikipedia.org/wiki/Null_graph", "g6": "Graph from g6"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(GraphFromGraph6.dict_attributes_names, name=GraphFromGraph6.name, g6='')
        dialog.dialog_next_button.clicked.connect(lambda: GraphFromGraph6.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Null_graph"))
        new_graph_store.set_radio_option(1 if dialog.insert_final_radio.isChecked() else 0)

        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        try:
            new_graph_store.set_graph(nx.from_graph6_bytes(str(dialog.dict['g6'].text()).encode('utf-8')))
        except nx.NetworkXError:
            new_graph_store.set_graph(str(dialog.dict['g6'].text()))
        NewGraphStore.create_graph(dialog)


class CycleGraph(NewGraphStore):
    name = "Cycle Graph"
    dict_attributes_names = {"n": "Number of nodes"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(CycleGraph.dict_attributes_names, name=CycleGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: CycleGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Cycle_graph"))

        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.cycle_graph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class PathGraph(NewGraphStore):
    name = "Path Graph"
    dict_attributes_names = {"n": "Number of nodes"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(PathGraph.dict_attributes_names, name=PathGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: PathGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Path_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.path_graph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class CompleteGraph(NewGraphStore):
    name = "Complete Graph"
    dict_attributes_names = {"n": "Number of nodes"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(CompleteGraph.dict_attributes_names, name=CompleteGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: CompleteGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Complete_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.complete_graph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class StarGraph(NewGraphStore):
    name = "Star Graph"
    dict_attributes_names = {"n": "Number of nodes"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(StarGraph.dict_attributes_names, name=StarGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: StarGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Star_(graph_theory)"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.star_graph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class TuranGraph(NewGraphStore):
    name = "Turan Graph"
    dict_attributes_names = {"n": "Number of nodes", "r": "Number of subsets"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(TuranGraph.dict_attributes_names, name=TuranGraph.name, n='', r='')
        dialog.dialog_next_button.clicked.connect(lambda: TuranGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Turán_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.turan_graph(int(dialog.dict['n'].text()), int(dialog.dict['r'].text())))
        NewGraphStore.create_graph(dialog)


class Grid2dGraph(NewGraphStore):
    name = "Grid 2d Graph"
    dict_attributes_names = {"m": "Number of rows", "n": "Number of columns"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(Grid2dGraph.dict_attributes_names, name=Grid2dGraph.name, m='', n='')
        dialog.dialog_next_button.clicked.connect(lambda: Grid2dGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://mathworld.wolfram.com/GridGraph.html#:~:text=A%20two-dimensional%20"
         "grid%20graph,path%20graphs%20on%20and%20vertices."))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.grid_2d_graph(int(dialog.dict['m'].text()), int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class TriangularLatticeGraph(NewGraphStore):
    name = "Triangular Lattice Graph"
    dict_attributes_names = {"m": "Number of rows", "n": "Number of columns"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(TriangularLatticeGraph.dict_attributes_names,
                                name=TriangularLatticeGraph.name, m='', n='')
        dialog.dialog_next_button.clicked.connect(lambda: TriangularLatticeGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Lattice_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.triangular_lattice_graph(int(dialog.dict['m'].text()),
                                                              int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class PetersenGraph(NewGraphStore):
    name = "Petersen Graph"
    dict_attributes_names = None

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(PetersenGraph.dict_attributes_names, name=PetersenGraph.name)
        dialog.dialog_next_button.clicked.connect(lambda: PetersenGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Petersen_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.petersen_graph())
        NewGraphStore.create_graph(dialog)


class RandomRegularGraph(NewGraphStore):
    name = "Random Regular Graph"
    dict_attributes_names = {"d": "Degree of nodes", "n": "Number of nodes"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(RandomRegularGraph.dict_attributes_names, name=RandomRegularGraph.name, d='', n='')
        dialog.dialog_next_button.clicked.connect(lambda: RandomRegularGraph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Random_regular_graph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_regular_graph(int(dialog.dict['d'].text()), int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


class RandomCograph(NewGraphStore):
    name = "Random Cograph"
    dict_attributes_names = {"n": "Order of cograph"}

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(RandomCograph.dict_attributes_names, name=RandomCograph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: RandomCograph.create_graph(dialog))
        dialog.graph_link.clicked.connect(lambda: NewGraphStore.open_url
        ("https://en.wikipedia.org/wiki/Cograph"))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_cograph(int(dialog.dict['n'].text())))
        NewGraphStore.create_graph(dialog)


new_graph_store = NewGraphStore()

new_graph_dict_name = new_graph_store.dic_name_new_graph
