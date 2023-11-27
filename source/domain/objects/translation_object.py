from source.domain.objects.nameable_object import NameableObject


class TranslationObject(NameableObject):
    def __init__(self, name: str = None, code: str = None):
        super().__init__(name=name)
        self.code = code
