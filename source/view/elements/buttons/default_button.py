from source.domain.objects.nameable_object import NameableObject
from source.domain.objects.translation_object import TranslationObject
from source.view.elements.buttons import GenericButton
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.constants.icons import Icons


class DefaultButton(GenericButton):

    def __init__(self, nameable_object: NameableObject = None, icon: Icons = None, font_size: int = BUTTON_FONT_SIZE):
        super().__init__(TranslationObject(name=nameable_object.name, code=""), icon, font_size)
        self.nameable_object = nameable_object

        self.set_content_attributes()
