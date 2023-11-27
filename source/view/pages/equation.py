from PyQt5.QtWidgets import *

from source.domain.expression_solver import ExpressionSolver
from source.view.components.group_button import GroupButton
from source.view.components.verifiable_input import MathVerifiableInput
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.pages import MAPPED_ENTITIES


class Equation(QWizardPage):

    def __init__(self):
        super().__init__()

        self.equation = MathVerifiableInput(placeholder="Write your equation...")
        self.math_tab = QTabWidget(self)

        self.set_content_attributes()
        self.set_up_layout()
        self.connect_events()

    def set_content_attributes(self):
        self.setTitle("Equation")

        for title, entity in MAPPED_ENTITIES.items():
            button_group = GroupButton(ListButton.factory(entity, KeyButton))
            button_group.connect(self.add_button_input_to_equation_text)
            self.math_tab.addTab(button_group, title)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.equation)
        layout.addStretch(1)
        layout.addWidget(self.math_tab)
        layout.addStretch(1)
        self.setLayout(layout)

    def connect_events(self):
        self.equation.input.textChanged.connect(self.on_equation_input_changed)

    def add_button_input_to_equation_text(self):
        button_clicked = KeyButton().sender().translation_object
        self.equation.add_custom_text(button_clicked.code)

    def on_equation_input_changed(self, equation, difference):
        cursor_position = self.equation.input.cursorPosition()
        if difference in [" ", ""]:
            return
        try:
            expression_solver = ExpressionSolver(equation)
            expression = expression_solver.build()
            # self.equation.input.setText(expression)
            self.equation.input.setCursorPosition(self.get_new_cursor_position(cursor_position, equation))
            expression_solver.verify()
            self.equation.set_success_label()
        except ValueError as e:
            self.equation.set_warning_label(e.args[0].args[0])
        except AttributeError as e:
            self.equation.set_error_label(e.args[0])

    def get_new_cursor_position(self, cursor_position, previous_equation):
        return cursor_position + (len(self.equation.input.text()[cursor_position:]) -
                                  len(previous_equation[cursor_position:]))
