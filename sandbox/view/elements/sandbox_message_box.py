from sandbox import Sandbox
from source.view.elements.buttons.key_button import KeyButton
from source.view.elements.message_box import MessageBoxDescription


class SandboxMessageBox(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__

    @staticmethod
    def handler():
        print(KeyButton().sender().translation_object)


if __name__ == '__main__':
    sandbox = SandboxMessageBox()
    sandbox.instantiate_element(MessageBoxDescription(title="Test message?", text="Testing message box "))
    sandbox.start()
