from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QWIDGETSIZE_MAX

from source.domain.objects.nameable_object import NameableObject
from source.view.components.group_button import GroupButton
from source.view.elements.buttons import GenericButton
from source.view.elements.buttons.default_button import DefaultButton
from source.view.elements.file_dialog import FileDialog
from source.view.elements.file_list import FileList
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.utils.constants.file_types import FileTypes


class FileSelector(QWidget):
    def __init__(self, file_type: FileTypes, group_button: GroupButton = None):
        super().__init__()
        self.file_list = FileList()

        self.selected_files = []

        self.add_file_button = AddFileButton(NameableObject("Add files"))
        self.remove_file_button = RemoveFilesButton(NameableObject("Remove files"))
        self.remove_all_files_button = RemoveAllFilesButton(NameableObject("Remove all"))

        self.group_button = group_button
        self.scroll_area = ScrollAreaLayout()

        self.file_dialog = FileDialog(file_type)

        self.set_content_attributes()
        self.set_up_layout()
        self.connect_buttons()
        self.connect_file_list()

    def set_content_attributes(self):
        self.scroll_area.add_element(self.file_list)
        self.file_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    def scroll_value_changed(self):
        is_visible = self.group_button.scroll_area.scroll_area.verticalScrollBar().isVisible()

        # self.group_button.resizeEvent(None)
        self.group_button.setMinimumHeight(120)
        if not is_visible:
            self.group_button.setMaximumHeight(self.group_button.height())
        else:
            self.group_button.setMaximumHeight(QWIDGETSIZE_MAX)

    def set_up_layout(self):
        layout = QHBoxLayout()

        layout.addLayout(self.scroll_area, stretch=1)

        buttons = QVBoxLayout()

        buttons.addWidget(self.add_file_button)
        buttons.addWidget(self.remove_file_button)
        buttons.addWidget(self.remove_all_files_button)
        buttons.addSpacing(10)
        buttons.addStretch(1)

        if self.group_button:
            buttons.addWidget(self.group_button, stretch=1)
            self.group_button.scroll_area.scroll_area.resizeEvent = lambda event: self.scroll_value_changed()

        layout.addLayout(buttons)

        self.setLayout(layout)

    def connect_buttons(self):
        self.add_file_button.clicked.connect(self.add_file)
        self.remove_file_button.clicked.connect(self.remove_file)
        self.remove_all_files_button.clicked.connect(self.remove_all_files)
        self.file_list.itemCountChanged.connect(self.remove_all_files_button.set_visibility)
        self.file_list.itemSelected.connect(self.remove_file_button.set_visibility)
        self.file_list.itemList.connect(self.set_selected_files)
        self.group_button.connect(self.handler)

    def connect_file_list(self):
        self.file_list.itemClicked.connect(lambda: self.remove_file_button.setEnabled(True))

    def add_file(self):
        file_name = self.file_dialog.get_open_file_names()
        self.file_list.add_items(file_name)

    def remove_file(self):
        self.file_list.remove_selected_items()

    def remove_all_files(self):
        self.file_list.clear_items()

    def set_selected_files(self, files: list[str]):
        self.selected_files = files

    @staticmethod
    def handler():
        print(GenericButton().sender())


class AddFileButton(DefaultButton):
    def __init__(self, nameable_object: NameableObject):
        super().__init__(nameable_object)


class RemoveFilesButton(DefaultButton):
    def __init__(self, nameable_object: NameableObject):
        super().__init__(nameable_object)
        self.setEnabled(False)

    def set_visibility(self, selected_files: int):
        self.setEnabled(selected_files > 0)


class RemoveAllFilesButton(DefaultButton):
    def __init__(self, nameable_object: NameableObject):
        super().__init__(nameable_object)
        self.setEnabled(False)

    def set_visibility(self, count_files: int):
        self.setEnabled(count_files > 0)
