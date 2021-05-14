import networkx as nx
import numpy as np


class MathOperations:
    code = None
    code_literal = None
    name = None
    is_a_function = None
    all = []

    def __init__(self):
        self.all = MathOperations.__subclasses__()
        self.dic_function: {str: staticmethod} = {}
        self.dic_name_inv: {str: MathOperations} = {}
        for i, inv in enumerate(self.all):
            inv.code_literal = 'mop' + str(i)
            self.dic_function[inv.code_literal] = inv.calculate
            self.dic_name_inv[inv.name] = inv

    @staticmethod
    def calculate(graph):
        pass


class BasicMathOperations:
    code = None
    name = None
    is_a_function = None
    all = []

    def __init__(self):
        self.all = BasicMathOperations.__subclasses__()
        self.dic_name_inv: {str: BasicMathOperations} = {}
        for inv in self.all:
            self.dic_name_inv[inv.name] = inv


class GraphOperations:
    code = None
    code_literal = None
    name = None
    is_a_function = None
    all = []

    def __init__(self):
        self.all = GraphOperations.__subclasses__()
        self.dic_function: {str: staticmethod} = {}
        self.dic_name_inv: {str: GraphOperations} = {}
        for i, inv in enumerate(self.all):
            inv.code_literal = 'gop' + str(i)
            self.dic_function[inv.code_literal] = inv.calculate
            self.dic_name_inv[inv.name] = inv

    @staticmethod
    def calculate(graph):
        pass


class Complement(GraphOperations):
    name = "Complement"
    code = "Comp"
    is_a_function = True

    @staticmethod
    def calculate(graph):
        return nx.complement(graph)


class Line(GraphOperations):
    name = "Line"
    code = "\u2113"
    is_a_function = True

    @staticmethod
    def calculate(graph):
        return nx.line_graph(graph)


class Graph(GraphOperations):
    name = "Graph"
    code = "G"
    is_a_function = False


class Sin(MathOperations):
    name = "sin"
    code = "sin"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Cos(MathOperations):
    name = "cos"
    code = "cos"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Tan(MathOperations):
    name = "tan"
    code = "tan"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.tan(x)


class Log(MathOperations):
    name = "Logarithm in base 10"
    code = "log"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.log10(x)


class Ln(MathOperations):
    name = "Natural Logarithm"
    code = "ln"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.log(x)


class Sqrt(MathOperations):
    name = "Square root"
    code = "sqrt"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.sqrt(x)


class Absolute(MathOperations):
    name = "Absolute"
    code = "abs"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.abs(x)


class Plus(BasicMathOperations):
    name = "Sum"
    code = "+"
    is_a_function = False


class Subtraction(BasicMathOperations):
    name = "Subtraction"
    code = "-"
    is_a_function = False


class Division(BasicMathOperations):
    name = "Division"
    code = "/"
    is_a_function = False


class Product(BasicMathOperations):
    name = "Product"
    code = "*"
    is_a_function = False


class Power(BasicMathOperations):
    name = "Power"
    code = "**"
    is_a_function = False


class Modulus(BasicMathOperations):
    name = "Modulus"
    code = "%"
    is_a_function = False


class Equal(BasicMathOperations):
    name = "Equal"
    code = "=="
    is_a_function = False


class LogicAND(BasicMathOperations):
    name = "Logic AND"
    code = " AND "
    is_a_function = False


class LogicOR(BasicMathOperations):
    name = "Logic OR"
    code = " OR "
    is_a_function = False


class LessThan(BasicMathOperations):
    name = "Less than"
    code = "<"
    is_a_function = False


class GreaterThan(BasicMathOperations):
    name = "Greater than"
    code = ">"
    is_a_function = False


class LessThanEqual(BasicMathOperations):
    name = "Less than or equal"
    code = "<="
    is_a_function = False


class GreaterThanEqual(BasicMathOperations):
    name = "Greater than or equal"
    code = ">="
    is_a_function = False
