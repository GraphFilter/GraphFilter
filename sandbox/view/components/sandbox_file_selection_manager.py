from sandbox import Sandbox
from source.commons.objects.translation_object import TranslationObject
from source.view.components.group_button import GroupButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.button_collection import ButtonCollection
from source.view.utils.file_types import GraphTypes
from source.view.utils.icons import Icons


class SandboxFileSelectionManager(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFileSelectionManager()
    sandbox.instantiate_element(GraphTypes(), GroupButton(
        ButtonCollection().factory(
            [TranslationObject(name="By Brandon", code="https://houseofgraphs.org/meta-directory"),
             TranslationObject(name="House of Graphs", code="http://users.cecs.anu.edu.au/~bdm/data/graphs.html")],
            KeyButton, Icons.FILE_DOWNLOAD), "Download Graphs"))
    sandbox.start()
