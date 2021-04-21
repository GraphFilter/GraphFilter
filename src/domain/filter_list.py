import networkx as nx
from simpleeval import simple_eval

from src.store.operations_invariants import *
from src.domain.equation import Equation


class FilterList:
    list_g6_in = None
    expressions = None
    list_inv_bool_choices = None
    functions_to_eval = {}
    list_out = []
    invalid_lines = 0
    invariant_bool = None
    invariant_num = None
    operations_math = None
    operations_graph = None
    AND_OR = None

    def __init__(self):
        # NOTE: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: list of couples [invariant_name, 'true' or 'false']
        self.functions_to_eval.update(dic_function_to_eval)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices):
        self.invalid_lines = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = Equation.split_translate_expression(expression)

    def run_filter(self):
        self.list_out = []
        count = 0
        total = 0
        for g6code in self.list_g6_in:
            if g6code == '' or g6code == ' ':
                continue
            graph_satisfies = True
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                total = total + 1
                names = {"G": g, "g": g}
                # Check the expressions
                if len(self.expressions) > 0:
                    if self.AND_OR == 'SINGLE':
                        graph_satisfies = simple_eval(self.expressions, functions=self.functions_to_eval, names=names)
                    elif self.AND_OR == 'AND':
                        for exp in self.expressions:
                            graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                            if not graph_satisfies:
                                break
                    elif self.AND_OR == "OR":
                        for exp in self.expressions:
                            graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                            if graph_satisfies:
                                break
                # Check the boolean invariants
                if graph_satisfies:
                    for bool_inv in self.list_inv_bool_choices:
                        if bool_inv[1] == 'true':
                            graph_satisfies = dic_bool_invariants_names[bool_inv[0]].calculate(g)
                        else:
                            graph_satisfies = not dic_bool_invariants_names[bool_inv[0]].calculate(g)
                        if not graph_satisfies:
                            break
                if graph_satisfies:
                    self.list_out.append(g6code)
                    count = count + 1
                else:
                    continue
            except nx.NetworkXError:
                self.invalid_lines = self.invalid_lines + 1
                continue
        return float(count / total)

    def run_find_counterexample(self):
        self.list_out = []
        graph_satisfies = True
        for g6code in self.list_g6_in:
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                names = {"G": g, "g": g}
                # Check the expressions
                if len(self.expressions) > 0:
                    if self.AND_OR == 'SINGLE':
                        graph_satisfies = simple_eval(self.expressions, functions=self.functions_to_eval, names=names)
                    elif self.AND_OR == 'AND':
                        for exp in self.expressions:
                            graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                            if not graph_satisfies:
                                self.list_out.append(g6code)
                                return True
                    elif self.AND_OR == "OR":
                        for exp in self.expressions:
                            graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                            if graph_satisfies:
                                break
                        if not graph_satisfies:
                            self.list_out.append(g6code)
                            return True
                    # Check the boolean invariants
                    if not graph_satisfies:
                        self.list_out.append(g6code)
                        return True
                if graph_satisfies:
                    for bool_inv in self.list_inv_bool_choices:
                        if bool_inv[1] == 'true':
                            graph_satisfies = dic_bool_invariants_names[bool_inv[0]].calculate(g)
                        else:
                            graph_satisfies = not dic_bool_invariants_names[bool_inv[0]].calculate(g)
                        if not graph_satisfies:
                            self.list_out.append(g6code)
                            return True
            except nx.NetworkXError:
                self.invalid_lines = self.invalid_lines + 1
                continue
        return False
