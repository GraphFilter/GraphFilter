from src.store.operations_and_invariants.bool_invariants import InvariantBool
from src.store.operations_and_invariants.num_invariants import InvariantNum
from src.store.operations_and_invariants.other_invariants import InvariantOther
from src.store.operations_and_invariants.operations import *


class OperationsInvariantsStore:

    def __init__(self):
        self.numInvariant: InvariantNum = InvariantNum()
        self.boolInvariant: InvariantBool = InvariantBool()
        self.graphOperations: GraphOperations = GraphOperations()
        self.mathOperations: MathOperations = MathOperations()
        self.basicMathOperations: BasicMathOperations = BasicMathOperations()
        self.otherInvariant: InvariantOther = InvariantOther()


operations_invariants = OperationsInvariantsStore()

dic_num_invariants_names = operations_invariants.numInvariant.dic_name_inv
dic_graph_operations_names = operations_invariants.graphOperations.dic_name_inv
dic_math_operations_names = operations_invariants.mathOperations.dic_name_inv
dic_math_and_basic_operations_names = {**operations_invariants.mathOperations.dic_name_inv,
                                       **operations_invariants.basicMathOperations.dic_name_inv}
dic_other_invariants_names = operations_invariants.otherInvariant.dic_name_inv

dic_bool_invariants_names = operations_invariants.boolInvariant.dic_name_inv
dic_bool_inv_spectral_names = operations_invariants.boolInvariant.dic_name_inv_spectral
dic_bool_inv_structural_names = operations_invariants.boolInvariant.dic_name_inv_structural



# Note: Dictionary used in equation box
dict_text_equation = {**operations_invariants.numInvariant.dic_name_inv,
                      **operations_invariants.graphOperations.dic_name_inv,
                      **operations_invariants.mathOperations.dic_name_inv,
                      **operations_invariants.basicMathOperations.dic_name_inv}
dic_math_symbols = operations_invariants.basicMathOperations.dic_math_symbols

# Note: Dictionary used for translation by simpleeval
dic_function_to_eval = {**operations_invariants.numInvariant.dic_function,
                        **operations_invariants.graphOperations.dic_function,
                        **operations_invariants.mathOperations.dic_function}

# Note: Dictionary used for visualize in graph_information_dock
dic_invariants_to_visualize = {**dic_bool_invariants_names, **dic_num_invariants_names, **dic_other_invariants_names}

#Note: Dictionary used for number constants
dic_math_const = operations_invariants.basicMathOperations.dic_math_const
