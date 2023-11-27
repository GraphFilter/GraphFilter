from PyQt5.QtWidgets import QFileDialog

from source.view.utils.constants import DOCUMENTS_LOCATION
from source.view.utils.constants.file_types import FileTypes


class FileDialog(QFileDialog):

    def __init__(self, file_types: FileTypes = FileTypes()):
        super().__init__()
        self.file_types = file_types

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setNameFilters(self.file_types.type_list)

    def get_open_file_name(self) -> str:
        return self.getOpenFileName(
            caption=self.file_types.name, filter=self.file_types.type_in_full, directory=DOCUMENTS_LOCATION)[0]

    def get_open_file_names(self) -> str:
        return self.getOpenFileNames(
            caption=self.file_types.name, filter=self.file_types.type_in_full, directory=DOCUMENTS_LOCATION)[0]

    def get_save_file_name(self) -> str:
        return self.getSaveFileName(
            caption=self.file_types.name, filter=self.file_types.type_in_full, directory=DOCUMENTS_LOCATION)[0]

    def get_existing_directory(self) -> str:
        return self.getExistingDirectory(
            caption=self.file_types.name, directory=DOCUMENTS_LOCATION)
