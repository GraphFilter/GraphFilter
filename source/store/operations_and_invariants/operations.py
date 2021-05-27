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
        self.dic_math_symbols: {str: str} = {"<=": "\u2264", ">=": "\u2265", "!=": "\u2260", "**": "^", "pi": "\u03c0"}
        self.dic_math_const = {"pi": np.pi}
        for inv in self.all:
            self.dic_name_inv[inv.name] = inv
            inv.is_a_function = False


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

class CliqueGraph(GraphOperations):
    name = "Clique Operator (maximal)"
    code = "\u0198"
    is_a_function = True

    @staticmethod
    def calculate(graph):
        return nx.make_max_clique_graph(graph)


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


class Floor(MathOperations):
    name = "Floor"
    code = "floor"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.floor(x)


class Ceiling(MathOperations):
    name = "Ceiling"
    code = "ceiling"
    is_a_function = True

    @staticmethod
    def calculate(x):
        return np.ceil(x)


class Plus(BasicMathOperations):
    name = "Sum"
    code = "+"


class Subtraction(BasicMathOperations):
    name = "Subtraction"
    code = "-"


class Division(BasicMathOperations):
    name = "Division"
    code = "/"


class Product(BasicMathOperations):
    name = "Product"
    code = "*"


class Power(BasicMathOperations):
    name = "Power"
    code = "**"


class Modulus(BasicMathOperations):
    name = "Modulus"
    code = "%"


class Equal(BasicMathOperations):
    name = "Equal"
    code = "=="


class LogicAND(BasicMathOperations):
    name = "Logic AND"
    code = " AND "


class LogicOR(BasicMathOperations):
    name = "Logic OR"
    code = " OR "


class LessThan(BasicMathOperations):
    name = "Less than"
    code = "<"


class GreaterThan(BasicMathOperations):
    name = "Greater than"
    code = ">"


class LessThanEqual(BasicMathOperations):
    name = "Less than or equal"
    code = "\u2264"


class GreaterThanEqual(BasicMathOperations):
    name = "Greater than or equal"
    code = "\u2265"


class Different(BasicMathOperations):
    name = "Different"
    code = "\u2260"


class PInumber(BasicMathOperations):
    name = "\u03c0"
    code = "\u03c0"
