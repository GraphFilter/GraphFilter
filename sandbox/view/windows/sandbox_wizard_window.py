from sandbox import Sandbox


class SandboxWizardWindow(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__
        self.windowed = False


if __name__ == '__main__':
    sandbox = SandboxWizardWindow()
    sandbox.instantiate_element()
    sandbox.set_initial_size()
    sandbox.start()
