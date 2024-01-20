from sandbox import Sandbox


class SandboxCaptionContainer(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxCaptionContainer()
    sandbox.instantiate_element("Project Name", "some random description")
    sandbox.start()
