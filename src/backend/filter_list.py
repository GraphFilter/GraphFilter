from simpleeval import simple_eval
import networkx as nx
from src.backend.operations_and_invariants import operations as op
from src.backend.operations_and_invariants import num_invariants as i_num
from src.backend.operations_and_invariants import bool_invariants as i_bool


class FilterList:
    list_g6_in = None
    expressions = None
    list_inv_bool_choices = None
    list_g6_out = []
    functions_to_eval = {}
    list_out = None

    def __init__(self):
        # note: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: list of couples [invariant, True/False]
        self.invariant_bool = i_bool.InvariantBool()
        self.invariant_num = i_num.InvariantNum()
        self.operations_math = op.MathOperations()
        self.operations_graph = op.GraphOperations()
        self.functions_to_eval.update(self.invariant_num.dic_function)
        self.functions_to_eval.update(self.operations_graph.dic_function)
        self.functions_to_eval.update(self.operations_math.dic_function)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices):
        self.list_g6_in = list_g6_in
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = self.split_translate_expression(expression)

    def split_translate_expression(self, expression):
        for inv in self.invariant_num.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")
        for inv in self.operations_graph.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")

        if "AND" in expression and "OR" in expression:
            return 'error'
        elif "AND" in expression:
            return expression.replace(" ", "").split("AND"), 'AND'
        elif "OR" in expression:
            return expression.replace(" ", "").split("OR"), 'OR'
        else:
            return expression.replace(" ", ""), 'SINGLE'

    def run(self):
        self.list_out = []
        count = 0
        total = 0
        for g6code in self.list_g6_in:
            if g6code == '' or g6code == ' ':
                continue
            total = total + 1
            graph_satisfies = True
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
                            break
                elif self.AND_OR == "OR":
                    for exp in self.expressions:
                        graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                        if graph_satisfies:
                            break
            # Check the boolean invariants
            if graph_satisfies:
                for bool_inv in self.list_inv_bool_choices:
                    if bool_inv[1]:
                        graph_satisfies = bool_inv[0].calculate(g)
                    else:
                        graph_satisfies = not bool_inv[0].calculate(g)
                    if not graph_satisfies:
                        break
            if graph_satisfies:
                self.list_out.append(g6code)
                count = count + 1
            else:
                continue
        return float(count / total)

    def find_counter_example(self):
        self.list_out = []
        graph_satisfies = True
        for g6code in self.list_g6_in:
            if g6code == '' or g6code == ' ':
                continue
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
                    if bool_inv[1]:
                        graph_satisfies = bool_inv[0].calculate(g)
                    else:
                        graph_satisfies = not bool_inv[0].calculate(g)
                    if not graph_satisfies:
                        self.list_out.append(g6code)
                        return True
        return False
