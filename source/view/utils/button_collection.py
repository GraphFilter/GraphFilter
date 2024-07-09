from typing import Type

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget

from source.commons.objects.translation_object import TranslationObject
from source.view.elements.buttons import GenericButton
from source.view.utils.colors import Colors
from source.view.utils.constants import BUTTON_FONT_SIZE


class ButtonCollection:
    def __init__(self, buttons: list[GenericButton] = None):
        self.buttons = buttons

    def get_max_button_width(self, widget_object: QWidget):
        return max(self.buttons, key=lambda button: button.calculate_combined_width(widget_object))

    @staticmethod
    def factory(objects: list[TranslationObject],
                button_type: Type[GenericButton],
                icon: QIcon = None,
                font_size: int = BUTTON_FONT_SIZE,
                background_color: str = Colors.LIGHT_GRAY
                ):
        button_list = []
        for item in objects:
            generic_button = GenericButton(item, icon, font_size, background_color=background_color)
            target_params = button_type.__init__.__code__.co_varnames[1:]
            generic_params = {param: getattr(generic_button, param) for param in target_params}
            button_list.append(button_type(**generic_params))

        return button_list
