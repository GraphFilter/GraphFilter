from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLayout, QWidgetItem, QSizePolicy
from PyQt5 import QtCore

from source.view.elements.buttons import GenericButton


class ResponsiveLayout(QLayout):
    def __init__(self, buttons: list[GenericButton]):
        super().__init__()

        self.buttons = buttons
        self.items = []

        self.add_buttons()

    def addItem(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

    def itemAt(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.create_layout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.create_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        return QtCore.QSize(max(button.width() for button in self.buttons) + (self.getContentsMargins()[0] * 2), 100)

    def add_buttons(self):
        for button in self.buttons:
            self.addItem(QWidgetItem(button))

    def create_layout(self, rect, test_only):
        left, top, right, bottom = self.getContentsMargins()
        effective_rect = rect.adjusted(left, top, -right, -bottom)

        x, y, line_height = effective_rect.x(), effective_rect.y(), 0

        for item in self.items:
            widget = item.widget()
            space_x = self.spacing() + widget.style().layoutSpacing(
                QSizePolicy.DefaultType, QSizePolicy.DefaultType, Qt.Horizontal)
            space_y = self.spacing() + widget.style().layoutSpacing(
                QSizePolicy.DefaultType, QSizePolicy.DefaultType, Qt.Vertical)
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > effective_rect.right() and line_height > 0:
                x = effective_rect.x()
                y += line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0
            if not test_only:
                item.setGeometry(QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y() + bottom
