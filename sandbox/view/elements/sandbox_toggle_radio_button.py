from sandbox import Sandbox
from source.commons.objects.nameable_object import NameableObject


class SandboxToggleRadioButton(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxToggleRadioButton()
    sandbox.instantiate_element(NameableObject("item"))
    sandbox.start()
