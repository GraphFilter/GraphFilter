import logging
import math

from PyQt5.QtWidgets import QGridLayout, QGroupBox

from source.view.elements.buttons import GenericButton, ListButton
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.utils.constants import STRETCH_FACTOR


class GroupButton(QGroupBox):
    def __init__(self, keys: list[GenericButton], title: str = "") -> None:
        super().__init__()

        self.keys = keys
        self.handler = None
        self.title = title

        self.grid = QGridLayout()
        self.scroll_area = ScrollAreaLayout()
        self.biggest_button_width = 0
        self.biggest_button_minimum_height = 0

        self.set_up_layout()
        self.set_content_attributes()
        self.add_keys()

    def set_content_attributes(self):
        self.setTitle(self.title)
        self.set_max_button_width()
        self.scroll_area.set_minimum_width(self.biggest_button_width)
        self.setMinimumHeight(self.biggest_button_minimum_height)

    def set_up_layout(self):
        self.scroll_area.add_element(self.grid)
        self.setLayout(self.scroll_area)

    def set_max_button_width(self):
        biggest_button = ListButton(self.keys).get_max_button_width(self)
        self.biggest_button_minimum_height = biggest_button.minimumHeight() * self.layout().getContentsMargins()[0] * 3
        self.biggest_button_width = biggest_button.get_width(self) + 60
        if self.biggest_button_width > self.width():
            new_font_size = biggest_button.rescale_font(self)
            logging.warning(f"Font greater than supported, the value was adjusted to {new_font_size}")
            for button in self.keys:
                setattr(button, 'font_size', new_font_size)
                button.set_content_attributes()
            self.biggest_button_width = biggest_button.get_width(self)

    def resizeEvent(self, event):
        self.set_max_button_width()
        self.add_keys()
        self.update()
        super().resizeEvent(event)

    def add_keys(self):
        buttons_per_row = math.floor(self.width() / self.biggest_button_width)

        for i, key in enumerate(self.keys):
            row = int(i / buttons_per_row)
            column = int(i % buttons_per_row)
            self.grid.setRowStretch(i, STRETCH_FACTOR)
            self.grid.addWidget(key, row, column)

    def connect(self, handler):
        self.handler = handler if handler is not None else self.handler
        if handler is not None:
            for i in range(self.grid.count()):
                item = self.grid.itemAt(i)
                if item and item.widget() and isinstance(item.widget(), type(self.keys[i])):
                    item.widget().clicked.connect(self.handler)
