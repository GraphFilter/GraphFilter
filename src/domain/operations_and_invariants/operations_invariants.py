from src.domain.operations_and_invariants.bool_invariants import InvariantBool
from src.domain.operations_and_invariants.num_invariants import InvariantNum
from src.domain.operations_and_invariants.operations import MathOperations
from src.domain.operations_and_invariants.operations import GraphOperations


class Invariants:
    numerics: InvariantNum
    booleans: InvariantBool

    def __init__(self):
        self.numerics = InvariantNum()
        self.booleans = InvariantBool()


class Operations:
    graphs: GraphOperations
    math: MathOperations

    def __init__(self):
        self.graphs = GraphOperations()
        self.math = MathOperations()
