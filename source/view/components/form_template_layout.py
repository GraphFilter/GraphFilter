from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QSizePolicy

from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.utils import PairWidgets


class FormTemplateLayout(ScrollAreaLayout):
    def __init__(self, pairs: list[PairWidgets]):
        super().__init__()
        self.pairs = pairs
        self.form = QFormLayout()

        self.configure_scroll()
        self.add_items()
        self.add_element(self.form)

    def configure_scroll(self):
        # self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def add_items(self):
        for pair in self.pairs:
            self.form.addRow(pair.key, pair.value)

            pair.key.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            pair.value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        # self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.form.setVerticalSpacing(30)
        self.form.setLabelAlignment(Qt.AlignLeft)
