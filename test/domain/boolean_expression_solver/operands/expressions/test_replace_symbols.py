import unittest
from itertools import product

from parameterized import parameterized

from source.domain.boolean_expression_solver import Properties
from source.domain.entities import Operator, Function

input_string = "num"
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


class Number(Function):
    def __init__(self):
        super().__init__("n")

    def calculate(self, graph):
        return graph


class Clique(Function):
    def __init__(self):
        super().__init__("c")

    def calculate(self, graph):
        return graph


class Num(Function):
    def __init__(self):
        super().__init__("n")

    def calculate(self, graph):
        return graph


class Cli(Function):
    def __init__(self):
        super().__init__("c")

    def calculate(self, graph):
        return graph


class TestReplaceSymbols(unittest.TestCase):
    def setUp(self) -> None:
        self.properties = Properties(operators=[Number(), Num(), Clique(), Cli()])

    def test_valid_expression(self):
        expected_expression = "n()c()"
        self.assertEqual(expected_expression, self.properties.operators.decode("n()c()"))

    def test_uppercase_single_replacement(self):
        expected_expression = "n()"
        self.assertEqual(expected_expression, self.properties.operators.decode("NUMBER"))

    def test_lowercase_single_replacement(self):
        expected_expression = "n()"
        self.assertEqual(expected_expression, self.properties.operators.decode("number"))

    @parameterized.expand(scrambled_case_expressions)
    def test_scrambled_case_replacement(self, expression):
        expected_expression = "n()"
        self.assertEqual(expected_expression, self.properties.operators.decode(expression))

    @parameterized.expand(whitespace_expressions)
    def test_whitespace_replacement(self, expression):
        expected_expression = expression
        self.assertEqual(expected_expression, self.properties.operators.decode(expression))

    def test_uppercase_double_replacement(self):
        expected_expression = "n() c()"
        self.assertEqual(expected_expression, self.properties.operators.decode("NUM CLI"))

    def test_lowercase_double_replacement(self):
        expected_expression = "n()c()"
        self.assertEqual(expected_expression, self.properties.operators.decode("numberclique"))

    @parameterized.expand(scrambled_double_case_expressions)
    def test_scrambled_case_double_replacement(self, expression):
        expected_expression = "n()c()"
        self.assertEqual(expected_expression, self.properties.operators.decode(expression))


if __name__ == '__main__':
    unittest.main()
