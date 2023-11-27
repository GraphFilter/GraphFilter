import sys
import unittest
from unittest.mock import patch

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from source.domain.objects.translation_object import TranslationObject
from source.view.components.file_selector import FileSelector
from source.view.components.group_button import GroupButton
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.elements.file_dialog import FileDialog
from source.view.utils.constants.file_types import GraphTypes
from source.view.utils.constants.icons import Icons


class TestFileSelector(unittest.TestCase):
    emitted_signal = None

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.selector = FileSelector(GraphTypes(), GroupButton(ListButton.factory([TranslationObject(name="a", code="1"),
                                                                     TranslationObject(name="b", code="2")],
                                                                    KeyButton, Icons.FILE_DOWNLOAD), "Download Graphs"))
        self.emitted_object = None
        self.emitted_files = None

    def test_add_files(self):
        self.assertFalse(self.selector.remove_all_files_button.isEnabled())

        with patch.object(FileDialog, 'get_open_file_names', return_value=['mocked_file.txt']):
            QTest.mouseClick(self.selector.add_file_button, Qt.LeftButton)

            self.assertEqual(self.selector.file_list.item(0).text(), 'mocked_file.txt')
            self.assertEqual(self.selector.file_list.count(), 1)
            self.assertTrue(self.selector.remove_all_files_button.isEnabled())

    def test_remove_files(self):
        self.assertFalse(self.selector.remove_all_files_button.isEnabled())
        self.selector.file_list.add_items(['file1.txt', 'file2.txt', 'file3.txt'])

        self.assertFalse(self.selector.remove_file_button.isEnabled())
        self.assertTrue(self.selector.remove_all_files_button.isEnabled())

        item_widget = self.selector.file_list.item(0)
        QTest.mouseClick(self.selector.file_list.viewport(), Qt.LeftButton,
                         pos=self.selector.file_list.visualItemRect(item_widget).center())

        self.assertTrue(self.selector.remove_file_button.isEnabled())

        QTest.mouseClick(self.selector.remove_file_button, Qt.LeftButton)

        self.assertEqual(self.selector.file_list.count(), 2)
        self.assertNotIn('file1.txt', [self.selector.file_list.item(i).text()
                                       for i in range(self.selector.file_list.count())])

    def test_remove_all_files(self):
        self.assertFalse(self.selector.remove_all_files_button.isEnabled())
        self.selector.file_list.add_items(['file1.txt', 'file2.txt', 'file3.txt'])
        self.assertTrue(self.selector.remove_all_files_button.isEnabled())

        QTest.mouseClick(self.selector.remove_all_files_button, Qt.LeftButton)

        self.assertEqual(self.selector.file_list.count(), 0)
        self.assertFalse(self.selector.remove_all_files_button.isEnabled())

    def slot_to_receive_signal(self, files):
        self.emitted_files = files

    def test_emit_signal_all_files(self):
        self.selector.file_list.itemList.connect(self.slot_to_receive_signal)
        with patch.object(FileDialog, 'get_open_file_names', return_value=['file1.txt', 'file2.txt']):
            QTest.mouseClick(self.selector.add_file_button, Qt.LeftButton)

        self.assertEqual(self.emitted_files, ['file1.txt', 'file2.txt'])

    def tearDown(self):
        del self.selector
        del self.app


if __name__ == '__main__':
    unittest.main()
