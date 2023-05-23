import networkx as nx
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt

from source.domain.utils_file import change_gml_file, create_g6_file
from source.store.project_information_store import project_information_store
import network2tikz as tkz


class ExportGraphTo:
    name = None

    def __init__(self):
        self.all = ExportGraphTo.__subclasses__()
        self.dict_name_export_graph_to: {str: ExportGraphTo} = {}
        for formats in self.all:
            self.dict_name_export_graph_to[formats.name] = formats
        self.file_path = None

    @staticmethod
    def export():
        file_dialog = QFileDialog()
        file_path = file_dialog.getSaveFileName(directory=project_information_store.get_file_name())
        export_graph_to.file_path = file_path[0].strip(project_information_store.get_file_type())


class ExportToGML(ExportGraphTo):
    name = ".GML"

    @staticmethod
    def export():
        ExportGraphTo.export()
        change_gml_file(export_graph_to.file_path)


class ExportToG6(ExportGraphTo):
    name = ".Graph6"

    @staticmethod
    def export():
        ExportGraphTo.export()
        create_g6_file(export_graph_to.file_path + ".g6", nx.to_graph6_bytes(project_information_store.current_graph,
                                                                             header=False).decode('utf-8'))


class ExportToPNG(ExportGraphTo):
    name = ".PNG"

    @staticmethod
    def export():
        ExportGraphTo.export()
        nx.draw(project_information_store.current_graph)
        plt.savefig(f"{export_graph_to.file_path}.png", format="PNG")
        plt.close()


class ExportToTikZ(ExportGraphTo):
    name = ".TikZ"

    @staticmethod
    def export():
        ExportGraphTo.export()
        tkz.plot(project_information_store.current_graph, f"{export_graph_to.file_path}.tex", layout='fr',
                 node_size=0.4)


export_graph_to = ExportGraphTo()

dict_name_export_graph_to = export_graph_to.dict_name_export_graph_to
