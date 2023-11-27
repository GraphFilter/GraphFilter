from source.domain.entities.invariants.boolean_spectral_invariants import BooleanSpectralInvariants
from source.domain.entities.invariants.boolean_structural_invariants import BooleanStructuralInvariants
from source.domain.entities.invariants.dictionary_invariants import DictionaryInvariants
from source.domain.entities.invariants.matrix_invariants import MatrixInvariants
from source.domain.entities.invariants.numeric_spectral_invariants import NumericSpectralInvariants
from source.domain.entities.invariants.numeric_structural_invariants import NumericStructuralInvariants
from source.domain.entities.operations.graph_operations import GraphOperations
from source.domain.entities.operations.math_operations import MathOperations
from source.domain.entities.symbols import Unicode, Symbol
from source.domain.entities.symbols.math_symbols import MathSymbols
from source.domain.objects.function_object import FunctionObject


def get_inner_classes(cls):
    return [attr for attr in cls.__dict__.values() if isinstance(attr, type)]


FUNCTIONS = [subclass() for subclass in FunctionObject.__subclasses__()]
BOOLEAN_SPECTRAL_INVARIANTS = [cls() for cls in get_inner_classes(BooleanSpectralInvariants)]
BOOLEAN_STRUCTURAL_INVARIANTS = [cls() for cls in get_inner_classes(BooleanStructuralInvariants)]
DICTIONARY_INVARIANTS = [cls() for cls in get_inner_classes(DictionaryInvariants)]
MATRIX_INVARIANTS = [cls() for cls in get_inner_classes(MatrixInvariants)]
NUMERIC_SPECTRAL_INVARIANTS = [cls() for cls in get_inner_classes(NumericSpectralInvariants)]
NUMERIC_STRUCTURAL_INVARIANTS = [cls() for cls in get_inner_classes(NumericStructuralInvariants)]
GRAPH_OPERATIONS = [cls() for cls in get_inner_classes(GraphOperations)]
MATH_OPERATIONS = [cls() for cls in get_inner_classes(MathOperations)]
MATH_SYMBOLS = [cls() for cls in get_inner_classes(MathSymbols)]
UNICODE_SYMBOLS = [subclass() for subclass in Unicode.__subclasses__()]
SYMBOLS = MATH_SYMBOLS + UNICODE_SYMBOLS
