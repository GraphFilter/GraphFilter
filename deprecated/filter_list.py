import multiprocessing
import multiprocessing as mp
import os
import random
import time

from simpleeval import simple_eval

from source.domain.boolean_expression_solver import Expression
from source.store.operations_invariants import *


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
        self.is_forced_to_terminate = mp.Value("d", 0.0, lock=True)

        self.update_to_progress_bar = mp.Value("d", 0.0, lock=True)

        # NOTE: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: dict of couples {invariant_name: 'true' or 'false'}
        self.functions_to_eval.update(dic_function_to_eval)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices):
        self.satisfied_graphs = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.total = len(self.list_g6_in)
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = Expression.split_translate_expression(expression)

    def start_filter(self, list_g6_in, expression, list_inv_bool_choices):
        self.set_inputs(list_g6_in, expression, list_inv_bool_choices)
        number_cores = int(np.ceil((1 / 3) * os.cpu_count()))
        if self.need_multiprocess(list_g6_in, number_cores) and self.is_forced_to_terminate != 1.0:
            manager_class = mp.Manager()
            number_cores = int(np.ceil((1 / 3) * os.cpu_count()))
            list_broken_in = self.subdivide_input_list(number_cores)
            list_broken_out = manager_class.list(range(number_cores))
            list_of_process = []
            for k, list_in in enumerate(list_broken_in):
                if self.is_forced_to_terminate.value == 1.0:
                    return
                single_process = mp.Process(target=self.filter_multiprocess, args=(list_in, k, list_broken_out,))
                list_of_process.append(single_process)
                single_process.start()
            for single_process in list_of_process:
                single_process.join()
                self.update_to_progress_bar.value = self.total
            for list_in in list_broken_out:
                self.list_out += list_in
            return
        else:
            list_out = [None] * 1
            self.filter_multiprocess(self.list_g6_in, 0, list_out)
            self.list_out = list_out[0]
            return

    def filter_multiprocess(self, list_g6_in, i, list_out):
        list_out_temp = []
        for g6code in list_g6_in:
            if self.is_forced_to_terminate.value == 1.0:
                try:
                    multiprocessing.current_process().terminate()
                    return
                except AttributeError:
                    return
            self.update_to_progress_bar.value = self.update_to_progress_bar.value + 1
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if self.graph_satisfies_conditions(g):
                        list_out_temp.append(g6code)
            except Exception:
                continue
        list_out[i] = list_out_temp

    def start_find_example(self, list_g6_in, expression, list_inv_bool_choices):
        self.set_inputs(list_g6_in, expression, list_inv_bool_choices)
        number_cores = int(np.ceil((1 / 3) * os.cpu_count()))
        if self.need_multiprocess(list_g6_in, number_cores):
            manager_class = mp.Manager()
            list_broken_in = self.subdivide_input_list(number_cores)
            list_broken_out = manager_class.list(range(number_cores))
            list_of_process = []
            for k, list_in in enumerate(list_broken_in):
                single_process = mp.Process(target=self.find_example_multiprocess, args=(list_in, k, list_broken_out,))
                list_of_process.append(single_process)
                single_process.start()
            for single_process in list_of_process:
                single_process.join()
                self.update_to_progress_bar.value = self.total
            for element in list_broken_out:
                if element != "":
                    self.list_out.append(element)
                    return True
            return False
        else:
            list_out = [None] * 1
            self.find_example_multiprocess(self.list_g6_in, 0, list_out)
            if list_out[0] == "":
                return False
            else:
                self.list_out.append(list_out[0])
                return True

    def find_example_multiprocess(self, list_g6_in, i, list_out):
        list_out[i] = ""
        for g6code in list_g6_in:
            if self.is_forced_to_terminate.value == 1.0:
                try:
                    multiprocessing.current_process().terminate()
                    return
                except AttributeError:
                    return
            if self.update_to_progress_bar == self.total:
                return
            self.update_to_progress_bar.value = self.update_to_progress_bar.value + 1
            if g6code == '' or g6code == ' ':
                continue
            try:
                g = nx.from_graph6_bytes(g6code.encode('utf-8'))
                if self.graph_satisfies_equation(g):
                    if self.graph_satisfies_conditions(g):
                        # list_out_temp.append(g6code)
                        list_out[i] = g6code
                        self.update_to_progress_bar.value = self.total
                        return
                        # break
            except Exception:
                continue
        # list_out[i] = list_out_temp

    def subdivide_input_list(self, parts):
        n_sub = int(np.ceil(self.total / parts))
        return [self.list_g6_in[i:i + n_sub] for i in range(0, self.total, n_sub)]

    def graph_satisfies_equation(self, g):
        names = {**{"G": g, "g": g}, **dic_math_const}
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

    def need_multiprocess(self, list_g6_in, number_process):
        if len(list_g6_in) < number_process:
            return False
        graph_is_valid = False
        fails = 0
        while not graph_is_valid:
            choices = random.choices(population=list_g6_in, k=2)
            try:
                g1 = nx.from_graph6_bytes(choices[0].encode('utf-8'))
                g2 = nx.from_graph6_bytes(choices[1].encode('utf-8'))
                graph_is_valid = True
            except Exception:
                graph_is_valid = False
                fails += 1
                if fails > 10:
                    return False

        start = time.time()
        self.graph_satisfies_equation(g1)
        self.graph_satisfies_conditions(g1)
        self.graph_satisfies_equation(g2)
        self.graph_satisfies_conditions(g2)
        end = time.time()
        if (end - start) * len(list_g6_in) > 30:
            return True
        else:
            return False
