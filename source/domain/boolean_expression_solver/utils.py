import re


def create_mask(expression: str, groups: list[str]) -> str:
    mask = expression

    for group in groups:
        mask = mask.replace(group, '`' * len(group))

    return mask


def parenthesis_match(expression):
    stack = []

    for char in re.findall(r'[()]', expression):
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def remove_outer_recursive(expression, hanging_parenthesis=""):
    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        inner_expression = expression[1:-1].strip()
        if parenthesis_match(inner_expression):
            return remove_outer_recursive(inner_expression, hanging_parenthesis)

    if expression.startswith('(') and len(expression) > 1:
        if not parenthesis_match(expression):
            inner_expression = expression[1:].strip()
            return remove_outer_recursive(inner_expression, hanging_parenthesis + "(")

    if expression.endswith(')'):
        if not parenthesis_match(expression):
            inner_expression = expression[:-1].strip()
            return remove_outer_recursive(inner_expression, hanging_parenthesis + ")")

    return expression, hanging_parenthesis


def remove_outer_parenthesis(s):
    return remove_outer_recursive(s)
