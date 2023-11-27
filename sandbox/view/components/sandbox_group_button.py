from sandbox import Sandbox
from source.domain.entities import GRAPH_OPERATIONS
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.constants.icons import Icons


class SandboxGroupButton(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__

    @staticmethod
    def handler():
        print(KeyButton().sender().translation_object)


if __name__ == '__main__':
    sandbox = SandboxGroupButton()
    sandbox.instantiate_element(ListButton().factory(GRAPH_OPERATIONS, KeyButton, icon=Icons.FILE_DOWNLOAD,
                                                     font_size=12)).connect(sandbox.handler)
    sandbox.start()
