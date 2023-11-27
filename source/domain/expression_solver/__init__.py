from source.domain.entities import FUNCTIONS, SYMBOLS
from source.domain.entities.graphs import DEFAULT_NAMES
from source.domain.expression_solver.operands.operators import LOGICAL_OPERATORS

from source.domain.expression_solver.operands.expressions import LogicExpression

from source.domain.expression_solver.utils import *
from source.domain.expression_solver.operands.operators import *


class ExpressionSolver:
    def __init__(self, expression, functions=FUNCTIONS, names=DEFAULT_NAMES, symbols=SYMBOLS + FUNCTIONS):
        self.names = names
        self.functions = functions
        self.symbols = symbols
        self.operators = LOGICAL_OPERATORS
        self.expression = expression
        self.tree = self._create_tree(self.expression)

    def _create_tree(self, expression) -> Operand:
        expression_without_parenthesis, parenthesis = remove_outer_parenthesis(expression)
        prioritized_terms = self.get_terms_with_operators_enclosed_in_parenthesis(expression_without_parenthesis)

        masked_expression = create_mask(expression, prioritized_terms)
        index, operator = self.find_first_operator(masked_expression)

        if index > 0:
            left, right, inverted = self.prioritize_branches(expression[:index], expression[index + len(operator):])

            root = globals()[operator](inverted)
            root.left, root.right = self._create_tree(left), self._create_tree(right)

            return root
        else:
            return LogicExpression(expression_without_parenthesis, self.functions, self.names, self.symbols).\
                set_parenthesis(parenthesis)

    def get_terms_with_operators_enclosed_in_parenthesis(self, expression):
        matched_groups = []
        pattern = re.compile(r'(\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))')
        matches = pattern.finditer(expression)
        for match in matches:
            group = match.group(1)
            if any(operator in group for operator in self.operators):
                matched_groups.append(group)
        return matched_groups

    def build(self) -> str:
        return self.tree.serialize()

    def verify(self) -> None:
        try:
            self.tree.inspect()
            expression_without_parenthesis, parenthesis = remove_outer_parenthesis(self.expression)
            if ")" in parenthesis:
                raise AttributeError("unmatched ')'")
            elif "(" in parenthesis:
                raise AttributeError("'(' was never closed")
        except ValueError as e:
            raise ValueError(e)
        except SyntaxError as e:
            raise AttributeError(e.args[0])
        except Exception as e:
            print(e.args[0])
            raise AttributeError(e.args[0])

    def find_first_operator(self, expression: str) -> (int, str):
        index = -1
        op = ""

        for operator in self.operators:
            new_index = expression.find(operator)
            if (index <= 0) or ((index > new_index) and (new_index > 0)):
                index, op = (new_index, operator)
            else:
                index, op = (index, op)

        return index, op.strip()

    def calculate_priority(self, substring: str) -> int:
        priority = sum(substring.count(operator) for operator in self.operators)
        priority += substring.count('(')
        return priority

    def prioritize_branches(self, left: str, right: str) -> (str, str, bool):
        left_priority, right_priority = self.calculate_priority(left), self.calculate_priority(right)

        if right_priority > left_priority:
            return right, left, True
        return left, right, False

    def execute(self, expression: str):
        return self._create_tree(expression).solve()
