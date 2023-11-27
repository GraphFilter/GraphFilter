from typing import Dict, List

from source.domain.entities import MATH_OPERATIONS, MATH_SYMBOLS, NUMERIC_SPECTRAL_INVARIANTS, \
    NUMERIC_STRUCTURAL_INVARIANTS, GRAPH_OPERATIONS
from source.domain.expression_solver import LOGICAL_OPERATORS_NAMES

MAPPED_ENTITIES: Dict[str, List] = {
    'Math Operations': MATH_OPERATIONS + MATH_SYMBOLS + LOGICAL_OPERATORS_NAMES,
    'Numeric Spectral Invariants': NUMERIC_SPECTRAL_INVARIANTS,
    'Numeric Structural Invariants': NUMERIC_STRUCTURAL_INVARIANTS,
    'Graph Operations': GRAPH_OPERATIONS
}
