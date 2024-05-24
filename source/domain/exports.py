import math
import os
from typing import Callable

import matplotlib.pyplot as plt

import networkx as nx
import xlsxwriter
import network2tikz as nxtikz
from networkx import NetworkXError

from source.domain.utils import convert_g6_to_nx
from source.store.operations_invariants import dic_invariants_to_visualize as dic
from matplotlib.backends.backend_pdf import PdfPages


def export_g6_to_png(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw_networkx(graph,
                     node_color='#EEF25C',
                     labels={item: item for item in nx.nodes(graph)})
    plt.savefig(f"{folder}\Graph_{count + 1}.png", format="PNG")
    plt.close()


def export_g6_to_tikz(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    style = {'node_label': list(nx.nodes(graph)), 'node_color': "white"}
    nxtikz.plot(graph, f"{folder}\Graph_{count}.tex", layout='fr', node_size=0.4, **style)


def export_g6_to_pdf(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw_networkx(graph,
                     node_color='#EEF25C',
                     labels={item: item for item in nx.nodes(graph)})
    plt.savefig(f"{folder}\Graph_{count + 1}.pdf", format="PDF")
    plt.close()


def draw_graph(graph, ax, idx, node_size, font_size):
    nx.draw_networkx(graph, ax=ax, node_color='white', edgecolors='black',
                     labels={node: node for node in nx.nodes(graph)}, node_size=node_size,
                     font_size=font_size)
    ax.set_title(f"Graph {idx + 1}", fontsize=font_size)


def plot_graphs_on_page(g6_graphs, start_index, end_index, number_rows, number_cols, node_size, font_size,
                        last_page=False):
    fig, axs = plt.subplots(number_rows, number_cols, figsize=(8.27, 11.69), tight_layout=True)
    for i, idx in enumerate(range(start_index, end_index)):
        row, col = divmod(i, number_cols)
        ax = axs[row, col] if number_rows > 1 else axs[col] if number_cols > 1 else axs
        try:
            graph = nx.from_graph6_bytes(g6_graphs[idx].encode('utf-8'))
            draw_graph(graph, ax, idx, node_size, font_size)
        except NetworkXError:
            i -= 1

    if last_page:
        for j in range(i + 1, number_rows * number_cols):
            fig.delaxes(axs.flatten()[j])

    return fig


def export_g6_list_to_pdf(g6_graphs: list[str], file_path: str, number_rows: int, number_cols: int,
                          loading_window: object, update_loading: Callable):
    number_graphs = len(g6_graphs)
    elements_per_page = number_rows * number_cols
    number_pages = math.ceil(number_graphs / elements_per_page)
    max_dimension = max(number_rows, number_cols)
    node_size = 500 / max_dimension
    font_size = 18 / (max_dimension ** (1 / 1.618))

    with PdfPages(file_path) as pdf:
        for page in range(number_pages):
            start_index = page * elements_per_page
            end_index = min((page + 1) * elements_per_page, number_graphs)
            last_page = page == number_pages - 1
            fig = plot_graphs_on_page(g6_graphs, start_index, end_index, number_rows, number_cols, node_size, font_size,
                                      last_page)
            pdf.savefig(fig)
            plt.close(fig)

            if loading_window.is_forced_to_close:
                loading_window.is_forced_to_close = False
                return
            update_loading(end_index - 1)


def export_g6_to_sheet(graph_list, invariants, file_name, update_progress, loading_window):
    workbook = xlsxwriter.Workbook(filename=file_name)
    sheet = workbook.add_worksheet()
    sheet.write(0, 0, 'id')
    sheet.write(0, 1, 'g6 code')
    for i, invariant in enumerate(invariants):
        if loading_window.is_forced_to_close:
            loading_window.is_forced_to_close = False
            return
        sheet.write(0, i + 2, invariant)
    for step, graph in enumerate(graph_list):
        if loading_window.is_forced_to_close:
            loading_window.is_forced_to_close = False
            return
        sheet.write(step + 1, 0, step + 1)
        sheet.write(step + 1, 1, graph)
        for k, invariant in enumerate(invariants):
            if dic[invariant].type in ["number_structural", "number_spectral"]:
                try:
                    sheet.write_number(step + 1, k + 2,
                                       float(dic[invariant].print(convert_g6_to_nx(graph), precision=5)))
                except:
                    sheet.write_string(step + 1, k + 2, "ERROR in calculation, please report problem.")
            elif dic[invariant].type in ['bool_structural', 'bool_spectral']:
                try:
                    sheet.write_string(step + 1, k + 2, dic[invariant].print(convert_g6_to_nx(graph), precision=5))
                except:
                    sheet.write_string(step + 1, k + 2, "ERROR in calculation, please report problem.")
            else:
                sheet.write(step + 1, k + 2, 'no data')
        update_progress(step)
    workbook.close()
