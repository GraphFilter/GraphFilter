from sandbox import Sandbox


class SandboxReview(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxReview()
    sandbox.instantiate_element()
    sandbox.start()
