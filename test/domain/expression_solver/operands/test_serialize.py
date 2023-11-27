import unittest

from source.domain.entities.operations.math_operations import MathOperations
from source.domain.expression_solver import LogicExpression, AND


class TestSerialize(unittest.TestCase):
    def setUp(self):
        self.functions = [MathOperations.Sin(), MathOperations.Cos()]
        self.names = {"x": 5, "y": 3}
        self.symbols = [MathOperations.Sin(), MathOperations.Cos()]

    def test_unary_numeric_expression(self):
        expression = "sin(1)"

        operand_tree = LogicExpression("sin(1)", self.functions, self.names, self.symbols)
        serialized_expression = operand_tree.serialize()
        self.assertEqual(expression, serialized_expression)

    def test_binary_numeric_expression(self):
        expression = "sin(1) AND cos(1)"

        operand_tree = AND()
        operand_tree.left = LogicExpression("sin(1)", self.functions, self.names, self.symbols)
        operand_tree.right = LogicExpression("cos(1)", self.functions, self.names, self.symbols)

        serialized_expression = operand_tree.serialize()
        self.assertEqual(expression, serialized_expression)


if __name__ == '__main__':
    unittest.main()
