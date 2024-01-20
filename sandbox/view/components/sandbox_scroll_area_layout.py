from PyQt5.QtWidgets import QVBoxLayout

from sandbox import Sandbox
from source.commons.objects.translation_object import TranslationObject
from source.view.elements.chip import Chip


class SandboxScrollAreaLayout(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxScrollAreaLayout()
    sandbox.instantiate_element()

    layout = QVBoxLayout()
    for i in range(10):
        layout.addWidget(Chip(TranslationObject(f"Planar{i}", i)))

    sandbox.element.add_element(layout)

    sandbox.start()
