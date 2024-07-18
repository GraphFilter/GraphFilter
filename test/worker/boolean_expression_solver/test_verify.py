import itertools
import unittest

import networkx as nx
from parameterized import parameterized

from source.worker.boolean_expression_solver import BooleanExpressionSolver, Properties
from source.domain.entities import MathOperations, NumericStructuralInvariants

valid_equation_prioritized = [
    ("{expression} AND ({expression} OR {expression})", "n(G) + n(G) ≤ 1"),
    ("({expression} AND {expression}) OR {expression}", "n(G) + n(G) ≤ 1"),
    ("{expression} AND {expression} OR ({expression} AND {expression})", "n(G) + n(G) ≤ 1"),
    ("({expression} AND {expression}) OR {expression} AND {expression}", "n(G) + n(G) ≤ 1"),
    ("{expression} AND ({expression} OR {expression}) AND {expression}", "n(G) + n(G) ≤ 1"),
    ("({expression} AND {expression}) OR ({expression} AND {expression})", "n(G) + n(G) ≤ 1"),
    ("(({expression} AND {expression}) OR {expression}) AND {expression}", "n(G) + n(G) ≤ 1"),
    ("{expression} AND ({expression} OR ({expression} AND {expression}))", "n(G) + n(G) ≤ 1"),
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
        self.properties = Properties(functions=[MathOperations.Sin(), MathOperations.Cos(),
                                                NumericStructuralInvariants.NumberVertices()],
                                     names={"x": 5, "y": 3, "G": nx.path_graph(2)})

    def test_valid_equation(self):
        expression = "n(G) ≤ 1"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        self.solver.verify()

    def test_valid_equation_with_logic_operator(self):
        expression = "n(G) ≤ 1 AND n(G) > 0"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        self.solver.verify()

    def test_invalid_equation_nonexistent_function(self):
        expression = "func(1) + cos(1) ≤ 1"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        with self.assertRaises(ValueError) as context:
            self.solver.verify()

        expected_error_message = "Function 'func' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation_open_parenthesis(self):
        expression = "sin(1"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "'(' was never closed"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation(self):
        expression = "1 . 2 > 3"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "invalid syntax"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_outer_parentheses_equation(self):
        expression = "(1 > 0 AND 1 > 0 ))"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "unmatched ')'"
        self.assertIn(expected_error_message, str(context.exception))

    @parameterized.expand(valid_equation_prioritized)
    def test_valid_equation_with_logic_operator_and_parenthesis(self, template_expression, expression):
        self.solver = BooleanExpressionSolver(
            template_expression.format(expression=expression), self.properties
        )

        self.solver.verify()

    @parameterized.expand(invalid_equation_nonexistent_function_prioritized)
    def test_invalid_equation_nonexistent_function_and_parenthesis(self, template_expression, expression,
                                                                   invalid_expression):
        self.solver = BooleanExpressionSolver(
            template_expression.format(expression=expression, invalid_expression=invalid_expression),
            self.properties
        )

        with self.assertRaises(ValueError) as context:
            self.solver.verify()

        expected_error_message = "Function 'func' not defined"
        self.assertIn(expected_error_message, str(context.exception))

    def test_invalid_equation_with_parenthesis(self):
        expression = "1 . 2 > 3"
        self.solver = BooleanExpressionSolver(expression, self.properties)

        with self.assertRaises(AttributeError) as context:
            self.solver.verify()

        expected_error_message = "invalid syntax"
        self.assertIn(expected_error_message, str(context.exception))


if __name__ == '__main__':
    unittest.main()
