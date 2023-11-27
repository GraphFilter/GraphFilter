from sandbox import Sandbox


class SandboxVerifiableInput(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxVerifiableInput()
    sandbox.instantiate_element("placeholder")
    sandbox.start()
