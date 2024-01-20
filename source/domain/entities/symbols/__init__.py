from source.domain.entities.operators import Operator


class Symbol(Operator):
    def __init__(self, code: str = None):
        super().__init__(code)


class Unicode(Symbol):
    def __init__(self, code: str = None, unicode: str = None):
        super().__init__(code)
        self.unicode = unicode

    @staticmethod
    def get_subclasses():
        return [unicode() for unicode in Unicode.__subclasses__()]
