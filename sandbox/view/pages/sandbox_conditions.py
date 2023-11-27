from PyQt5.QtWidgets import QRadioButton
from sandbox import Sandbox


class SandboxConditions(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxConditions()
    sandbox.instantiate_element()
    sandbox.start()
