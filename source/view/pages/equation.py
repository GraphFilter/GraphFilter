from PyQt6.QtWidgets import *

from source.worker.boolean_expression_solver import Properties
from source.view.components.keyboard import Keyboard
from source.view.elements.message_box import MessageBoxDescription
from source.view.pages import WizardPage


class Equation(WizardPage):
    def __init__(self):
        super().__init__()

        self.keyboard = Keyboard(
            Properties(),
            empty_input_message="When the equation is empty, it is mandatory to select at least one condition"
        )

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setTitle("Equation")
        self.setSubTitle(self.subtitle)

    def set_up_layout(self):
        self.setLayout(self.keyboard)

    def set_properties(self) -> None:
        self.registerField("equation*", self.keyboard.input.input)

    def isComplete(self):
        return self.keyboard.input.input.hasAcceptableInput()

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, True)

    def showEvent(self, a0):
        self.keyboard.input.input.setFocus()

    def cleanupPage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, False)

    subtitle = """Write an mathematical equation or inequality, using the numeric invariants and operations."""

    help_message = MessageBoxDescription(title="How to write equations?",
                                         text="""
            <p>
                You can input equations and inequalities by typing, using the names or symbols for the invariants, or by
                using buttons for easy input. It is necessary to apply the functions to a Graph, as <code>f(G)</code>, or by
                using compositions <code>f(Compl(G))</code>. Expressions can be combined using logical connectors
                <code>AND</code> or <code>OR</code>, and can also be prioritized using parenthesis. <br>
                <h4>Examples:</h4>
                <ul>
                    <li><code>n(G) \u2265 0</code></li>
                    <li><code>\u03c7(\u2113(G))/2 \u2264 floor(\u03bc\u2081(G))+1-\u03c0**2</code></li>
                    <li><code>EE(G)+diam(Comp(\u2113(G)) > ln(\u03bb\u2082(G))</code></li>
                    <li><code>n(G) \u2265 15 OR \u0394(G) > 5 AND Е(G) > 10</code></li>
                    <li><code>\u0394(G) > 5 AND r(\u0198(G)) == diam(G) AND Е(G) > 10</code></li>
                </ul>

                    You can access our <a href="https://github.com/GraphFilter/GraphFilter/wiki/User-Guide#equations">
                    dictionary</a> to find out more about each invariant.
            </p>
                 """
                                         )
