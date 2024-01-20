from abc import ABC, abstractmethod
from source.commons.objects.translation_object import TranslationObject


class Calculator(TranslationObject, ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str = None, code: str = None):
        name = self.__class__.__name__ if name is None else name
        super().__init__(name, code)

    @abstractmethod
    def calculate(self, graph):
        pass
