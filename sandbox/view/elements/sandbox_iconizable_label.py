from sandbox import Sandbox
from source.domain.objects.translation_object import TranslationObject
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.constants.colors import Colors
from source.view.utils.constants.icons import Icons


class SandboxIconizableLabel(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxIconizableLabel()
    sandbox.instantiate_element().set_content_attributes(Icons.SUCCESS, "This is a success label")
    sandbox.start()
