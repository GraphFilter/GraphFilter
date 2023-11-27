import unittest

from source.domain.entities.operations.math_operations import MathOperations
from source.domain.expression_solver import ExpressionSolver


class TestBuild(unittest.TestCase):

    def setUp(self):
        self.functions = [MathOperations.Sin(), MathOperations.Cos()]
        self.names = {"x": 5, "y": 3}

    def test_valid_equation(self):
        expression = "sin(1) + cos(1) ≤ 1"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_valid_equation_with_logic_operator(self):
        expression = "sin(1) + cos(1) ≤ 1 AND x > 5"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_equation_with_invalid_logic_operator(self):
        expression = "sin(1) + cos(1) ≤ 1 VERSUS x > 5"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_ternary_numeric_expression_prioritized_beginning(self):
        expression = "(sin(1) AND cos(1)) OR sin(1)"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_ternary_numeric_expression_prioritized_end(self):
        expression = "sin(1) AND (cos(1) OR sin(1))"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_prioritized_beginning(self):
        expression = "(sin(1) AND cos(1)) OR sin(1) AND cos(1)"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_prioritized_end(self):
        expression = "sin(1) AND cos(1) OR (sin(1) AND cos(1))"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_prioritized_middle(self):
        expression = "sin(1) AND (cos(1) OR sin(1)) AND cos(1)"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_prioritized_chained_beginning(self):
        expression = "((sin(1) AND cos(1)) OR sin(1)) AND cos(1)"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_prioritized_chained_end(self):
        expression = "sin(1) AND (cos(1) OR (sin(1) AND cos(1)))"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)

    def test_quaternary_numeric_expression_with_two_prioritized(self):
        expression = "(sin(1) AND cos(1)) OR (sin(1) AND cos(1))"

        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        expression_built = self.solver.build()
        self.assertEqual(expression, expression_built)


if __name__ == '__main__':
    unittest.main()
