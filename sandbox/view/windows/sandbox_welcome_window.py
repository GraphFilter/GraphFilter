from sandbox import Sandbox


class SandboxWelcomeWindow(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__
        self.windowed = False


if __name__ == '__main__':
    sandbox = SandboxWelcomeWindow()
    sandbox.instantiate_element()
    sandbox.start()
