from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtGui import QDesktopServices, QKeyEvent
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy

from source.commons.objects.translation_object import TranslationObject
from source.view.components.group_button import GroupButton
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.elements.buttons import GenericButton
from source.view.elements.buttons.default_button import DefaultButton
from source.view.elements.file_dialog import FileDialog
from source.view.elements.file_list import FileList
from source.view.utils.file_types import FileTypes


class FileSelectionManager(QWidget):
    listChanged = pyqtSignal()

    def __init__(self, file_type: FileTypes, custom_button_group: GroupButton = None):
        """
        This widget provides a user interface for selecting and managing files. It includes a list of selected files,
        buttons for adding, removing, and clearing files, as well as an optional custom button group. The files can be
        selected using a file dialog based on the specified file type.

        :param file_type: The type of files to be selected, as specified by the FileTypes enum.
        :type file_type: FileTypes
        :param custom_button_group: An optional custom button group for additional file management actions.
                                    Defaults to None.
        :type custom_button_group: GroupButton, optional
        """

        super().__init__()
        self.file_list = FileList()

        self.add_file_button = self.AddFileButton()
        self.remove_file_button = self.RemoveFilesButton()
        self.remove_all_files_button = self.RemoveAllFilesButton()

        self.custom_button_group = custom_button_group
        self.scroll_area = ScrollAreaLayout()

        self.file_dialog = FileDialog(file_type)

        self._set_content_attributes()
        self._set_up_layout()
        self._connect_buttons()
        self._connect_file_list()

    def _set_content_attributes(self):
        self.scroll_area.add_element(self.file_list)
        self.custom_button_group.setMinimumWidth(self.custom_button_group.biggest_button_width)
        self.file_list.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

    def _set_up_layout(self):
        layout = QHBoxLayout()

        layout.addLayout(self.scroll_area, 1)

        buttons = QVBoxLayout()

        top_buttons = QVBoxLayout()
        top_buttons.addWidget(self.add_file_button, alignment=Qt.AlignmentFlag.AlignTop)
        top_buttons.addWidget(self.remove_file_button, alignment=Qt.AlignmentFlag.AlignTop)
        top_buttons.addWidget(self.remove_all_files_button, alignment=Qt.AlignmentFlag.AlignTop)

        buttons.addLayout(top_buttons)
        top_buttons.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons.addSpacing(30)

        if self.custom_button_group:
            buttons.addWidget(self.custom_button_group)
            self.custom_button_group.setMinimumWidth(
                self.custom_button_group.biggest_button_width +
                self.custom_button_group.contentsMargins().left() +
                self.custom_button_group.contentsMargins().right() +
                self.custom_button_group.grid.contentsMargins().left() +
                self.custom_button_group.grid.contentsMargins().right()
            )

            self.custom_button_group.setMaximumHeight(self.custom_button_group.biggest_button_minimum_height * 2)

        layout.addLayout(buttons)

        self.setLayout(layout)

    def _connect_buttons(self):
        self.add_file_button.clicked.connect(self.add_file)
        self.remove_file_button.clicked.connect(self.remove_file)
        self.remove_all_files_button.clicked.connect(self.remove_all_files)
        self.file_list.itemCountChanged.connect(self.remove_all_files_button.set_visibility)
        self.file_list.itemSelected.connect(self.remove_file_button.set_visibility)
        self.file_list.itemList.connect(self.set_selected_files)
        self.custom_button_group.connect(self._handler)

    def _connect_file_list(self):
        self.file_list.itemClicked.connect(lambda: self.remove_file_button.setEnabled(True))

    @staticmethod
    def _handler():
        QDesktopServices.openUrl(QUrl(GenericButton().sender().translation_object.code))

    def add_file(self):
        file_name = self.file_dialog.get_open_file_names()
        self.file_list.add_items(file_name)

    def remove_file(self):
        self.file_list.remove_selected_items()

    def remove_all_files(self):
        self.file_list.clear_items()

    def set_selected_files(self, files: list[str]):
        self.setProperty("files", files)
        self.listChanged.emit()

    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        print(event.key())
        if event.key() == Qt.Key.Key_Delete:
            self.remove_file()
        return super().keyPressEvent(event)

    class AddFileButton(DefaultButton):
        def __init__(self):
            super().__init__(TranslationObject("Add Files"))

    class RemoveFilesButton(DefaultButton):
        def __init__(self):
            super().__init__(TranslationObject("Remove Files"))
            self.setEnabled(False)

        def set_visibility(self, selected_files: int):
            self.setEnabled(selected_files > 0)

    class RemoveAllFilesButton(DefaultButton):
        def __init__(self):
            super().__init__(TranslationObject("Remove All"))
            self.setEnabled(False)

        def set_visibility(self, count_files: int):
            self.setEnabled(count_files > 0)
