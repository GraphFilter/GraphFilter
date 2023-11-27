from abc import abstractmethod

from source.domain.expression_solver.operands import Operand
from source.domain.objects.translation_object import TranslationObject


class Operator(Operand):
    def __init__(self, value=None, inverted=False):
        super().__init__(value)
        self.inverted = inverted

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def validate(self):
        pass


class AND(Operator):
    def __init__(self, inverted=False):
        super().__init__("AND", inverted)

    def calculate(self):
        return self.left and self.right

    def validate(self):
        pass


class OR(Operator):

    def __init__(self, inverted=False):
        super().__init__("OR", inverted)

    def calculate(self):
        return self.left or self.right

    def validate(self):
        pass


LOGICAL_OPERATORS = [cls().value for cls in Operator.__subclasses__()]
LOGICAL_OPERATORS_NAMES = [TranslationObject(cls.__name__, cls.__name__) for cls in Operator.__subclasses__()]
