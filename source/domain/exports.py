import matplotlib.pyplot as plt
import networkx as nx
import xlsxwriter
import network2tikz as nxtikz

from source.domain.utils import convert_g6_to_nx
from source.store.operations_invariants import dic_invariants_to_visualize as dic


def export_g6_to_png(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw_networkx(graph,
                     node_color='#EEF25C',
                     labels={item: item for item in nx.nodes(graph)})
    plt.savefig(f"{folder}\Graph_{count}.png", format="PNG")
    plt.close()


def export_g6_to_tikz(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    style = {}
    style['node_label'] = list(nx.nodes(graph))
    style['node_color'] = "white"
    nxtikz.plot(graph, f"{folder}\Graph_{count}.tex", layout='fr', node_size=0.4, **style)


def export_g6_to_pdf(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw_networkx(graph,
                     node_color='#EEF25C',
                     labels={item: item for item in nx.nodes(graph)})
    plt.savefig(f"{folder}\Graph_{count}.pdf", format="PDF")
    plt.close()


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
        sheet.write(step + 1, 0, step)
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
