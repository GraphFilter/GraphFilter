from source.domain.entities.operators import Operator


class Function(Operator):
    def __init__(self, code: str = ""):
        super().__init__(code + "()")

    def calculate(self, graph):
        pass

    @staticmethod
    def get_subclasses():
        return [function() for function in Function.__subclasses__()]
