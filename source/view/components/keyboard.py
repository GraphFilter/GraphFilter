from PyQt6.QtWidgets import QVBoxLayout, QTabWidget

from source.commons import split_camel_case
from source.commons.objects.translation_object import TranslationObject
from source.domain.boolean_expression_solver import Properties
from source.view.components.group_button import GroupButton
from source.view.components.verifiable_input import VerifiableInput
from source.view.elements.buttons.key_button import KeyButton
from source.view.elements.inputs.equation_input import EquationInput


class Keyboard(QVBoxLayout):
    def __init__(self, properties: Properties, empty_input_message: str = None):
        super().__init__()

        self.operators = properties.operators
        self.input = VerifiableInput(EquationInput(properties, empty_input_message), "insert your equation...")
        self.tab = QTabWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        tabs = {}

        for operator in self.operators.operators:
            key = split_camel_case(operator.__class__.__qualname__.split('.')[0])

            if key not in tabs:
                tabs[key] = []

            button = KeyButton(TranslationObject(split_camel_case(operator.name), operator.code))
            tabs[key].append(button)
            button.clicked.connect(self.add_button_input_to_equation_text)

        for key, value in reversed(list(tabs.items())):
            self.tab.addTab(GroupButton(value), key)

    def set_up_layout(self):
        self.addStretch(1)
        self.addWidget(self.input)
        self.addStretch(1)
        self.addWidget(self.tab)
        self.addStretch(1)

    def add_button_input_to_equation_text(self):
        button_clicked = KeyButton().sender().translation_object
        self.input.add_custom_text(button_clicked.code)
