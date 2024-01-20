from sandbox import Sandbox


class SandboxFiles(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFiles()
    sandbox.instantiate_element()
    sandbox.start()
