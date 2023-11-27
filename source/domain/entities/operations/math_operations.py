from source.domain.objects.function_object import FunctionObject
import numpy as np

from source.domain.entities.operations import Operation


class MathOperations:

    @staticmethod
    def calculate(graph):
        pass

    class Sin(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="sin", code="sin")

        def calculate(self, x):
            return np.sin(x)

    class Cos(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="cos", code="cos")

        def calculate(self, x):
            return np.cos(x)

    class Tan(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="tan", code="tan")

        def calculate(self, x):
            return np.tan(x)

    class Log(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Logarithm in base 10", code="log")

        def calculate(self, x):
            return np.log10(x)

    class Ln(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Natural Logarithm", code="ln")

        def calculate(self, x):
            return np.log(x)

    class Sqrt(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Square root", code="sqrt")

        def calculate(self, x):
            return np.sqrt(x)

    class Absolute(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Absolute", code="abs")

        def calculate(self, x):
            return np.abs(x)

    class Floor(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Floor", code="floor")

        def calculate(self, x):
            return np.floor(x)

    class Ceiling(Operation, FunctionObject):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(name="Ceiling", code="ceiling")

        def calculate(self, x):
            return np.ceil(x)
