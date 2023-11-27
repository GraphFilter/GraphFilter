import unittest
from itertools import product

from parameterized import parameterized

from source.domain.expression_solver import LogicExpression

input_string = "number"
whitespace_expressions = []

for combination in product(*[(' ' + c, c) for c in input_string]):
    result = ''.join(combination).strip()
    if ' ' in result[1:-1]:
        whitespace_expressions.append(result)


input_string = "Number"
scrambled_case_expressions = []

for combination in product(*[(c.lower(), c.upper()) for c in input_string]):
    result = ''.join(combination)
    scrambled_case_expressions.append(result)

input_string = "numcli"
scrambled_double_case_expressions = []

for combination in product(*[(c.lower(), c.upper()) for c in input_string]):
    result = ''.join(combination)
    scrambled_double_case_expressions.append(result)


class TestReplaceSymbols(unittest.TestCase):
    def test_valid_expression(self):
        expected_expression = "n()c()"
        symbols = {"num": "n()", "cli": "c()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression("n()c()", symbols))

    def test_uppercase_single_replacement(self):
        expected_expression = "n()"
        symbols = {"number": "n()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression("NUMBER", symbols))

    def test_lowercase_single_replacement(self):
        expected_expression = "n()"
        symbols = {"number": "n()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression("number", symbols))

    @parameterized.expand(scrambled_case_expressions)
    def test_scrambled_case_replacement(self, expression):
        expected_expression = "n()"
        symbols = {"number": "n()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression(expression, symbols))

    @parameterized.expand(whitespace_expressions)
    def test_whitespace_replacement(self, expression):
        expected_expression = expression
        symbols = {"number": "n()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression(expression,  symbols))

    def test_uppercase_double_replacement(self):
        expected_expression = "n() c()"
        symbols = {"number": "n()", "clique": "c()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression("NUMBER CLIQUE", symbols))

    def test_lowercase_double_replacement(self):
        expected_expression = "n()c()"
        symbols = {"number": "n()", "clique": "c()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression("numberclique", symbols))

    @parameterized.expand(scrambled_double_case_expressions)
    def test_scrambled_case_double_replacement(self, expression):
        expected_expression = "n()c()"
        symbols = {"num": "n()", "cli": "c()"}
        self.assertEqual(expected_expression, LogicExpression.replace_symbols_on_expression(expression, symbols))


if __name__ == '__main__':
    unittest.main()
