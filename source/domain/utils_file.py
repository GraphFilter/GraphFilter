import networkx as nx

from source.store.project_information_store import project_information_store


def create_gml_file(graph, file_path):
    nx.write_gml(graph, file_path)


def import_gml_graph(file_path):
    try:
        graph = nx.read_gml(file_path)
    except nx.NetworkXError:
        return None

    if len(nx.get_node_attributes(graph, 'x')) != 0:
        for node in graph.nodes:
            graph.nodes[node]['pos'] = (graph.nodes[node]['x'], graph.nodes[node]['y'])

        project_information_store.current_graph_pos = nx.get_node_attributes(graph, 'pos')

    return graph


def change_gml_file(file_path):
    graph = project_information_store.current_graph
    pos = project_information_store.current_graph_pos

    for node, (x, y) in pos.items():
        graph.nodes[node]['x'] = float(x)
        graph.nodes[node]['y'] = float(y)

    nx.write_gml(graph, file_path)


def change_g6_file(file_path, new_g6, current_index):
    file = open(file_path, "r")
    changed_data = file.readlines()

    try:
        changed_data[current_index] = new_g6 + "\n"
    except IndexError:
        changed_data.append(new_g6 + "\n")

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(changed_data)

    with open(file_path) as file:
        graph = file.read().splitlines()

    return graph