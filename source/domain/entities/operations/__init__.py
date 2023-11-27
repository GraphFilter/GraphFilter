from abc import ABC, abstractmethod

from source.domain.objects.translation_object import TranslationObject


class Operation(TranslationObject, ABC):
    def __init__(self, name: str = None, code: str = None):
        super().__init__(name, code)

    @abstractmethod
    def calculate(self, graph):
        pass
    