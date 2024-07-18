import logging
import numpy

from simpleeval import FunctionNotDefined, NameNotDefined, SimpleEval

from source.worker.boolean_expression_solver.operands import Operand


class LogicExpression(SimpleEval, Operand):
    def __init__(self, expression: str, properties):
        super().__init__()
        self.properties = properties
        self.functions = properties.functions.to_calculate_dictionary()
        self.names = properties.names

        super(SimpleEval, self).__init__(expression)

    def calculate(self) -> bool:
        return self.eval(self.properties.functions.decode(self.value))

    def validate(self) -> bool:
        if not self.value:
            return
        try:
            result = self.eval(self.properties.functions.decode(self.value))
            evaluation_type = type(result)

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
