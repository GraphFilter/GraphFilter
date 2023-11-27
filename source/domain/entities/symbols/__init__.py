from abc import ABC

from source.domain.objects.translation_object import TranslationObject


class Symbol(TranslationObject, ABC):
    def __init__(self, name: str = None, code: str = None):
        super().__init__(name, code)
        self._code = code


class Unicode(Symbol):
    def __init__(self, name: str = None, code: str = None):
        super().__init__(name, code)
