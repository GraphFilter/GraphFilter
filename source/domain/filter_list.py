import os

from simpleeval import simple_eval
from source.store.operations_invariants import *
from source.domain.equation import Equation
import numpy as np
import multiprocessing as mp
from ctypes import c_char_p
import dill

class FilterList():

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

        self.update_to_progress_bar = None

        # NOTE: list_g6_in: list with graphs6 string
        #  expression: (in)equation string with AND OR
        #  list_inv_bool_choices: dict of couples {invariant_name: 'true' or 'false'}
        self.functions_to_eval.update(dic_function_to_eval)

    def set_inputs(self, list_g6_in, expression, list_inv_bool_choices, update):
        self.satisfied_graphs = 0
        self.list_out.clear()
        self.list_g6_in = list_g6_in
        self.total = len(self.list_g6_in)
        self.list_inv_bool_choices = list_inv_bool_choices
        self.expressions, self.AND_OR = Equation.split_translate_expression(expression)
        self.update_to_progress_bar = update

    def start_filter(self, list_g6_in, expression, list_inv_bool_choices, update):
        # counterexample
        # filter
        mp.freeze_support()
        self.set_inputs(list_g6_in, expression, list_inv_bool_choices, update)
        if self.total > 10:
            manager = mp.Manager()
            cores=4
            list_breaked_in = subdivide_input_list(list_g6_in, cores)
            list_breaked_out = manager.list(range(cores))
            list_process=[]
            for i, list in enumerate(list_breaked_in):
                # process = mp.Process(
                #     target=filter_multiprocess,
                #     args=(list, i, list_breaked_out, self,)
                # )
                process = apply_multiprocess(
                    mp,
                    function=filter_multiprocess,
                    args=(list, i, list_breaked_out, self,)
                )
                list_process.append(process)
                process.start()
            for process in list_process:
                process.join()
                process.close()
            for list in list_breaked_out:
                self.list_out += list
            return float(len(self.list_out) / self.total)
        else:
            # self.filter_singleprocess(self.list_g6_in)
            list_out = [None]*1
            filter_multiprocess(self.list_g6_in, 0, list_out, self)
            self.list_out = list_out[0]
            return float(len(self.list_out) / self.total)


    def start_find_counterexample(self, list_g6_in, expression, list_inv_bool_choices, update):
        self.set_inputs(list_g6_in, expression, list_inv_bool_choices, update)
        manager = mp.Manager()
        graph_out = manager.Value(c_char_p, '')
        if self.total > 10:
            cores=4
            list_breaked_in = subdivide_input_list(list_g6_in,cores)
            list_process=[]
            for i, list in enumerate(list_breaked_in):
                process = mp.Process(
                    target=find_counterexample_multiprocess,
                    args=(list, graph_out, self,)
                )
                list_process.append(process)
                process.start()
            for process in list_process:
                process.join()
                process.close()
        else:
            find_counterexample_multiprocess(self.list_g6_in, graph_out, self)
        if graph_out.value:
            self.list_out.append(graph_out.value)
            return True
        else:
            return False


def filter_multiprocess(list_g6_in, i, list_out, filter_class):
    list_out_temp = []
    for g6code in list_g6_in:
        # filter_class.update_to_progress_bar()
        if g6code == '' or g6code == ' ':
            continue
        try:
            g = nx.from_graph6_bytes(g6code.encode('utf-8'))
            if graph_satisfies_equation(g, filter_class):
                if graph_satisfies_conditions(g, filter_class):
                    list_out_temp.append(g6code)
        except Exception:
            continue
    # self.satisfied_graphs = self.satisfied_graphs + len(list_out)
    list_out[i] = list_out_temp

def find_counterexample_multiprocess(list_g6_in, graph_out, filter_class):
    for g6code in list_g6_in:
        if graph_out.value != '':
            return True
        # filter_class.update_to_progress_bar()
        if g6code == '' or g6code == ' ':
            continue
        try:
            g = nx.from_graph6_bytes(g6code.encode('utf-8'))
            if not graph_satisfies_equation(g, filter_class):
                graph_out.value=g6code
                return True
            else:
                if not graph_satisfies_conditions(g, filter_class):
                    graph_out.value=g6code
                    return True
        except Exception:
            continue
    return ''
    # self.satisfied_graphs = self.satisfied_graphs + len(list_out)

def subdivide_input_list(list_g6_in, parts):
    total = len(list_g6_in)
    n_sub = int(np.ceil(total / parts))
    return [list_g6_in[i:i + n_sub] for i in range(0, total, n_sub)]

def graph_satisfies_equation(g, filter):

    names = {**{"G": g, "g": g}, **dic_math_const}
    # Check the expressions
    if len(filter.expressions) > 0:
        if filter.AND_OR == 'SINGLE':
            return simple_eval(filter.expressions, functions=filter.functions_to_eval, names=names)
        elif filter.AND_OR == 'AND':
            for exp in filter.expressions:
                if not simple_eval(exp, functions=filter.functions_to_eval, names=names):
                    return False
            return True
        elif filter.AND_OR == "OR":
            for exp in filter.expressions:
                if simple_eval(exp, functions=filter.functions_to_eval, names=names):
                    return True
            return False
    return True


def graph_satisfies_conditions(g, filter):
    for inv_name in filter.list_inv_bool_choices:
        if filter.list_inv_bool_choices[inv_name] == 'true':
            graph_satisfies = dic_bool_invariants_names[inv_name].calculate(g)
        else:
            graph_satisfies = not dic_bool_invariants_names[inv_name].calculate(g)
        if not graph_satisfies:
            return False
    return True

def run_dill_encoded(payload):
    fun, args = dill.loads(payload)
    return fun(*args)


def apply_multiprocess(multiprocess: mp, function, args):
    payload = dill.dumps((function, args))
    return multiprocess.Process(run_dill_encoded, (payload,))


if __name__ == "__main__":
    print("teste")