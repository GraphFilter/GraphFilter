from source.domain.entities.calculators import Calculator
from source.domain.entities.functions import Function
from source.domain.entities.functions.graph_operations import GraphOperations
from source.domain.entities.functions.math_operations import MathOperations
from source.domain.entities.graphs import DOMAINS
from source.domain.entities.invariants import Invariant
from source.domain.entities.invariants.boolean_spectral_invariants import BooleanSpectralInvariants
from source.domain.entities.invariants.boolean_structural_invariants import BooleanStructuralInvariants
from source.domain.entities.invariants.dictionary_invariants import DictionaryInvariants
from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants.numeric_spectral_invariants import NumericSpectralInvariants
from source.domain.entities.invariants.numeric_structural_invariants import NumericStructuralInvariants
from source.domain.entities.operators import Operator
from source.domain.entities.symbols import Unicode, Symbol
from source.domain.entities.symbols.math_symbols import MathSymbols


def get_inner_classes(cls):
    return [attr() for attr in cls.__dict__.values() if isinstance(attr, type)]


def get_subclasses(cls):
    return [subclass for subclass in cls.__subclasses__()]


GRAPH_OPERATIONS = get_inner_classes(GraphOperations)
MATH_OPERATIONS = get_inner_classes(MathOperations)
NUMERIC_STRUCTURAL_INVARIANTS = get_inner_classes(NumericStructuralInvariants)
NUMERIC_SPECTRAL_INVARIANTS = get_inner_classes(NumericSpectralInvariants)
BOOLEAN_STRUCTURAL_INVARIANTS = get_inner_classes(BooleanStructuralInvariants)
BOOLEAN_SPECTRAL_INVARIANTS = get_inner_classes(BooleanSpectralInvariants)
MATRIX_INVARIANTS = get_inner_classes(MatrixInvariants)
DICTIONARY_INVARIANTS = get_inner_classes(DictionaryInvariants)
MATH_SYMBOLS = get_inner_classes(MathSymbols)

SYMBOLS = get_subclasses(Symbol)
UNICODES = get_subclasses(Unicode)
INVARIANTS = get_subclasses(Invariant)
FUNCTIONS = get_subclasses(Function)
CALCULATORS = FUNCTIONS + INVARIANTS
OPERATORS = FUNCTIONS + SYMBOLS
