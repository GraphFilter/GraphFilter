from sandbox import Sandbox


class SandboxFileList(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFileList()
    sandbox.instantiate_element()
    for i in range(10):
        sandbox.element.add_item(f"file{i}.txt")
    sandbox.start()
