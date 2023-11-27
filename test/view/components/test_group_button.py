import sys
import unittest

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from source.domain.entities import NUMERIC_SPECTRAL_INVARIANTS
from source.view.components.group_button import GroupButton
from source.view.elements.buttons import ListButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.utils.constants.icons import Icons


class TestGroupButton(unittest.TestCase):
    emitted_signal = None

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.keys = NUMERIC_SPECTRAL_INVARIANTS
        self.keyboard = GroupButton(ListButton.factory(self.keys, KeyButton, icon=Icons.FILE_DOWNLOAD))
        self.emitted_object = None

    def test_key_button_signal(self):
        key_button: KeyButton = self.keyboard.grid.itemAt(0).widget()
        self.keyboard.connect(self.handler)

        QTest.mouseClick(key_button, Qt.LeftButton)

        self.assertEqual(self.emitted_signal, self.keys[0])

    def test_font_warning(self):
        with self.assertLogs(level='WARNING') as cm:
            group_button = GroupButton(
                ListButton.factory(self.keys, KeyButton, icon=Icons.FILE_DOWNLOAD, font_size=500)
            )
            group_button.resize(100, 100)
            self.assertIn(f"Font greater than supported, the value was adjusted to {group_button.keys[0].font_size}",
                          cm.output[0])

    def handler(self):
        self.emitted_signal = KeyButton().sender().translation_object

    def tearDown(self):
        del self.keyboard
        del self.app


if __name__ == '__main__':
    unittest.main()
