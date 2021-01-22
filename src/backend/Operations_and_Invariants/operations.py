import networkx as nx
import numpy as np


class MathOperations:
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        for subclass in MathOperations.__subclasses__():
            self.all.append(subclass)
            self.dic_function[subclass.code] = subclass.calculate

    @staticmethod
    def calculate(graph):
        pass


class GraphOperations:
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        self.all = GraphOperations.__subclasses__()
        '''
        data = pd.read_excel(os.path.abspath('invariants_data.xlsx'), sheet_name='Operation')
        line = 0
        for subclass in self.all:
            subclass.defi = data.loc[line].at['Definition']
            subclass.link = data.loc[line].at['Link']
            subclass.implement = data.loc[line].at['Implementation']
        '''
        for subclass in GraphOperations.__subclasses__():
            self.all.append(subclass)
            self.dic_function[subclass.code] = subclass.calculate

    name = None
    defi = None
    link = None
    implement = None

    @staticmethod
    def calculate(graph):
        pass


class Complement(GraphOperations):
    name = "Complement of graph"
    code = "c"

    @staticmethod
    def calculate(graph):
        return nx.complement(graph)


class Line(GraphOperations):
    name = "Line of graph"
    code = "l"

    @staticmethod
    def calculate(graph):
        return nx.line_graph(graph)


class Sin(MathOperations):
    name = "sin"
    code = "sin"

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Cos(MathOperations):
    name = "cos"
    code = "cos"

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Tan(MathOperations):
    name = "tan"
    code = "tan"

    @staticmethod
    def calculate(x):
        return np.tan(x)


class Log(MathOperations):
    name = "Logarithm in base 10"
    code = "log"

    @staticmethod
    def calculate(x):
        return np.log10(x)


class Ln(MathOperations):
    name = "Natural Logarithm"
    code = "ln"

    @staticmethod
    def calculate(x):
        return np.log(x)


class Sqrt(MathOperations):
    name = "Square root"
    code = "sqrt"

    @staticmethod
    def calculate(x):
        return np.sqrt(x)


class Absolute(MathOperations):
    name = "Absolute"
    code = "abs"

    @staticmethod
    def calculate(x):
        return np.abs(x)
