import os

from simpleeval import simple_eval
from source.store.operations_invariants import *
from source.domain.equation import Equation
import numpy as np
import multiprocessing as mp

class FilterList:

    def __init__(self):
        self.list_g6_in = None
        self.expressions = None
        self.list_inv_bool_choices = None
        self.functions_to_eval = {}
        self.list_out = []
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
        self.satisfied_graphs = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.total = len(self.list_g6_in)
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = Equation.split_translate_expression(expression)
        self.update_to_progress_bar = update

    # TODO: organizar a variável que armazena linhas inválidas, organizar os métodos filter e findcounterexample.
    def run_filter(self):
        if self.total > 100:
            manager = mp.Manager()
            cores=os.cpu_count()
            list_breaked_in = self.subdivide_input_list(cores)
            list_breaked_out = manager.list(range(cores))
            list_process=[]
            for i, list in enumerate(list_breaked_in):
                list_process.append(mp.Process(target=self.filter_multi, args=(list, i, list_breaked_out)))
            for process in list_process:
                process.start()
            for process in list_process:
                process.join()
            for list in list_breaked_out:
                self.list_out+=list
            return float(len(self.list_out) / self.total)
        else:
            self.filter(self.list_g6_in)
            return float(len(self.list_out) / self.total)


    def filter_multi(self, list_g6_in, i, list_out):
        list_out_temp = []
        for g6code in list_g6_in:
            self.update_to_progress_bar
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if self.graph_satisfies_conditions(g):
                        list_out_temp.append(g6code)
            except Exception:
                self.invalid_lines += 1
        # self.satisfied_graphs = self.satisfied_graphs + len(list_out)
        list_out[i] = list_out_temp


    def filter(self, list_g6_in):
        for g6code in list_g6_in:
            self.update_to_progress_bar
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if self.graph_satisfies_conditions(g):
                        self.list_out.append(g6code)
            except Exception:
                self.invalid_lines += 1
        # self.satisfied_graphs = self.satisfied_graphs + len(list_out)


    def subdivide_input_list(self, parts):
        n_sub = int(np.ceil(self.total / parts))
        return [self.list_g6_in[i:i + n_sub] for i in range(0, self.total, n_sub)]


    def run_find_counterexample(self):
        self.list_out = []
        for g6code in self.list_g6_in:
            if self.filter_list(g6code) ==False:
                self.list_out = [g6code]
                return True
        return False

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


if __name__ == "__main__":
    print("teste")