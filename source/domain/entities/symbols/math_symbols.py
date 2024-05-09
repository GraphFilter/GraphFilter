from source.domain.entities.symbols import Symbol, Unicode


class MathSymbols:
    class Plus(Symbol):

        def __init__(self):
            super().__init__("+")

    class Subtraction(Symbol):

        def __init__(self):
            super().__init__("-")

    class Division(Symbol):

        def __init__(self):
            super().__init__("/")

    class Product(Symbol):

        def __init__(self):
            super().__init__("*")

    class Power(Symbol):

        def __init__(self):
            super().__init__("**")

    class Modulus(Symbol):

        def __init__(self):
            super().__init__("%")

    class Equal(Symbol):

        def __init__(self):
            super().__init__("==")

    class LessThan(Symbol):

        def __init__(self):
            super().__init__("<")

    class GreaterThan(Symbol):

        def __init__(self):
            super().__init__(">")

    class PiNumber(Symbol):

        def __init__(self):
            super().__init__("\u03c0")

    class LessThanEqual(Unicode):

        def __init__(self):
            super().__init__("\u2264", "<=")

    class GreaterThanEqual(Unicode):

        def __init__(self):
            super().__init__("\u2265", ">=")

    class Different(Unicode):

        def __init__(self):
            super().__init__("\u2260", "!=")
