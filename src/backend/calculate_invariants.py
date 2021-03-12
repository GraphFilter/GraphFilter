import networkx as nx


def run(g6code, list_invariants):
    graph = nx.from_graph6_bytes(g6code.encode('utf-8'))
    dic = {}
    for inv in list_invariants:
        dic[inv.name] = str(inv.calculate(graph))
    return dic
