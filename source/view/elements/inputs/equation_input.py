import typing

from PyQt6.QtGui import QValidator, QFont

from source.worker.boolean_expression_solver import BooleanExpressionSolver, Properties
from source.view.elements.inputs import Input


class EquationInput(Input):
    def __init__(self, properties: Properties = Properties(), empty_input_message: str = None):
        super().__init__()
        self.properties = properties
        self.setFont(QFont("Courier"))
        self.empty_input_message = empty_input_message

    def validator(self):
        try:
            super().validator()
            expression_solver = BooleanExpressionSolver(self.text(), self.properties)
            expression_solver.verify()
            self.validInput.emit()
            return QValidator.State.Acceptable
        except NameError as e:
            self.invalidInput.emit(self.empty_input_message, NameError)
            return QValidator.State.Acceptable
        except ValueError as e:
            self.invalidInput.emit(e.args[0].args[0], ValueError)
            return QValidator.State.Invalid
        except AttributeError as e:
            self.invalidInput.emit(e.args[0], AttributeError)
            return QValidator.State.Invalid

    def setText(self, a0: typing.Optional[str]) -> None:
        new_text = self.properties.operators.decode(a0)
        cursor_position = self.reset_cursor(new_text)
        super().setText(new_text)
        self.validator()
        self.setCursorPosition(cursor_position)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.setText(self.text())

    def reset_cursor(self, new_text: str):
        current_cursor_position = self.cursorPosition()

        if self.text() != new_text:
            if current_cursor_position <= len(new_text) and new_text[current_cursor_position - 1] == ")":
                current_cursor_position -= 1
            elif new_text[-1] == ")":
                current_cursor_position = len(new_text) - 1

        return current_cursor_position
