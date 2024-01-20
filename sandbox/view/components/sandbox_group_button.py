from sandbox import Sandbox
from source.domain.entities import GRAPH_OPERATIONS
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.button_collection import ButtonCollection
from source.view.utils.icons import Icons


class SandboxGroupButton(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__

    @staticmethod
    def handler():
        print(KeyButton().sender().translation_object)


if __name__ == '__main__':
    sandbox = SandboxGroupButton()
    sandbox.instantiate_element(
        ButtonCollection().factory(
            GRAPH_OPERATIONS,
            KeyButton,
            icon=Icons.FILE_DOWNLOAD,
            font_size=12)
    ).connect(sandbox.handler)
    sandbox.start()
