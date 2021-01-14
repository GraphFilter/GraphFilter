from simpleeval import simple_eval
import networkx as nx
from Operations_and_Invariants import Operations as op
from Operations_and_Invariants import Invariant_num as inum
from Operations_and_Invariants import Invariant_bool as ibool


def Split_The_Expression(expression):
    if "AND" in expression and "OR" in expression:
        return 'error'
    elif "AND" in expression:
        return expression.replace(" ", "").split("AND"), 'AND'
    elif "OR" in expression:
        return expression.replace(" ", "").split("OR"), 'OR'
    else:
        return expression.replace(" ", ""), 'SINGLE'


class Filter:

    @staticmethod
    def Run(listG6_in, expression, list_inv_bool):
        listG6_out = []
        functions = {}
        functions.update(inum.Invariant_num().dic_function)
        functions.update(op.Math_operations().dic_function)
        functions.update(op.Graph_operations().dic_function)
        expressions, AND_OR = Split_The_Expression(expression)
        count = 0
        total = 0
        for g6code in listG6_in:
            if g6code=='' or g6code==' ':
                continue
            total=total+1
            graph_satisfies = True
            g = nx.from_graph6_bytes(g6code.encode('utf-8'))
            names = {"G": g, "g": g}
            # Check the expressions
            if len(expression) > 0:
                if AND_OR == 'SINGLE':
                    graph_satisfies = simple_eval(expression, functions=functions, names=names)
                elif AND_OR == 'AND':
                    for exp in expressions:
                        graph_satisfies = simple_eval(exp, functions=functions, names=names)
                        if not graph_satisfies:
                            break
                elif AND_OR == "OR":
                    for exp in expressions:
                        graph_satisfies = simple_eval(exp, functions=functions, names=names)
                        if graph_satisfies:
                            break
            # Check the boolean invariants
            if graph_satisfies:
                for bool_inv in list_inv_bool:
                    if bool_inv == ibool.k_Regular:
                        graph_satisfies = bool_inv.calculate(g, k=1)
                    else:
                        graph_satisfies = bool_inv.calculate(g)
                    if not graph_satisfies:
                        break
            if graph_satisfies:
                listG6_out.append(g6code)
                count = count + 1
            else:
                continue
        return listG6_out, float(count / total)

    @staticmethod
    def FindCounterExample(listG6_in, expression, list_inv_bool):
        functions = {}
        functions.update(inum.Invariant_num().dic_function)
        functions.update(op.Math_operations().dic_function)
        functions.update(op.Graph_operations().dic_function)
        expressions, AND_OR = Split_The_Expression(expression)
        graph_satisfies = True
        for g6code in listG6_in:
            g = nx.from_graph6_bytes(g6code.encode('utf-8'))
            names = {"G": g, "g": g}
            # Check the expressions
            if len(expression) > 0:
                if AND_OR == 'SINGLE':
                    graph_satisfies = simple_eval(expression, functions=functions, names=names)
                elif AND_OR == 'AND':
                    for exp in expressions:
                        graph_satisfies = simple_eval(exp, functions=functions, names=names)
                        if not graph_satisfies:
                            return g6code
                elif AND_OR == "OR":
                    for exp in expressions:
                        graph_satisfies = simple_eval(exp, functions=functions, names=names)
                        if graph_satisfies:
                            break
                    if not graph_satisfies:
                        return g6code
            # Check the boolean invariants
            if graph_satisfies:
                for item in list_inv_bool:
                    graph_satisfies = item.calculate(g, )
                    if not graph_satisfies:
                        return g6code
        return False
