from PyQt6 import QtGui

from source.commons.objects.translation_object import TranslationObject
from source.view.elements.buttons import GenericButton
from source.view.utils.constants import BUTTON_FONT_SIZE


class KeyButton(GenericButton):
    def __init__(self, translation_object: TranslationObject = None, icon: str = None,
                 font_size: int = BUTTON_FONT_SIZE):
        super().__init__(translation_object, icon, font_size)

        if translation_object:
            self.setToolTip(translation_object.code)

            self.setFont(QtGui.QFont("Cambria Math", self.font_size))
            self.set_content_attributes()
