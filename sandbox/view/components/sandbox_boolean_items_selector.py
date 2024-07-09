from PyQt6.QtWidgets import QRadioButton

from sandbox import Sandbox
from source.domain.entities import BOOLEAN_SPECTRAL_INVARIANTS


class SandboxBooleanItemsSelector(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__

    @staticmethod
    def handler():
        print(QRadioButton().sender().parent().item)


if __name__ == '__main__':
    sandbox = SandboxBooleanItemsSelector()
    sandbox.instantiate_element("teste", BOOLEAN_SPECTRAL_INVARIANTS).connect(sandbox.handler)
    sandbox.start()
