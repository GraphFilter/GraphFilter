from simpleeval import simple_eval
import networkx as nx
from operations_and_invariants import operations as op
from operations_and_invariants import num_invariants as inum
from operations_and_invariants import bool_invariants as ibool


def split_expression(expression):
    if "AND" in expression and "OR" in expression:
        return 'error'
    elif "AND" in expression:
        return expression.replace(" ", "").split("AND"), 'AND'
    elif "OR" in expression:
        return expression.replace(" ", "").split("OR"), 'OR'
    else:
        return expression.replace(" ", ""), 'SINGLE'


class FilterList:

    @staticmethod
    def run(list_g6_in, expression, list_inv_bool):
        list_g6_out = []
        functions = {}
        functions.update(inum.InvariantNum().dic_function)
        functions.update(op.MathOperations.dic_function)
        functions.update(op.GraphOperations().dic_function)
        expressions, AND_OR = split_expression(expression)
        count = 0
        total = 0
        for g6code in list_g6_in:
            if g6code == '' or g6code == ' ':
                continue
            total = total + 1
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
                    if bool_inv == ibool.KRegular:
                        graph_satisfies = bool_inv.calc(g, k=1)
                    else:
                        graph_satisfies = bool_inv.calc(g)
                    if not graph_satisfies:
                        break
            if graph_satisfies:
                list_g6_out.append(g6code)
                count = count + 1
            else:
                continue
        return list_g6_out, float(count / total)

    @staticmethod
    def find_counter_example(list_g6_in, expression, list_inv_bool):
        functions = {}
        functions.update(inum.InvariantNum().dic_function)
        functions.update(op.MathOperations().dic_function)
        functions.update(op.GraphOperations().dic_function)
        expressions, AND_OR = split_expression(expression)
        graph_satisfies = True
        for g6code in list_g6_in:
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
                if not graph_satisfies:
                    return g6code
            if graph_satisfies:
                for bool_inv in list_inv_bool:
                    if bool_inv == ibool.KRegular:
                        graph_satisfies = bool_inv.calc(g, k=1)
                    else:
                        graph_satisfies = bool_inv.calc(g)
                    if not graph_satisfies:
                        return g6code
        return ''
