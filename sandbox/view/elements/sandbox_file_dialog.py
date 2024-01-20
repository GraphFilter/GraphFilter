from sandbox import Sandbox
from source.view.utils.file_types import GraphTypes


class SandboxFileDialog(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFileDialog()
    sandbox.instantiate_element(GraphTypes())
    sandbox.start()
