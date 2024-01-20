from source.commons.objects.translation_object import TranslationObject


class Operator(TranslationObject):
    _instance = None
    _allow_multiple = False

    def __new__(cls):
        if cls is Operator:
            return super().__new__(cls)
        if cls._allow_multiple or cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, code: str = "", name: str = ""):
        super().__init__(self.__class__.__name__ if name == "" else name, code)

    @classmethod
    def allow_multiple(cls):
        cls._allow_multiple = True

    def get_leaf_subclasses(self, cls=None):
        if cls is None:
            cls = self.__class__

        subclasses = cls.__subclasses__()
        leaf_subclasses = [sub() for sub in subclasses if not sub.__subclasses__()]

        for sub in subclasses:
            leaf_subclasses.extend(self.get_leaf_subclasses(sub))

        return leaf_subclasses
