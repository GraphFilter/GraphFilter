from simpleeval import simple_eval
import networkx as nx
from operations_and_invariants import operations as op
from operations_and_invariants import num_invariants as inum
from operations_and_invariants import bool_invariants as ibool




def ini_out_file():
    dic_out = {}

def save_graph_out(dict, graph, ):
    pass




class FilterList:

    list_g6_in = None
    expressions = None
    list_inv_bool = None
    list_g6_out = []
    functions_to_eval = {}
    invariants_selected = []
    out = []

    def __init__(self, list_g6_in, expression, list_inv_bool):
        self.list_g6_in = list_g6_in
        self.list_inv_bool = list_inv_bool
        self.functions_to_eval.update(inum.InvariantNum().dic_function)
        self.functions_to_eval.update(op.MathOperations().dic_function)
        self.functions_to_eval.update(op.GraphOperations().dic_function)
        self.expressions, self.AND_OR = self.split_translate_expression(expression)
        self.fill_invariants_selected(expression)


    def fill_invariants_selected(self, expression):
        self.invariants_selected = self.list_inv_bool
        if len(expression)>0:
            for inv in inum.InvariantNum.all:
                if inv.code_literal in expression:
                    self.invariants_selected.append(inv)

    def save_invariants_dic_from(self, graph):
        dic = {}
        for inv in self.invariants_selected:
            dic[inv.name] = str(inv.calculate)
        return dic


    def split_translate_expression(self,expression):
        for code, code_literal in inum.InvariantNum.dic_translate.items():
            expression = str(expression).replace(code + "(", code_literal + "(")
        for code, code_literal in op.GraphOperations.dic_translate.items():
            expression = str(expression).replace(code + "(", code_literal + "(")

        if "AND" in expression and "OR" in expression:
            return 'error'
        elif "AND" in expression:
            return expression.replace(" ", "").split("AND"), 'AND'
        elif "OR" in expression:
            return expression.replace(" ", "").split("OR"), 'OR'
        else:
            return expression.replace(" ", ""), 'SINGLE'


    def run(self):
        self.out = []
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
                for bool_inv in self.list_inv_bool:
                    if bool_inv == ibool.KRegular:
                        graph_satisfies = bool_inv.calculate(g, k=1)
                    else:
                        graph_satisfies = bool_inv.calculate(g)
                    if not graph_satisfies:
                        break
            if graph_satisfies:
                self.out.append({'g6code': g6code, 'results': self.save_invariants_dic_from(g)})
                count = count + 1
            else:
                continue
        return float(count / total)


    def find_counter_example(self):
        self.out = []
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
                            self.out.append({'g6code': g6code, 'results': self.save_invariants_dic_from(g)})
                            return True
                elif self.AND_OR == "OR":
                    for exp in self.expressions:
                        graph_satisfies = simple_eval(exp, functions=self.functions_to_eval, names=names)
                        if graph_satisfies:
                            break
                    if not graph_satisfies:
                        self.out.append({'g6code': g6code, 'results': self.save_invariants_dic_from(g)})
                        return True
            # Check the boolean invariants
                if not graph_satisfies:
                    self.out.append({'g6code': g6code, 'results': self.save_invariants_dic_from(g)})
                    return True
            if graph_satisfies:
                for bool_inv in self.list_inv_bool:
                    if bool_inv == ibool.KRegular:
                        graph_satisfies = bool_inv.calculate(g, k=1)
                    else:
                        graph_satisfies = bool_inv.calculate(g)
                    if not graph_satisfies:
                        self.out.append({'g6code': g6code, 'results': self.save_invariants_dic_from(g)})
                        return True
        return False