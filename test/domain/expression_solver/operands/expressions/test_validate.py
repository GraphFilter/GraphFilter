import unittest

from source.domain.expression_solver import LogicExpression
from source.domain.entities.operations.math_operations import MathOperations


class TestValidate(unittest.TestCase):

    def setUp(self):
        self.functions = [MathOperations.Sin(), MathOperations.Cos()]
        self.valid_names = {"x": 5, "y": 3}
        self.symbols = [MathOperations.Sin(), MathOperations.Cos()]

    def test_valid_equation(self):
        expression = "sin(1) + cos(1) <= 1"

        LogicExpression(expression, self.functions, self.valid_names, self.symbols).validate()

    def test_undefined_name(self):
        invalid_expression = "z + 2  > 0"

        with self.assertRaises(ValueError) as context:
            LogicExpression(invalid_expression, self.functions, self.valid_names, self.symbols).validate()

        expected_error_message = "Name 'z' is not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_undefined_function(self):
        invalid_expression = "f(x) + y <= 10"

        with self.assertRaises(ValueError) as context:
            LogicExpression(invalid_expression, self.functions, self.valid_names, self.symbols).validate()

        expected_error_message = "Function 'f' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_expression(self):
        invalid_expression = "x . 2 <= 10"

        with self.assertRaises(Exception) as context:
            LogicExpression(invalid_expression, self.functions, self.valid_names, self.symbols).validate()


if __name__ == '__main__':
    unittest.main()
