from PyQt5.QtWidgets import QWizardPage, QVBoxLayout

from source.domain.objects.translation_object import TranslationObject
from source.view.components.file_selector import FileSelector
from source.view.components.group_button import GroupButton
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.constants.file_types import GraphTypes
from source.view.utils.constants.icons import Icons


class Files(QWizardPage):
    def __init__(self):
        super().__init__()

        self.file_selector = FileSelector(GraphTypes(), GroupButton(
            ListButton().factory(
                [TranslationObject(name="By Brandon", code="1"), TranslationObject(name="House of Graphs", code="2")],
                KeyButton, Icons.FILE_DOWNLOAD), "Download Graphs"), )

        self.set_up_layout()
        self.connect()

    def set_up_layout(self):
        self.setTitle("Files")

        layout = QVBoxLayout()
        layout.addWidget(self.file_selector)
        self.setLayout(layout)

    def connect(self):
        self.file_selector.file_list.itemCountChanged.connect(lambda: self.completeChanged.emit())

    def isComplete(self):
        return True if self.file_selector.file_list.count() > 0 else False
