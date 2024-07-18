from sandbox import Sandbox
from source.domain import Parameters
from source.domain.entities import BooleanStructuralInvariants
from source.domain.filter import Filter


class SandboxFilteringReportWindow(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__
        self.windowed = False


if __name__ == '__main__':
    sandbox = SandboxFilteringReportWindow()
    sandbox.instantiate_element(Parameters("Name mock",
                                           Filter(),
                                           "n(G) > 0",
                                           {BooleanStructuralInvariants.Planar(): True,
                                            BooleanStructuralInvariants.Biconnected(): False},
                                           "Description mock",
                                           ["path_files/graph.g6"],
                                           "path/path_mock"),
                                20
                                )
    sandbox.set_initial_size()
    sandbox.start()
