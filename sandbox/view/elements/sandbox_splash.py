from PyQt6.QtCore import QTimer
from sandbox import Sandbox


class SandboxSplash(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__
        self.windowed = False


if __name__ == '__main__':
    sandbox = SandboxSplash()
    sandbox.instantiate_element()

    timer = QTimer()
    timer.timeout.connect(sandbox.element.close)
    timer.timeout.connect(sandbox.quit)
    timer.start(1000)

    sandbox.start()


