from source.domain.entities.symbols import Symbol, Unicode


class MathSymbols:
    class Plus(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Sum",
                code="+",
            )

    class Subtraction(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Subtraction",
                code="-",
            )

    class Division(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Division",
                code="/",
            )

    class Product(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Product",
                code="*",
            )

    class Power(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="^",
                code="**",
            )

    class Modulus(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Modulus",
                code="%",
            )

    class Equal(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Equal",
                code="==",
            )

    class LessThan(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Less than",
                code="<",
            )

    class GreaterThan(Symbol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="Greater than",
                code=">",
            )

    class LessThanEqual(Unicode):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="<=",
                code="\u2264",
            )

    class GreaterThanEqual(Unicode):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name=">=",
                code="\u2265",
            )

    class Different(Unicode):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="!=",
                code="\u2260",
            )

    class PiNumber(Unicode):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            super().__init__(
                name="\u03c0",
                code="\u03c0",
            )
