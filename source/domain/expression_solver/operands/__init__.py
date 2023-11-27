from abc import ABC, abstractmethod

from source.domain.expression_solver.node import Node


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

            self.left.inspect()
            self.right.inspect()

        except Exception as e:
            raise e

    def serialize(self):

        if self.left is None and self.right is None:
            return self.value

        right = ""
        left = ""

        if self.__class__.__bases__[0].__name__ == 'Operator' and self.inverted:
            right = self.left.serialize()
            left = self.right.serialize()
        else:
            right = self.right.serialize()
            left = self.left.serialize()

        return f"{left} {self.value}{'' if right == '' else ' '}{right}"
