from abc import abstractmethod

from source.commons.objects.translation_object import TranslationObject


class FunctionObject(TranslationObject):
    def init(self, name: str = None, code: str = None):
        super().__init__(name, code)

    @property
    def code(self):
        return self._code + "()"

    @code.setter
    def code(self, new_code):
        self._code = new_code

    @abstractmethod
    def calculate(self, graph):
        pass
