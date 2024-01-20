import unittest

from source.domain.boolean_expression_solver import remove_outer_parenthesis


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_remove_simple_outer_parenthesis(self):
        expression = "( a + b == 0 )"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "a + b == 0"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_stack_outer_parenthesis(self):
        expression = "(( a + b == 0 ))"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "a + b == 0"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_only_first_outer_parenthesis(self):
        expression = "((a + b == 1 AND a + b == 1) OR (a + b == 1 AND a + b = 1))"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "(a + b == 1 AND a + b == 1) OR (a + b == 1 AND a + b = 1)"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_only_first_outer_parenthesis_with_functions(self):
        expression = "((sin(1) AND sin(1)) OR cos(1))"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "(sin(1) AND sin(1)) OR cos(1)"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_invalid_parenthesis_start(self):
        expression = "(sin(1)"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "sin(1)"
        expected_hanging_parenthesis = "("

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_invalid_parenthesis_end(self):
        expression = "cos(1))"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "cos(1)"
        expected_hanging_parenthesis = ")"

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_do_not_remove_parenthesis(self):
        expression = "(a + b == 1 AND a + b == 1) OR (a + b == 1 AND a + b = 1)"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "(a + b == 1 AND a + b == 1) OR (a + b == 1 AND a + b = 1)"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_do_not_remove_parenthesis_with_function(self):
        expression = "(sin(1) AND sin(1)) OR cos(1)"
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "(sin(1) AND sin(1)) OR cos(1)"
        expected_hanging_parenthesis = ""

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_double_parenthesis_start(self):
        expression = "((sin(1) + cos(1) <= 1 "
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "sin(1) + cos(1) <= 1"
        expected_hanging_parenthesis = "(("

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)

    def test_remove_double_parenthesis_end(self):
        expression = " sin(1) + cos(1) <= 1)) "
        result, hanging_parenthesis = remove_outer_parenthesis(expression)

        expected_expression = "sin(1) + cos(1) <= 1"
        expected_hanging_parenthesis = "))"

        self.assertEqual(expected_expression, result)
        self.assertEqual(expected_hanging_parenthesis, hanging_parenthesis)


if __name__ == '__main__':
    unittest.main()
