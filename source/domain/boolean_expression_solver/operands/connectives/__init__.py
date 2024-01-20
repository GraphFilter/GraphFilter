from source.domain.boolean_expression_solver.operands import Operand
from source.domain.entities import get_inner_classes, Operator


class Connectives:
    class AND(Operand, Operator):
        _allow_multiple = True

        def __init__(self):
            Operator.__init__(self, "AND")
            Operand.__init__(self, "AND")

        def calculate(self):
            return self.left and self.right

        def validate(self):
            pass

    class OR(Operand, Operator):
        _allow_multiple = True

        def __init__(self):
            Operator.__init__(self, "OR")
            Operand.__init__(self, "OR")

        def calculate(self):
            return self.left or self.right

        def validate(self):
            pass


LOGICAL_CONNECTIVES_VALUES = [cls.value for cls in get_inner_classes(Connectives)]
LOGICAL_CONNECTIVES = get_inner_classes(Connectives)
