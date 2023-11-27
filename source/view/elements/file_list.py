import logging

import qtawesome
from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem

from source.view.utils.constants.icons import Icons


class FileList(QListWidget):
    itemCountChanged = pyqtSignal(int)
    itemSelected = pyqtSignal(int)
    itemList = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.itemSelectionChanged.connect(self.emit_selection_list)
        self.set_content_attributes()

    def set_content_attributes(self):
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setIconSize(QSize(20, 20))
        self.setAlternatingRowColors(True)

    def add_item(self, name: str):
        if not self.findItems(name, Qt.MatchExactly):
            item = QListWidgetItem(name, self)
            color = self.palette().color(self.palette().WindowText).name()
            icon = qtawesome.icon(Icons.FILE, color=color)
            item.setIcon(icon)
            self.emit_count_list()
        else:
            logging.warning("You cannot add the same file twice.")

    def add_items(self, names: list[str]):
        for name in names:
            self.add_item(name)

    def remove_selected_items(self):
        for item in self.selectedItems():
            self.takeItem(self.row(item))
        self.emit_count_list()

    def clear_items(self):
        self.clear()
        self.emit_count_list()

    def emit_count_list(self):
        self.itemCountChanged.emit(self.count())
        self.itemList.emit([self.item(i).text() for i in range(self.count())])

    def emit_selection_list(self):
        selected_count = len(self.selectedItems())
        self.itemSelected.emit(selected_count)
