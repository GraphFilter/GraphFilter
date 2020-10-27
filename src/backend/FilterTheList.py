from simpleeval import simple_eval
from src.backend.Invariant import Invariant
import networkx as nx


class Filter:

    @staticmethod
    def Run(listG6_in):
        total = len(listG6_in)
        listG6_out=[]
        invariant = Invariant()
        functions = invariant.dic_invariants_num
        count=0
        for g6code in listG6_in:
            g=nx.from_graph6_bytes(g6code.encode('utf-8'))
            lg = nx.line_graph(nx.from_graph6_bytes(g6code.encode('utf-8')))
            cg = nx.complement(nx.from_graph6_bytes(g6code.encode('utf-8')))
            names = {"G": g, "lG": lg, "cG": cg}
            if simple_eval("match(G)==5", functions=functions, names=names):
                listG6_out.append(g6code)
                count=count+1
        return listG6_out,count/total

