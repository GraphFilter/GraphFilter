from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLayout, QWidgetItem
from PyQt5 import QtCore, QtWidgets


class ResponsiveLayout(QLayout):
    def __init__(self, widgets: list):
        super().__init__()

        self.items = []
        self.widgets = widgets
        self.height = 0

        self.add_widgets(widgets)

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
        return self.height

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.create_layout(rect)

    def sizeHint(self):
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()

        new_width = int(screen_geometry.width() * 0.5)
        new_height = int(screen_geometry.height() * 0.5)

        return QtCore.QSize(new_width, new_height)

    def minimumSize(self):
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()

        new_width = int(screen_geometry.width() * 0.1)
        # new_height = int(screen_geometry.height() * 0.1)

        if self.items:
            new_width = max(self.items, key=lambda x: x.widget().width(), default=None).widget().width() + 12

        return QtCore.QSize(new_width, 0)

    def maximumSize(self):
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        return QtCore.QSize(screen_geometry.width(), screen_geometry.height())

    def add_widgets(self, widgets: list):
        for widget in widgets:
            self.addItem(QWidgetItem(widget))

    def create_layout(self, rect):
        spacing = 6
        actual_position_x, actual_position_y, line_height = spacing, 26, spacing

        for item in self.items:
            next_position_x = actual_position_x + item.sizeHint().width() + spacing
            if next_position_x - spacing > rect.right() and line_height > 0:
                actual_position_x = spacing
                actual_position_y += line_height + spacing
                next_position_x = actual_position_x + item.sizeHint().width() + spacing
                line_height = spacing
            item.setGeometry(QRect(QtCore.QPoint(actual_position_x, actual_position_y), item.sizeHint()))
            actual_position_x = next_position_x
            line_height = max(line_height, item.sizeHint().height())

        self.height = actual_position_y + (line_height - spacing)
