from sandbox import Sandbox


class SandboxEquation(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxEquation()
    sandbox.instantiate_element()
    sandbox.start()
