from PyQt5.QtWidgets import QSizePolicy

from source.commons.objects.translation_object import TranslationObject
from source.view.elements.buttons import GenericButton
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.colors import Colors
from source.view.utils.icons import Icons


class Chip(GenericButton):
    def __init__(self,
                 translation_object: TranslationObject = None,
                 icon: Icons = None,
                 font_size: int = BUTTON_FONT_SIZE,
                 background_color: str = Colors.LIGHT_GRAY
                 ):
        super().__init__(translation_object, icon, font_size, background_color)

        self.set_content_attributes()
        self.set_chip_style()

    def set_chip_style(self):
        style = f"""
            border-radius: {self.font_size}px; 
            border: 1px solid {self.background_color}; 
        """
        self.setStyleSheet(self.styleSheet() + style)
        self.setFixedHeight(self.font_size * 2)
        self.setFixedWidth(self.get_minimum_size() + 24)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
