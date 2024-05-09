import numpy as np

from source.domain.entities.functions import Function


class MathOperations:

    @staticmethod
    def calculate(graph):
        pass

    class Sin(Function):

        def __init__(self):
            super().__init__("sin")

        def calculate(self, x):
            return np.sin(x)

    class Cos(Function):

        def __init__(self):
            super().__init__("cos")

        def calculate(self, x):
            return np.cos(x)

    class Tan(Function):

        def __init__(self):
            super().__init__("tan")

        def calculate(self, x):
            return np.tan(x)

    class Log(Function):

        def __init__(self):
            super().__init__("log")

        def calculate(self, x):
            return np.log10(x)

    class Ln(Function):

        def __init__(self):
            super().__init__("ln")

        def calculate(self, x):
            return np.log(x)

    class Sqrt(Function):

        def __init__(self):
            super().__init__("sqrt")

        def calculate(self, x):
            return np.sqrt(x)

    class Absolute(Function):

        def __init__(self):
            super().__init__("abs")

        def calculate(self, x):
            return np.abs(x)

    class Floor(Function):

        def __init__(self):
            super().__init__("floor")

        def calculate(self, x):
            return np.floor(x)

    class Ceiling(Function):

        def __init__(self):
            super().__init__("ceiling")

        def calculate(self, x):
            return np.ceil(x)
