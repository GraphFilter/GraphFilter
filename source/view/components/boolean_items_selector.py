from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from source.domain.objects.nameable_object import NameableObject
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.elements.toggle_radio_button import ToggleRadioButton


class BooleanItemsSelector(QGroupBox):

    def __init__(self, title: str, items: list[NameableObject]):
        """
        This component groups a list of items that can be checked as True or False.

        :param title: Title of the GroupBox. It appears around the group.
        :param items: The list of items contained in the group.
        """
        super().__init__()

        self.title = title
        self.items = items
        self.handler = None

        self.grid = QGridLayout()
        self.scroll_area = ScrollAreaLayout()

        self.set_content_attributes()
        self.set_up_layout()
        self.add_items()

    def set_content_attributes(self):
        """
        :rtype: object

        """
        self.setTitle(self.title)
        self.setMinimumWidth(250)

        self.grid.setHorizontalSpacing(20)

    def set_up_layout(self):
        layout = QVBoxLayout()
        header = Header()
        header.setContentsMargins(0, 0, 30, 0)
        layout.addWidget(header)
        self.scroll_area.add_element(self.grid)
        self.scroll_area.scroll_area.widget().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addLayout(self.scroll_area)
        self.setLayout(layout)

    def add_items(self):
        for i, item in enumerate(self.items):
            self.grid.addWidget(BooleanGroupItem(item), i, 0)

    def connect(self, handler):
        self.handler = handler if handler is not None else self.handler
        for row in range(len(self.items)):
            column: BooleanGroupItem = self.grid.itemAt(row).widget()
            for item in column.children():
                if isinstance(item, ToggleRadioButton):
                    item.clicked.connect(self.handler)


class Header(QGroupBox):

    def __init__(self):
        super().__init__()
        grid_layout_aux = QGridLayout()
        grid_layout_aux.setColumnStretch(0, 1)
        grid_layout_aux.setRowStretch(0, 0)
        grid_layout_aux.addWidget(QLabel(), 0, 0, Qt.AlignLeft)
        grid_layout_aux.addWidget(QLabel("TRUE"), 0, 1, Qt.AlignCenter)
        grid_layout_aux.addWidget(QLabel("FALSE"), 0, 2, Qt.AlignCenter)
        grid_layout_aux.setColumnMinimumWidth(1, 50)
        grid_layout_aux.setColumnMinimumWidth(2, 50)
        self.setLayout(grid_layout_aux)


class BooleanGroupItem(QGroupBox):
    def __init__(self, item: NameableObject):
        super().__init__()

        self.setFlat(True)
        self.item = item
        self.radio_true = ToggleRadioButton(item)
        self.radio_false = ToggleRadioButton(item)

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.radio_true.setObjectName("true")
        self.radio_false.setObjectName("false")

    def set_up_layout(self):
        grid_layout_aux = QGridLayout()
        grid_layout_aux.setColumnStretch(0, 1)
        grid_layout_aux.setRowStretch(0, 0)
        grid_layout_aux.addWidget(QLabel(self.item.name), 0, 0, Qt.AlignLeft)

        grid_layout_aux.addWidget(self.radio_true, 0, 1, Qt.AlignCenter)
        grid_layout_aux.addWidget(self.radio_false, 0, 2, Qt.AlignCenter)
        grid_layout_aux.setColumnMinimumWidth(1, 50)
        grid_layout_aux.setColumnMinimumWidth(2, 50)

        self.setLayout(grid_layout_aux)
