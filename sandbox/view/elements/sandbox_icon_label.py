from sandbox import Sandbox
from source.view.utils.icons import Icons


class SandboxIconLabel(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxIconLabel()
    sandbox.instantiate_element().set_content_attributes(Icons.SUCCESS, "This is a success label")
    sandbox.start()
