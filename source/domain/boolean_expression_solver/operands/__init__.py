from abc import ABC, abstractmethod

from source.domain.boolean_expression_solver.node import Node


class Operand(Node, ABC):
    def __init__(self, expression: str = ""):
        super().__init__(expression)
        self.left: Operand = None
        self.right: Operand = None

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def solve(self):
        if self.left is None and self.right is None:
            return self.calculate()

        return self.left.solve() or self.right.solve()

    def inspect(self):
        try:
            if self.left is None and self.right is None:
                return self.validate()

            left_result = self.left.inspect() if self.left else True
            right_result = self.right.inspect() if self.right else True

            if self.__class__.__name__ == "LogicExpression":
                return self.validate() and left_result and right_result
            else:
                return left_result and right_result

        except Exception as e:
            raise e
