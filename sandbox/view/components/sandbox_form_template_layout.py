from PyQt6.QtWidgets import QLabel
from sandbox import Sandbox
from source.view.items.pair_widgets import PairWidgets


class SandboxFormTemplateLayout(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxFormTemplateLayout()
    sandbox.instantiate_element([
        PairWidgets(QLabel("A"), QLabel("A")),
        PairWidgets(QLabel("A"), QLabel("A")),
        PairWidgets(QLabel("A"), QLabel("A"))
    ])
    sandbox.start()
