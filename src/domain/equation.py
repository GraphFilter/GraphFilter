import networkx as nx
from simpleeval import simple_eval
import numpy
from src.store.operations_invariants import *


class Equation:

    @staticmethod
    def split_translate_expression(expression):
        for inv in operations_invariants.graphOperations.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")
        for inv in operations_invariants.mathOperations.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")
        for inv in operations_invariants.numInvariant.all:
            expression = str(expression).replace(inv.code + "(", inv.code_literal + "(")

        if "AND" in expression and "OR" in expression:
            return '', 'error'
        elif "AND" in expression:
            return expression.replace(" ", "").split("AND"), 'AND'
        elif "OR" in expression:
            return expression.replace(" ", "").split("OR"), 'OR'
        else:
            return expression.replace(" ", ""), 'SINGLE'

    @staticmethod
    def validate_expression(expression):
        if len(expression) == 0:
            return ""
        expressions, and_or = Equation.split_translate_expression(expression)
        if and_or == 'error':
            return "Expression using 'AND' and 'OR' simultaneously is not allowed"
        try:
            if and_or == 'SINGLE':
                if not Equation.valid_bool_simple_eval(expressions):
                    return "It's not a valid equation or inequality"
            elif and_or == 'AND' or and_or == 'OR':
                for exp in expressions:
                    if not Equation.valid_bool_simple_eval(exp):
                        return "It's not a valid equation or inequality"
        except:
            return "Unknown terms in the expression"
        return ""

    @staticmethod
    def valid_bool_simple_eval(expression):
        g = nx.trivial_graph()
        names = {"G": g, "g": g}
        type_ex = type(simple_eval(expression, functions=dic_function_to_eval, names=names))
        return type_ex == numpy.bool or type_ex == numpy.bool_ or type_ex == bool
