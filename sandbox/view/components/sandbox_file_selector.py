from sandbox import Sandbox
from source.domain.objects.translation_object import TranslationObject
from source.view.components.group_button import GroupButton
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.constants.file_types import GraphTypes
from source.view.utils.constants.icons import Icons


class SandboxFileSelector(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFileSelector()
    sandbox.instantiate_element(GraphTypes(), GroupButton(
        ListButton().factory(
            [TranslationObject(name="By Brandon", code="1"), TranslationObject(name="House of Graphs", code="2")],
            KeyButton, Icons.FILE_DOWNLOAD), "Download Graphs"))
    sandbox.start()
