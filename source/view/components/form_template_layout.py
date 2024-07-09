from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFormLayout, QSizePolicy

from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.items import pair_widgets
from source.view.items.pair_widgets import PairWidgets


class FormTemplateLayout(ScrollAreaLayout):
    def __init__(self, pairs: list[PairWidgets]):
        """
        This widget extends the ScrollAreaLayout and is designed to create a form layout with paired widgets.
        Each pair typically consists of a label and an associated input widget. The pairs are specified using a
        list of PairWidgets.

        :param pairs: A list of PairWidgets, where each PairWidgets object represents a label-input widget pair.
        :type pairs: list[pair_widgets]
        """
        super().__init__()
        self.pairs = pairs
        self.form = QFormLayout()

        self._configure_scroll()
        self._add_items()
        self.add_element(self.form)

    def _configure_scroll(self):
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def _add_items(self):
        for pair in self.pairs:
            if hasattr(pair, 'key'):
                self.form.addRow(pair.key, pair.value)

                pair.key.setContentsMargins(0, 0, 27, 0)
                pair.key.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                pair.value.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                self.form.setAlignment(pair.key, Qt.AlignmentFlag.AlignVCenter)
            else:
                self.form.addRow(pair)

        self.form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.form.setVerticalSpacing(15)
        self.form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
