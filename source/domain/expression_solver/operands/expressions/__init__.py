import logging
import re
from typing import Dict

import numpy
from simpleeval import FunctionNotDefined, NameNotDefined, SimpleEval

from source.domain.entities import UNICODE_SYMBOLS, FUNCTIONS
from source.domain.expression_solver.operands import Operand
from source.domain.objects.function_object import FunctionObject


class LogicExpression(SimpleEval, Operand):
    def __init__(self, expression: str, functions: list[FunctionObject], names: dict, symbols: list):
        super().__init__()
        if functions:
            self.functions = self.get_functions_dict_calculate(functions)
        if names:
            self.names = names

        self.parenthesis: str = ""

        replaced_expression = self.replace_symbols_on_expression(expression, self.get_functions_dict_symbols(symbols))

        super(SimpleEval, self).__init__(replaced_expression)

    def set_parenthesis(self, parenthesis: str = ""):
        self.parenthesis = parenthesis
        return self

    def calculate(self):
        self.eval(self.value)

    def validate(self) -> bool:
        if not self.value:
            raise ValueError("Incomplete expression")
        try:
            evaluation_type = type(self.eval(self.decode(self.value)))
            return evaluation_type == numpy.bool_ or evaluation_type == bool
        except FunctionNotDefined as exception:
            logging.warning(exception.message)
            raise ValueError(f"Function '{exception.func_name}' not defined")
        except NameNotDefined as exception:
            logging.warning(exception.message)
            raise ValueError(f"Name '{exception.name}' is not defined")
        except Exception as error:
            logging.error(str(error))
            raise error

    def check_name(self, name) -> bool:
        if name in self.names:
            return True

    @staticmethod
    def get_functions_dict_calculate(functions: list[FunctionObject]) -> Dict[str, callable]:
        return {type(function).__name__: function.calculate for function in functions}

    @staticmethod
    def get_functions_dict_symbols(symbols: list) -> Dict[str, str]:
        return {symbol.name: symbol._code for symbol in symbols}

    @staticmethod
    def replace_symbols_on_expression(expression: str, symbols: Dict[str, str]) -> str:
        replaced_expression = expression
        for name, code in symbols.items():
            pattern = re.compile(r'\b{}\b|\b{}\b|{}'.format(re.escape(name), re.escape(name.replace(" ", "")),
                                                            re.escape(name)), re.IGNORECASE)
            replaced_expression = pattern.sub(code, replaced_expression)

        if replaced_expression == expression:
            logging.info("Did not replace anything in expression.")

        return replaced_expression

    @staticmethod
    def decode(expression: str) -> str:
        combined_dict = {
            **{function._code: type(function).__name__ for function in FUNCTIONS},
            **{symbol._code: symbol.name for symbol in UNICODE_SYMBOLS}
        }

        replaced_expression = expression
        for code, name in combined_dict.items():
            pattern = re.compile(r'(?<!\w){}(?=\s|\(|$)'.format(re.escape(code)), re.IGNORECASE | re.UNICODE)
            replaced_expression = pattern.sub(name, replaced_expression)

        return replaced_expression

    def serialize(self):
        left, right = "",  ""

        if '(' in self.parenthesis:
            left = self.parenthesis

        if ')' in self.parenthesis:
            right = self.parenthesis

        return f"{left}{self.value}{right}"
