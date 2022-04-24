import matplotlib.pyplot as plt
import network2tikz as tkz
import networkx as nx
import xlsxwriter

from source.domain.utils import convert_g6_to_nx
from source.store.operations_invariants import dic_invariants_to_visualize as dic



def export_g6_to_png(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw(graph)
    plt.savefig(f"{folder}\Graph_{count}.png", format="PNG")
    plt.close()


def export_g6_to_tikz(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    tkz.plot(graph, f"{folder}\Graph_{count}.tex", layout='fr', node_size=0.4)


def export_g6_to_pdf(g6code, folder, count):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    nx.draw(graph)
    plt.savefig(f"{folder}\Graph_{count}.pdf", format="PDF")
    plt.close()
