import numpy

import networkx as nx
from simpleeval import simple_eval

from src.domain.operations_and_invariants.operations_invariants import Invariants
from src.domain.operations_and_invariants.operations_invariants import Operations


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
        # note: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: list of couples [invariant_name, 'true' or 'false']
        invariants = Invariants()
        operations = Operations()
        self.invariant_bool = invariants.booleans
        self.invariant_num = invariants.numerics
        self.operations_math = operations.math
        self.operations_graph = operations.graphs
        self.functions_to_eval.update(self.invariant_num.dic_function)
        self.functions_to_eval.update(self.operations_graph.dic_function)
        self.functions_to_eval.update(self.operations_math.dic_function)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices):
        self.invalid_lines = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = self.split_translate_expression(expression)

    def split_translate_expression(self, expression):
        for inv in self.operations_graph.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")
        for inv in self.operations_math.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")
        for inv in self.invariant_num.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")

        if "AND" in expression and "OR" in expression:
            return '', 'error'
        elif "AND" in expression:
            return expression.replace(" ", "").split("AND"), 'AND'
        elif "OR" in expression:
            return expression.replace(" ", "").split("OR"), 'OR'
        else:
            return expression.replace(" ", ""), 'SINGLE'

    def validate_expression(self, expression):
        if len(expression) == 0:
            return ""
        expressions, AND_OR = self.split_translate_expression(expression)
        if AND_OR == 'error':
            return "Expression using 'AND' and 'OR' simultaneously is not allowed"
        try:
            if AND_OR == 'SINGLE':
                if not self.valid_bool_simpleval(expressions):
                    return "It's not a valid equation or inequality"
            elif AND_OR == 'AND' or AND_OR == 'OR':
                for exp in expressions:
                    if not self.valid_bool_simpleval(exp):
                        return "It's not a valid equation or inequality"
        except:
            return "Unknown terms in the expression"
        return ""

    def valid_bool_simpleval(self, expression):
        g = nx.trivial_graph()
        names = {"G": g, "g": g}
        type_ex = type(simple_eval(expression, functions=self.functions_to_eval, names=names))
        return type_ex == numpy.bool or type_ex == numpy.bool_ or type_ex == bool

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
                            graph_satisfies = self.invariant_bool.dic_name_inv[bool_inv[0]].calculate(g)
                        else:
                            graph_satisfies = not self.invariant_bool.dic_name_inv[bool_inv[0]].calculate(g)
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
                            graph_satisfies = self.invariant_bool.dic_name_inv[bool_inv[0]].calculate(g)
                        else:
                            graph_satisfies = not self.invariant_bool.dic_name_inv[bool_inv[0]].calculate(g)
                        if not graph_satisfies:
                            self.list_out.append(g6code)
                            return True
            except nx.NetworkXError:
                self.invalid_lines = self.invalid_lines + 1
                continue
        return False
