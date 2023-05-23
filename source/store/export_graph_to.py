import networkx as nx
from PyQt5.QtWidgets import QFileDialog

from source.domain.utils_file import change_gml_file
from source.store.project_information_store import project_information_store
from source.view.components.message_box import MessageBox


class ExportGraphTo:
    name = None

    def __init__(self):
        self.all = ExportGraphTo.__subclasses__()
        self.dict_name_export_graph_to: {str: ExportGraphTo} = {}
        for formats in self.all:
            self.dict_name_export_graph_to[formats.name] = formats


class ExportToGML(ExportGraphTo):
    name = ".GML"

    @staticmethod
    def export():
        file_dialog = QFileDialog()
        file_path = file_dialog.getSaveFileName(directory=project_information_store.get_file_name())
        print(file_path)
        return change_gml_file(file_path[0])


export_graph_to = ExportGraphTo()

dict_name_export_graph_to = export_graph_to.dict_name_export_graph_to
