from PyQt5.QtCore import Qt

from source.domain.objects.translation_object import TranslationObject
from source.view.elements.buttons import GenericButton
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.constants.icons import Icons


class HelpButton(GenericButton):

    def __init__(self, translation_object: TranslationObject = None,
                 icon: Icons = None, font_size: int = BUTTON_FONT_SIZE):
        super().__init__(translation_object, icon, font_size)

        self.setToolTip(translation_object.name)
        self.setStyleSheet("background: transparent")
        self.setCursor(Qt.WhatsThisCursor)
        self.set_content_attributes()
