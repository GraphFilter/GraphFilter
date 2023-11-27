from sandbox import Sandbox
from source.domain.objects.translation_object import TranslationObject
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.constants.colors import Colors


class SandboxChip(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxChip()
    sandbox.instantiate_element(TranslationObject("a", "b"), None, BUTTON_FONT_SIZE, Colors.LIGHT_GRAY)
    sandbox.start()
