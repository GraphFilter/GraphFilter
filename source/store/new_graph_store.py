from source.view.project.new_graph_dialog import NewGraphDialog
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


class CycleGraph(NewGraphStore):
    name = "Cycle Graph"

    @staticmethod
    def open_dialog():
        dialog = NewGraphDialog(name='Default', n='')
        dialog.dialog_next_button.clicked.connect(lambda: CycleGraph.create_graph(dialog))
        dialog.exec()

    @staticmethod
    def create_graph(dialog):
        new_graph_store.set_graph(nx.cycle_graph(int(dialog.dict['n'].text())))
        new_graph_store.set_file_path(project_information_store.project_location + f"\\{dialog.dict['name'].text()}.g6")

        dialog.close()


new_graph_store = NewGraphStore()

new_graph_dict_name = new_graph_store.dic_name_new_graph
