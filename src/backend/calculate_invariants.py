import networkx as nx


def run_from_g6(g6code, list_invariants):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    dic = {}
    for inv in list_invariants:
        dic[inv.name] = str(inv.calculate(graph))
    return dic


def run_from_graph(graph, list_invariants):
    dic = {}
    for inv in list_invariants:
        dic[inv.name] = str(inv.calculate(graph))
    return dic
