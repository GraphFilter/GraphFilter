import networkx as nx
import numpy as np


class MathOperations:
    code = None
    dic_function = {}
    all = []

    def __init__(self):
        for subclass in MathOperations.__subclasses__():
            self.all.append(subclass)
            self.dic_function[subclass.code] = subclass.Calculate

    @staticmethod
    def Calculate(graph):
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
            self.dic_function[subclass.code] = subclass.Calculate

    name = None
    defi = None
    link = None
    implement = None

    @staticmethod
    def Calculate(graph):
        pass


class complement(GraphOperations):
    name = "Complement of graph"
    code = "c"

    @staticmethod
    def Calculate(graph):
        return nx.complement(graph)


class line(GraphOperations):
    name = "Line of graph"
    code = "l"

    @staticmethod
    def Calculate(graph):
        return nx.line_graph(graph)


class sin(MathOperations):
    name = "sin"
    code = "sin"

    @staticmethod
    def Calculate(x):
        return np.sin(x)


class cos(MathOperations):
    name = "cos"
    code = "cos"

    @staticmethod
    def Calculate(x):
        return np.sin(x)


class tan(MathOperations):
    name = "tan"
    code = "tan"

    @staticmethod
    def Calculate(x):
        return np.tan(x)


class log(MathOperations):
    name = "Logarithm in base 10"
    code = "log"

    @staticmethod
    def Calculate(x):
        return np.log10(x)


class ln(MathOperations):
    name = "Natural Logarithm"
    code = "ln"

    @staticmethod
    def Calculate(x):
        return np.log(x)


class sqrt(MathOperations):
    name = "Square root"
    code = "sqrt"

    @staticmethod
    def Calculate(x):
        return np.sqrt(x)


class absolute(MathOperations):
    name = "Absolute"
    code = "abs"

    @staticmethod
    def Calculate(x):
        return np.abs(x)
