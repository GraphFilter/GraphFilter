from sandbox import Sandbox
from source.worker.boolean_expression_solver import Properties
from source.view.elements.inputs.equation_input import EquationInput


class SandboxVerifiableInput(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxVerifiableInput()
    sandbox.instantiate_element(EquationInput(Properties()), "placeholder")
    sandbox.start()
