import networkx as nx
import numpy as np


class math_operations:
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        for subclass in math_operations.__subclasses__():
            self.all.append(subclass)
            self.dic_function[subclass.code] = subclass.Calculate

    @staticmethod
    def Calculate(graph):
        pass


class graph_operations:
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        self.all = graph_operations.__subclasses__()
        '''
        data = pd.read_excel(os.path.abspath('invariants_data.xlsx'), sheet_name='Operation')
        line = 0
        for subclass in self.all:
            subclass.defi = data.loc[line].at['Definition']
            subclass.link = data.loc[line].at['Link']
            subclass.implement = data.loc[line].at['Implementation']
        '''
        for subclass in graph_operations.__subclasses__():
            self.all.append(subclass)
            self.dic_function[subclass.code] = subclass.Calculate

    name = None
    defi = None
    link = None
    implement = None

    @staticmethod
    def Calculate(graph):
        pass


class complement(graph_operations):
    name = "Complement of graph"
    code = "c"

    @staticmethod
    def Calculate(graph):
        return nx.complement(graph)


class line(graph_operations):
    name = "Line of graph"
    code = "l"

    @staticmethod
    def Calculate(graph):
        return nx.line_graph(graph)


class sin(math_operations):
    name = "sin"
    code = "sin"

    @staticmethod
    def Calculate(x):
        return np.sin(x)


class cos(math_operations):
    name = "cos"
    code = "cos"

    @staticmethod
    def Calculate(x):
        return np.sin(x)


class tan(math_operations):
    name = "tan"
    code = "tan"

    @staticmethod
    def Calculate(x):
        return np.tan(x)


class log(math_operations):
    name = "Logarithm in base 10"
    code = "log"

    @staticmethod
    def Calculate(x):
        return np.log10(x)


class ln(math_operations):
    name = "Natural Logarithm"
    code = "ln"

    @staticmethod
    def Calculate(x):
        return np.log(x)


class sqrt(math_operations):
    name = "Square root"
    code = "sqrt"

    @staticmethod
    def Calculate(x):
        return np.sqrt(x)


class absolute(math_operations):
    name = "Absolute"
    code = "abs"

    @staticmethod
    def Calculate(x):
        return np.abs(x)
