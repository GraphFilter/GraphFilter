from sandbox import Sandbox
from source.domain.entities import BOOLEAN_STRUCTURAL_INVARIANTS
from source.view.elements.chip import Chip
from source.view.utils.button_collection import ButtonCollection
from source.view.utils.colors import Colors
from source.view.utils.icons import Icons


class SandboxResponsiveLayout(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxResponsiveLayout()
    sandbox.instantiate_element(
        ButtonCollection().factory(
            BOOLEAN_STRUCTURAL_INVARIANTS,
            Chip,
            icon=Icons.FILE_DOWNLOAD,
            background_color=Colors.DARK_RED)
    )
    sandbox.start()
