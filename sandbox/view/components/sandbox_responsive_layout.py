from sandbox import Sandbox
from source.domain.entities.invariants.boolean_structural_invariants import BOOLEAN_STRUCTURAL_INVARIANTS
from source.view.elements.buttons import ListButton
from source.view.elements.chip import Chip
from source.view.utils.constants.colors import Colors
from source.view.utils.constants.icons import Icons


class SandboxResponsiveLayout(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxResponsiveLayout()
    sandbox.instantiate_element(ListButton().factory(BOOLEAN_STRUCTURAL_INVARIANTS, Chip, icon=Icons.FILE_DOWNLOAD,
                                                     background_color=Colors.DARK_RED))
    sandbox.start()
