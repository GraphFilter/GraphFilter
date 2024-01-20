from sandbox import Sandbox
from source.domain.boolean_expression_solver import Properties
from source.domain.entities import Function, Operator, Calculator


class SandboxKeyboard(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


class Variables:
    class X(Operator, Calculator):
        def __init__(self):
            super().__init__("x")

        def calculate(self, x):
            return 10


class MockFunctions:
    class MockFunction(Function):
        def __init__(self):
            super().__init__("f")

        def calculate(self, x):
            return 5


if __name__ == '__main__':
    sandbox = SandboxKeyboard()
    sandbox.instantiate_element(Properties(operators=[MockFunctions.MockFunction(), Variables.X()],
                                           functions=[MockFunctions.MockFunction()], names={"x": 10}))
    sandbox.start()
