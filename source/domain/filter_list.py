from simpleeval import simple_eval
from source.store.operations_invariants import *
from source.domain.equation import Equation


class FilterList:

    def __init__(self):
        self.list_g6_in = None
        self.expressions = None
        self.list_inv_bool_choices = None
        self.functions_to_eval = {}
        self.list_out = []
        self.invalid_lines = 0
        self.invariant_bool = None
        self.invariant_num = None
        self.operations_math = None
        self.operations_graph = None
        self.AND_OR = None
        self.total = 0

        self.update_to_progress_bar = None

        # NOTE: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: dict of couples {invariant_name: 'true' or 'false'}
        self.functions_to_eval.update(dic_function_to_eval)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices, update):
        self.invalid_lines = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.total = len(self.list_g6_in)
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = Equation.split_translate_expression(expression)
        self.update_to_progress_bar = update

    def graph_satisfies_equation(self, g):
        names = {**{"G": g, "g": g}, **dic_math_const}
        # Check the expressions
        if len(self.expressions) > 0:
            if self.AND_OR == 'SINGLE':
                return simple_eval(self.expressions, functions=self.functions_to_eval, names=names)
            elif self.AND_OR == 'AND':
                for exp in self.expressions:
                    if not simple_eval(exp, functions=self.functions_to_eval, names=names):
                        return False
                return True
            elif self.AND_OR == "OR":
                for exp in self.expressions:
                    if simple_eval(exp, functions=self.functions_to_eval, names=names):
                        return True
                return False
        return True

    def graph_satisfies_conditions(self, g):
        for inv_name in self.list_inv_bool_choices:
            if self.list_inv_bool_choices[inv_name] == 'true':
                graph_satisfies = dic_bool_invariants_names[inv_name].calculate(g)
            else:
                graph_satisfies = not dic_bool_invariants_names[inv_name].calculate(g)
            if not graph_satisfies:
                return False
        return True


    def run_filter(self):
        self.list_out = []
        count = 0
        for step, g6code in enumerate(self.list_g6_in):
            self.update_to_progress_bar(step)
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if self.graph_satisfies_conditions(g):
                        self.list_out.append(g6code)
                        count = count + 1
                self.update_to_progress_bar(step)
            except Exception:
                self.invalid_lines = self.invalid_lines + 1
                continue
        return float(count / self.total)

    def run_find_counterexample(self):
        self.list_out = []
        for step, g6code in enumerate(self.list_g6_in):
            self.update_to_progress_bar(step)
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if not self.graph_satisfies_conditions(g):
                        self.list_out.append(g6code)
                        return True
                else:
                    self.list_out.append(g6code)
                    return True
                self.update_to_progress_bar(step)
            except Exception:
                self.invalid_lines = self.invalid_lines + 1
                continue
        return False


if __name__ == "__main__":
    print("teste")