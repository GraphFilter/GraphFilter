import itertools
import unittest

from parameterized import parameterized

from source.domain.entities.operations.math_operations import MathOperations
from source.domain.expression_solver import ExpressionSolver

valid_equation_prioritized = [
    ("{expression} AND ({expression} OR {expression})", "sin(1) + cos(1) ≤ 1"),
    ("({expression} AND {expression}) OR {expression}", "sin(1) + cos(1) ≤ 1"),
    ("{expression} AND {expression} OR ({expression} AND {expression})", "sin(1) + cos(1) ≤ 1"),
    ("({expression} AND {expression}) OR {expression} AND {expression}", "sin(1) + cos(1) ≤ 1"),
    ("{expression} AND ({expression} OR {expression}) AND {expression}", "sin(1) + cos(1) ≤ 1"),
    ("({expression} AND {expression}) OR ({expression} AND {expression})", "sin(1) + cos(1) ≤ 1"),
    ("(({expression} AND {expression}) OR {expression}) AND {expression}", "sin(1) + cos(1) ≤ 1"),
    ("{expression} AND ({expression} OR ({expression} AND {expression}))", "sin(1) + cos(1) ≤ 1"),
]

expressions_type = ["{invalid_expression}", "{expression}"]

invalid_equation_nonexistent_function_prioritized = list(itertools.chain(
    *[
        [(f"{c[0]} AND ({c[1]} OR {c[2]} AND {c[3]})", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1],
        [(f"({c[0]} AND {c[1]}) OR {c[2]} AND {c[3]}", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1],
        [(f"{c[0]} AND ({c[1]} OR {c[2]}) AND {c[3]}", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1],
        [(f"{c[0]} AND {c[1]} OR ({c[2]} AND {c[3]})", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1],
        [(f"(({c[0]} AND {c[1]}) OR {c[2]}) AND {c[3]}", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1],
        [(f"{c[0]} AND ({c[1]} OR ({c[2]} AND {c[3]}))", "sin(1) + cos(1) ≤ 1", "func(1) + cos(1) ≤ 1")
         for c in itertools.product(expressions_type, repeat=4) if len(set(c)) > 1]
    ]
))


class TestVerify(unittest.TestCase):

    def setUp(self):
        self.functions = [MathOperations.Sin(), MathOperations.Cos()]
        self.names = {"x": 5, "y": 3}

    def test_valid_equation(self):
        expression = "sin(1) + cos(1) ≤ 1"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        self.solver.verify()

    def test_valid_equation_with_logic_operator(self):
        expression = "sin(1) + cos(1) ≤ 1 AND sin(1) == 0"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        self.solver.verify()

    def test_invalid_equation_nonexistent_function(self):
        expression = "func(1) + cos(1) ≤ 1"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(ValueError) as context:
            self.solver.verify()

        expected_error_message = "Function 'func' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation_open_parenthesis(self):
        expression = "sin(1"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "'(' was never closed"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation(self):
        expression = "1 . 2 > 3"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "invalid syntax"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation_syntax_with_function(self):
        expression = " n(G) ≥ 0 λ₁()"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "invalid syntax"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_outer_parentheses_equation(self):
        expression = "(1 > 0 AND 1 > 0 ))"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "unmatched ')'"
        self.assertIn(expected_error_message, str(context.exception))

    @parameterized.expand(valid_equation_prioritized)
    def test_valid_equation_with_logic_operator_and_parenthesis(self, template_expression, expression):
        self.solver = ExpressionSolver(
            template_expression.format(expression=expression), functions=self.functions, names=self.names
        )

        self.solver.verify()

    @parameterized.expand(invalid_equation_nonexistent_function_prioritized)
    def test_invalid_equation_nonexistent_function_and_parenthesis(self, template_expression, expression,
                                                                   invalid_expression):
        self.solver = ExpressionSolver(
            template_expression.format(expression=expression, invalid_expression=invalid_expression),
            functions=self.functions, names=self.names
        )

        with self.assertRaises(ValueError) as context:
            self.solver.verify()

        expected_error_message = "Function 'func' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation_with_parenthesis(self):
        expression = "1 . 2 > 3"
        self.solver = ExpressionSolver(expression, functions=self.functions, names=self.names)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "invalid syntax"
        self.assertIn(expected_error_message, str(context.exception))


if __name__ == '__main__':
    unittest.main()
