from PyQt6 import QtCore
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QPushButton, QWidget

from source.commons.objects.translation_object import TranslationObject
from source.view.utils.colors import Colors
from source.view.utils.constants import BUTTON_FONT_SIZE
from source.view.utils.icons import Icons


class GenericButton(QPushButton):

    def __init__(self,
                 translation_object: TranslationObject = None,
                 icon: Icons = None,
                 font_size: int = BUTTON_FONT_SIZE,
                 background_color: str = None
                 ):
        super().__init__()
        self.translation_object = translation_object
        self.icon = icon
        self.font_size = font_size
        self.background_color = background_color

    def set_content_attributes(self):
        style = ""
        if self.font_size:
            font = QFont()
            font.setPixelSize(self.font_size)
            self.setFont(font)
            self.setMinimumHeight(self.font_size * 4)

        if self.translation_object:
            if self.icon:
                self.setIcon(self.icon(self.get_text_color()))
                self.setIconSize(QtCore.QSize(self.get_font_size(), self.get_font_size()))
                style = f"""
                    text-align: left; 
                    padding-left: 10px;
                """

            self.setStyleSheet(f"""
                    text-align: center; 
                    {"background-color:" + self.background_color + ";" if self.background_color is not None else ""}
                    color: {self.get_text_color()};                
                    """ + style)
            self.setText(self.translation_object.name)

    def get_text_color(self):
        background_color_rgb = QColor(self.background_color) \
            if self.background_color is not None else self.palette().button().color()
        red, green, blue = background_color_rgb.red(), background_color_rgb.green(), background_color_rgb.blue()
        luminance = 0.299 * red + 0.587 * green + 0.114 * blue

        threshold = 186
        text_color = "black" if luminance > threshold else "white"
        if text_color == "black" and luminance > 30:
            text_color = Colors.DARK_TEXT
        elif text_color == "white" and luminance < 220:
            text_color = Colors.LIGHT_TEXT

        return text_color

    def get_width(self, widget_object: QWidget):
        return self.get_minimum_size() + widget_object.contentsMargins().bottom() * 4

    def calculate_combined_width(self, widget: QWidget):
        return self.get_minimum_size() + widget.contentsMargins().bottom() * 4

    def get_font_size(self):
        return self.fontInfo().pixelSize()

    def get_minimum_size(self):
        icon_addition = 4 if self.icon is not None else 0
        return (self.fontMetrics()
                .horizontalAdvance(self.translation_object.name) + (self.iconSize().width() * icon_addition)
                )

    def rescale_font(self, widget_object: QWidget):
        font_size = int(
            (widget_object.width() - widget_object.contentsMargins().left()) / len(self.translation_object.name))

        return font_size
