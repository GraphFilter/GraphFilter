from sandbox import Sandbox
from source.commons.objects.translation_object import TranslationObject


class SandboxKeyButton(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxKeyButton()
    sandbox.instantiate_element(TranslationObject("KeyButton", "Key"))
    sandbox.start()
