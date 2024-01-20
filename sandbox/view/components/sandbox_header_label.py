from sandbox import Sandbox
from source.commons.objects.translation_object import TranslationObject
from source.view.elements.chip import Chip


class SandboxHeaderLabel(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxHeaderLabel()
    sandbox.instantiate_element("Conditions", Chip(TranslationObject("Planar", "1234")))
    sandbox.start()
