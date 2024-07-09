import logging

from PyQt6.QtCore import QSize, pyqtSignal, Qt
from PyQt6.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem
from PyQt6 import QtCore

from source.view.utils.icons import Icons


class FileList(QListWidget):
    itemCountChanged = pyqtSignal(int)
    itemSelected = pyqtSignal(int)
    itemList = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.itemSelectionChanged.connect(self.emit_selection_list)
        self.set_content_attributes()

    def set_content_attributes(self):
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setIconSize(QSize(20, 20))
        self.setAlternatingRowColors(True)

    def add_item(self, name: str):
        if not self.findItems(name, Qt.MatchFlag.MatchExactly):
            item = QListWidgetItem(name, self)
            color = self.palette().color(self.palette().WindowText).name()

            item.setIcon(Icons.FILE(color))

            icon_size = QtCore.QSize(self.get_font_size(), self.get_font_size())
            self.setIconSize(icon_size)

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

    def get_font_size(self):
        return self.fontInfo().pixelSize()
