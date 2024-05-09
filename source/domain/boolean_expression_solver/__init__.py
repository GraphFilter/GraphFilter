from source.domain.boolean_expression_solver.operands.expressions import LogicExpression
from source.domain.boolean_expression_solver.operands.connectives import Connectives, Operand, LOGICAL_CONNECTIVES, \
    LOGICAL_CONNECTIVES_VALUES
from source.domain.boolean_expression_solver.utils import *
from source.domain.entities import Function, Operator, DOMAINS, Unicode


class Properties:
    def __init__(self,
                 functions: list[Function] = Function.get_subclasses(),
                 operators: list[Operator] = Operator().get_leaf_subclasses(),
                 unicodes: list[Unicode] = Unicode.get_subclasses(),
                 names: dict = DOMAINS):
        self.functions = self.Function(functions, unicodes)
        self.operators = self.Operator(operators)
        self.names = names

    class Function:
        def __init__(self, functions, unicodes):
            self.functions = functions
            self.unicodes = unicodes

        def to_dictionary(self):
            return {function.code: function.name for function in self.functions}

        def to_calculate_dictionary(self):
            return {function.name: function.calculate for function in self.functions}

        def decode(self, expression):
            for code, name in self.to_dictionary().items():
                code = code.replace("()", "")
                pattern = re.compile(r'(?<!\w){}(?=\s|\(|$)'.format(re.escape(code.replace("()", ""))),
                                     re.IGNORECASE | re.UNICODE)
                expression = pattern.sub(name, expression)

            return Properties.Unicode(self.unicodes).decode(expression)

    class Operator:
        def __init__(self, operators):
            self.operators = operators

        def to_dictionary(self):
            return {operator.unicode if hasattr(operator, 'unicode') else operator.name: operator.code for
                    operator
                    in self.operators}

        def decode(self, expression: str) -> str:
            dictionary = self.to_dictionary()

            for name, code in dictionary.items():
                if name.lower() != code.replace("()", ""):
                    name_pattern = re.compile(r'\b{}\b|\b{}\b|{}'.format(re.escape(name), re.escape(name.replace(" ", "")),
                                                                 re.escape(name)), re.IGNORECASE)
                    expression = name_pattern.sub(code, expression)

                code_pattern = re.compile(r'(?<!\w)' + re.escape(code.replace("()", "")) + r'(?=\()', re.IGNORECASE)
                expression = code_pattern.sub(code.replace("()", ""), expression)

            return self.decode_unicode(expression)

        def decode_unicode(self, expression: str) -> str:
            pattern = re.compile('|'.join(re.escape(key) for key in self.to_dictionary().keys()))
            expression = pattern.sub(lambda match: self.to_dictionary().get(match.group(0), match.group(0)),
                                     expression)

            return expression

    class Unicode:
        def __init__(self, unicodes):
            self.unicodes = unicodes

        def to_dictionary(self):
            return {unicode.code: unicode.unicode for unicode in self.unicodes}

        def to_replace_dictionary(self):
            return {unicode.unicode: unicode.code for unicode in self.unicodes}

        def decode(self, expression: str) -> str:
            pattern = re.compile('|'.join(re.escape(key) for key, _ in self.to_dictionary().items()))
            expression = pattern.sub(lambda match: next((value for key, value in self.to_dictionary().items() if
                                                         key == match.group(0)), match.group(0)), expression)

            return expression


class BooleanExpressionSolver:
    def __init__(self, expression: str, properties: Properties):
        self.properties = properties
        self.connectives = LOGICAL_CONNECTIVES_VALUES
        self.expression = expression

        if expression:
            self.tree = self._create_tree(self.expression)

    def _create_tree(self, expression) -> Operand:
        cleaned_expression, _ = remove_outer_parenthesis(expression)
        prioritized_terms = self.get_terms_with_operators_enclosed_in_parenthesis(cleaned_expression)

        masked_expression = create_mask(expression, prioritized_terms)
        index, operator = self.find_first_operator(masked_expression)

        if index >= 0:
            left, right = self.prioritize_branches(expression[:index], expression[index + len(operator):])

            root = getattr(Connectives, operator)()
            root.left, root.right = self._create_tree(left), self._create_tree(right)

            return root
        else:
            return LogicExpression(cleaned_expression, self.properties)

    def get_terms_with_operators_enclosed_in_parenthesis(self, expression):
        matched_groups = []
        pattern = re.compile(r'(\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))')
        matches = pattern.finditer(expression)
        for match in matches:
            group = match.group(1)
            if any(operator in group for operator in self.connectives):
                matched_groups.append(group)
        return matched_groups

    def verify(self) -> None:
        try:
            self.tree.inspect()
            self.validate_boolean_expression()
            self.assert_parenthesis_matching()
            self.check_existent_required_terms()
        except ValueError as e:
            raise ValueError(e)
        except SyntaxError as e:
            raise AttributeError(e.args[0])
        except Exception as e:
            print(e.args[0])
            raise AttributeError(e.args[0])

    def validate_boolean_expression(self):
        if not self.tree.inspect() and self.expression.strip():
            raise ValueError("It's not a boolean expression")

    def assert_parenthesis_matching(self):
        expression_without_parenthesis, parenthesis = remove_outer_parenthesis(self.expression)
        if ")" in parenthesis:
            raise AttributeError("unmatched ')'")
        elif "(" in parenthesis:
            raise AttributeError("'(' was never closed")

    def check_existent_required_terms(self):
        for term in self.properties.names.keys():
            if term in self.expression or not self.expression.strip():
                return
        raise ValueError(f"{self.expression} doesn't contain required terms")

    def find_first_operator(self, expression: str) -> (int, str):
        index = -1
        op = ""

        for operator in self.connectives:
            new_index = expression.find(operator)
            if (index <= 0) or ((index > new_index) and (new_index > 0)):
                index, op = (new_index, operator)
            else:
                index, op = (index, op)

        return index, op.strip()

    def calculate_priority(self, substring: str) -> int:
        priority = sum(substring.count(operator) for operator in self.connectives)
        priority += substring.count('(')
        return priority

    def prioritize_branches(self, left: str, right: str) -> (str, str):
        left_priority, right_priority = self.calculate_priority(left), self.calculate_priority(right)

        if right_priority > left_priority:
            return right, left
        return left, right

    def solver(self):
        if self.expression:
            return self._create_tree(self.expression).solve()
        return True
