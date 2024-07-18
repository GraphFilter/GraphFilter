import unittest

from parameterized import parameterized

from source.worker.boolean_expression_solver import BooleanExpressionSolver, Properties
from source.worker.boolean_expression_solver.node import Node
from source.domain.entities import MathOperations

unary_numeric_expressions = [
    ("1 + 1 == 2"),
    ("1 + 1 == 3"),
]

binary_conjunction_numeric_expressions = [
    ("1 + 1 == 2", "AND", "1 + 1 == 2", True),
    ("1 + 1 == 3", "AND", "1 + 1 == 2", False),
    ("1 + 1 == 2", "AND", "1 + 1 == 3", False),
    ("1 + 1 == 3", "AND", "1 + 1 == 4", False),
]

binary_disjunction_numeric_expressions = [
    ("1 + 1 == 2", "OR", "1 + 1 == 2", True),
    ("1 + 1 == 3", "OR", "1 + 1 == 2", True),
    ("1 + 1 == 2", "OR", "1 + 1 == 3", True),
    ("6 + 1 == 3", "OR", "1 + 1 == 4", False),
]

ternary_numeric_expressions = [
    ("1 + 1 == 2", "AND", "AND"),
    ("6 + 6 == 2", "OR", "AND"),
    ("6 + 6 == 2", "AND", "OR"),
    ("1 + 1 == 2", "OR", "OR"),
]

quaternary_numeric_expressions = [
    ("1 + 1 == 2", "AND", "AND", "AND"),
    ("1 + 1 == 2", "OR", "AND", "AND"),
    ("1 + 1 == 2", "AND", "OR", "AND"),
    ("1 + 1 == 2", "OR", "OR", "AND"),
    ("1 + 1 == 2", "AND", "AND", "OR"),
    ("1 + 1 == 2", "OR", "AND", "OR"),
    ("1 + 1 == 2", "AND", "OR", "OR"),
    ("1 + 1 == 2", "OR", "OR", "OR"),
]


class TestTreeCreation(unittest.TestCase):

    def setUp(self):
        self.properties = Properties(functions=[MathOperations.Sin(), MathOperations.Cos()], names={"x": 5, "y": 3})

    @parameterized.expand(unary_numeric_expressions)
    def test_unary_numeric_expression(self, expression):
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(expression)
        self.assertEqual(expected_tree, solver_tree)

    def test_unary_numeric_expression_with_function(self):
        expression = "sin(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("sin(1)")
        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(binary_conjunction_numeric_expressions + binary_disjunction_numeric_expressions)
    def test_binary_numeric_expression(self, expression1, logic_operand, expression2, result):
        expression = f"{expression1} {logic_operand} {expression2}"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand)
        expected_tree.left = Node(expression1)
        expected_tree.right = Node(expression2)

        self.assertEqual(expected_tree, solver_tree)

    def test_binary_numeric_expression_with_function(self):
        expression = "sin(1) AND cos(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("sin(1)")
        expected_tree.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(binary_conjunction_numeric_expressions + binary_disjunction_numeric_expressions)
    def test_binary_numeric_expression_prioritized(self, expression1, logic_operand, expression2, result):
        expression = f"{expression1} {logic_operand} ({expression2})"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand)
        expected_tree.left = Node(expression2)
        expected_tree.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_binary_numeric_expression_prioritized_with_function(self):
        expression = "sin(1) AND (cos(1))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("cos(1)")
        expected_tree.right = Node("sin(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(ternary_numeric_expressions)
    def test_ternary_numeric_expression(self, expression1, logic_operand1, logic_operand2):
        expression = f"""
            {expression1} {logic_operand1} {expression1} {logic_operand2} {expression1}
            """.strip()

        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_ternary_numeric_expression_with_function(self):
        expression = "sin(1) AND cos(1) OR sin(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("sin(1)")
        expected_tree.left.left = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(ternary_numeric_expressions)
    def test_ternary_numeric_expression_prioritized_beginning(self, expression1, logic_operand1, logic_operand2):
        expression = f"({expression1} {logic_operand1} {expression1}) {logic_operand2} {expression1}"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand2)
        expected_tree.left = Node(logic_operand1)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_ternary_numeric_expression_prioritized_beginning_with_function(self):
        expression = "(sin(1) AND cos(1)) OR sin(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("OR")
        expected_tree.left = Node("AND")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("sin(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(ternary_numeric_expressions)
    def test_ternary_numeric_expression_prioritized_end(self, expression1, logic_operand1, logic_operand2):
        expression = f"{expression1} {logic_operand1} ({expression1} {logic_operand2} {expression1})"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_ternary_numeric_expression_prioritized_end_with_function(self):
        expression = "sin(1) AND (cos(1) OR sin(1))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("sin(1)")
        expected_tree.left.left = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression(self, expression1, logic_operand1, logic_operand2, logic_operand3):
        expression = f"""
        {expression1} {logic_operand1} {expression1} {logic_operand2} {expression1} {logic_operand3} {expression1}
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(logic_operand3)
        expected_tree.left.left.left = Node(expression1)
        expected_tree.left.left.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_with_function(self):
        expression = "sin(1) AND cos(1) OR sin(1) AND cos(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("AND")
        expected_tree.left.left.left = Node("sin(1)")
        expected_tree.left.left.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_prioritized_beginning(self, expression1, logic_operand1, logic_operand2,
                                                                 logic_operand3):
        expression = f"""
        ({expression1} {logic_operand1} {expression1}) {logic_operand2} {expression1} {logic_operand3} {expression1}
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand2)
        expected_tree.left = Node(logic_operand1)
        expected_tree.right = Node(logic_operand3)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(expression1)
        expected_tree.right.left = Node(expression1)
        expected_tree.right.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_prioritized_beginning_with_function(self):
        expression = "(sin(1) AND cos(1)) OR sin(1) AND cos(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("OR")
        expected_tree.left = Node("AND")
        expected_tree.right = Node("AND")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("sin(1)")
        expected_tree.right.left = Node("sin(1)")
        expected_tree.right.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_prioritized_end(self, expression1, logic_operand1, logic_operand2,
                                                           logic_operand3):
        expression = f"""
        {expression1} {logic_operand1} {expression1} {logic_operand2} ({expression1} {logic_operand3} {expression1})
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(logic_operand3)
        expected_tree.left.left.left = Node(expression1)
        expected_tree.left.left.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_prioritized_end_with_function(self):
        expression = "sin(1) AND cos(1) OR (sin(1) AND cos(1))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("AND")
        expected_tree.left.left.left = Node("sin(1)")
        expected_tree.left.left.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_prioritized_middle(self, expression1, logic_operand1, logic_operand2,
                                                              logic_operand3):
        expression = f"""
        {expression1} {logic_operand1} ({expression1} {logic_operand2} {expression1}) {logic_operand3} {expression1}
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand3)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(logic_operand2)
        expected_tree.left.left.left = Node(expression1)
        expected_tree.left.left.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_prioritized_middle_with_function(self):
        expression = "sin(1) AND (cos(1) OR sin(1)) AND cos(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("AND")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("OR")
        expected_tree.left.left.left = Node("cos(1)")
        expected_tree.left.left.right = Node("sin(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_prioritized_chained_beginning(self, expression1, logic_operand1,
                                                                         logic_operand2, logic_operand3):
        expression = f"""
        (({expression1} {logic_operand1} {expression1}) {logic_operand2} {expression1}) {logic_operand3} {expression1}
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand3)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(logic_operand1)
        expected_tree.left.left.left = Node(expression1)
        expected_tree.left.left.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_prioritized_chained_beginning_with_function(self):
        expression = "((sin(1) AND cos(1)) OR sin(1)) AND cos(1)"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("cos(1)")
        expected_tree.left.right = Node("sin(1)")
        expected_tree.left.left = Node("AND")
        expected_tree.left.left.left = Node("sin(1)")
        expected_tree.left.left.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_prioritized_chained_end(self, expression1, logic_operand1,
                                                                   logic_operand2, logic_operand3):
        expression = f"""
        {expression1} {logic_operand1} ({expression1} {logic_operand2} ({expression1} {logic_operand3} {expression1}))
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand1)
        expected_tree.left = Node(logic_operand2)
        expected_tree.right = Node(expression1)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(logic_operand3)
        expected_tree.left.left.left = Node(expression1)
        expected_tree.left.left.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_prioritized_chained_end_with_function(self):
        expression = "sin(1) AND (cos(1) OR (sin(1) AND cos(1)))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("AND")
        expected_tree.left = Node("OR")
        expected_tree.right = Node("sin(1)")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("AND")
        expected_tree.left.left.left = Node("sin(1)")
        expected_tree.left.left.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(quaternary_numeric_expressions)
    def test_quaternary_numeric_expression_with_two_prioritized(self, expression1, logic_operand1,
                                                                logic_operand2, logic_operand3):
        expression = f"""
        ({expression1} {logic_operand1} {expression1}) {logic_operand2} ({expression1} {logic_operand3} {expression1})
        """.strip()
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand2)
        expected_tree.left = Node(logic_operand1)
        expected_tree.right = Node(logic_operand3)
        expected_tree.left.right = Node(expression1)
        expected_tree.left.left = Node(expression1)
        expected_tree.right.left = Node(expression1)
        expected_tree.right.right = Node(expression1)

        self.assertEqual(expected_tree, solver_tree)

    def test_quaternary_numeric_expression_with_two_prioritized_with_function(self):
        expression = "(sin(1) AND cos(1)) OR (sin(1) AND cos(1))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node("OR")
        expected_tree.left = Node("AND")
        expected_tree.right = Node("AND")
        expected_tree.left.right = Node("cos(1)")
        expected_tree.left.left = Node("sin(1)")
        expected_tree.right.left = Node("sin(1)")
        expected_tree.right.right = Node("cos(1)")

        self.assertEqual(expected_tree, solver_tree)

    @parameterized.expand(binary_conjunction_numeric_expressions + binary_disjunction_numeric_expressions)
    def test_binary_numeric_expression_with_stacked_outer_parenthesis(
            self, expression1, logic_operand, expression2, result):
        expression = f"(((({expression1} {logic_operand} {expression2}))))"
        solver_tree = BooleanExpressionSolver(expression, self.properties).tree

        expected_tree = Node(logic_operand)
        expected_tree.left = Node(expression1)
        expected_tree.right = Node(expression2)

        self.assertEqual(expected_tree, solver_tree)


if __name__ == '__main__':
    unittest.main()
