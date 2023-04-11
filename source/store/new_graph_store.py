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

    def set_graph(self, graph):
        self.graph = graph

    def set_file_path(self, file_path):
        self.file_path = file_path

    def reset_attributes(self):
        self.graph = None
        self.file_path = None


class BlankGraph(NewGraphStore):
    name = "Blank Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=BlankGraph.name)
        dialog.dialog_next_button.clicked.connect(lambda: BlankGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.Graph())
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class G6Graph(NewGraphStore):
    name = "G6 Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=G6Graph.name, g6='')
        dialog.dialog_next_button.clicked.connect(lambda: G6Graph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        try:
            new_graph_store.set_graph(nx.from_graph6_bytes(str(dialog.dict['g6'].text()).encode('utf-8')))
        except nx.NetworkXError:
            new_graph_store.set_graph(str(dialog.dict['g6'].text()))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class CycleGraph(NewGraphStore):
    name = "Cycle Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=CycleGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: CycleGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.cycle_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class PathGraph(NewGraphStore):
    name = "Path Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=PathGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: PathGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.path_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class CompleteGraph(NewGraphStore):
    name = "Complete Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=CompleteGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: CompleteGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.complete_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class StarGraph(NewGraphStore):
    name = "Star Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=StarGraph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: StarGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.star_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class TuranGraph(NewGraphStore):
    name = "Turan Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=TuranGraph.name, n='', r='')
        dialog.dialog_next_button.clicked.connect(lambda: TuranGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.turan_graph(int(dialog.dict['n'].text()), int(dialog.dict['r'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class Grid2dGraph(NewGraphStore):
    name = "Grid 2d Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=Grid2dGraph.name, m='', n='', periodic='False')
        dialog.dialog_next_button.clicked.connect(lambda: Grid2dGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.grid_2d_graph(int(dialog.dict['m'].text()), int(dialog.dict['n'].text()),
                                                   bool(dialog.dict['periodic'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class TriangularLatticeGraph(NewGraphStore):
    name = "Triangular Lattice Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=TriangularLatticeGraph.name, m='', n='', periodic='False', with_positions='True')
        dialog.dialog_next_button.clicked.connect(lambda: TriangularLatticeGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.triangular_lattice_graph(int(dialog.dict['m'].text()),
                                                              int(dialog.dict['n'].text()),
                                                              bool(dialog.dict['periodic'].text()),
                                                              bool(dialog.dict['periodic'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class PetersenGraph(NewGraphStore):
    name = "Petersen Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=PetersenGraph.name)
        dialog.dialog_next_button.clicked.connect(lambda: PetersenGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.petersen_graph())
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class RandomRegularGraph(NewGraphStore):
    name = "Random Regular Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=RandomRegularGraph.name, d='', n='')
        dialog.dialog_next_button.clicked.connect(lambda: RandomRegularGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_regular_graph(int(dialog.dict['d'].text()), int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


class RandomCograph(NewGraphStore):
    name = "Random Cograph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name=RandomCograph.name, n='')
        dialog.dialog_next_button.clicked.connect(lambda: RandomCograph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.random_cograph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


new_graph_store = NewGraphStore()

new_graph_dict_name = new_graph_store.dic_name_new_graph
