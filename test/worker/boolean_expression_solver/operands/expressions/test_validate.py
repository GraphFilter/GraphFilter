import unittest

from source.worker.boolean_expression_solver import LogicExpression, Properties
from source.domain.entities import MathOperations


class TestValidate(unittest.TestCase):

    def setUp(self):
        self.properties = Properties(functions=[MathOperations.Sin(), MathOperations.Cos()], names={"x": 5, "y": 3})

    def test_valid_equation(self):
        expression = "sin(1) + cos(1) <= 1"

        LogicExpression(self.properties.functions.decode(expression), self.properties).validate()

    def test_undefined_name(self):
        invalid_expression = "z + 2  > 0"

        with self.assertRaises(ValueError) as context:
            LogicExpression(invalid_expression, self.properties).validate()

        expected_error_message = "Name 'z' is not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_undefined_function(self):
        invalid_expression = "f(x) + y <= 10"

        with self.assertRaises(ValueError) as context:
            LogicExpression(invalid_expression, self.properties).validate()

        expected_error_message = "Function 'f' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_expression(self):
        invalid_expression = "x . 2 <= 10"

        with self.assertRaises(Exception) as context:
            LogicExpression(invalid_expression, self.properties).validate()


if __name__ == '__main__':
    unittest.main()
