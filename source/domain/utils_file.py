import networkx as nx
from PyQt5.QtCore import QStandardPaths
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore

from source.domain.utils import trigger_message_box
from source.store.project_information_store import project_information_store
from source.domain.pdf_model import PDF


def create_gml_file(graph, file_path):
    nx.write_gml(graph, file_path)


def import_gml_graph(file_path):
    try:
        graph = nx.read_gml(file_path)
    except nx.NetworkXError:
        return None

    project_information_store.current_graph_pos = {}

    if len(nx.get_node_attributes(graph, 'x')) != 0:
        for node in graph.nodes:
            graph.nodes[node]['pos'] = (graph.nodes[node]['x'], graph.nodes[node]['y'])

        project_information_store.current_graph_pos = nx.get_node_attributes(graph, 'pos')

    return graph


def change_gml_file(file_path):
    if project_information_store.get_file_type() != '.gml':
        file_path = file_path + '.gml'
    graph = project_information_store.current_graph
    pos = project_information_store.current_graph_pos

    for node, (x, y) in pos.items():
        graph.nodes[node]['x'] = float(x)
        graph.nodes[node]['y'] = float(y)

    try:
        nx.write_gml(graph, file_path)
        return [project_information_store.get_file_name()]
    except:
        handle_invalid_file_open()
        return None


def delete_all_gml_nodes(file_path):
    graph = project_information_store.current_graph
    e = list(graph.nodes)
    graph.remove_nodes_from(e)
    nx.write_gml(graph, file_path)
    return graph


def change_g6_file(file_path, new_g6, current_index):
    try:
        with open(file_path, "r") as file:
            changed_data = file.readlines()
    except:
        handle_invalid_file_open()
        return None

    try:
        changed_data[current_index] = new_g6 + "\n"
    except IndexError:
        changed_data.append("\n" + new_g6)

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(changed_data)

    with open(file_path) as file:
        graph = file.read().splitlines()

    return graph


def create_g6_file(path_to_save, graph_list, name_file=None, name_modifier=''):
    if name_file is None:
        with open(path_to_save, "w", encoding="utf-8") as file:
            file.writelines(graph_list)
        return

    with open(f"{path_to_save}/{name_file}{name_modifier}.g6", 'w') as fp:
        for graph in graph_list:
            fp.write(f"{graph}\n")


def generate_pdf_report(name, method, equation, conditions, input_graph_file, filtered_graphs, name_modifier,
                        num_graphs, description):
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.information_about_filtering(name,
                                    method,
                                    equation,
                                    conditions,
                                    description,
                                    input_graph_file)
    pdf.information_about_graphs(filtered_graphs, method, num_graphs)
    pdf.output(project_information_store.get_file_directory() +
               '/' + f'{name}{name_modifier}.pdf')


def handle_invalid_file_open():
    trigger_message_box("Invalid file to save or delete. Check if the file still exists.", icon=QMessageBox.Warning,
                        window_title="Invalid File")


def get_name_from_save_dialog(format_file):
    default_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    default_name = project_information_store.get_file_name_without_extension()
    file_name, _ = QFileDialog.getSaveFileName(caption=f"Export graph(s) to {format_file} file",
                                                filter=f"Files (*.{format_file})",
                                               directory=default_dir + f"/{default_name}")
    if file_name:
        if not QtCore.QFileInfo(file_name).suffix():
            file_name += f".{format_file}"
    return file_name


def get_directory_name_from_existing_directory():
    default_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    return str(QFileDialog.getExistingDirectory(caption="Select Directory",
                                                directory=default_dir))
