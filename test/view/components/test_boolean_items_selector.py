import sys
import unittest

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QRadioButton

from source.domain.entities import BOOLEAN_STRUCTURAL_INVARIANTS, BooleanStructuralInvariants
from source.view.components.boolean_items_selector import BooleanItemsSelector, BooleanGroupItem


class TestBooleanItemsSelector(unittest.TestCase):
    emitted_signal = None

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.items = BOOLEAN_STRUCTURAL_INVARIANTS
        self.boolean_items_selector = BooleanItemsSelector("Test Title", self.items)

    def test_radio_buttons(self):
        item_widgets = self.boolean_items_selector.grid.itemAt(0).widget().children()

        item_widget = item_widgets[0]

        true_radio = item_widget.itemAt(1).widget()
        false_radio = item_widget.itemAt(2).widget()

        QTest.mouseClick(true_radio, Qt.LeftButton)
        self.assertTrue(true_radio.isChecked())
        self.assertFalse(false_radio.isChecked())

        QTest.mouseClick(false_radio, Qt.LeftButton)
        self.assertTrue(false_radio.isChecked())
        self.assertFalse(true_radio.isChecked())

    def test_radio_buttons_double_click(self):
        item_widgets = self.boolean_items_selector.grid.itemAt(0).widget().children()

        item_widget = item_widgets[0]

        true_radio = item_widget.itemAt(1).widget()
        false_radio = item_widget.itemAt(2).widget()

        QTest.mouseClick(true_radio, Qt.LeftButton)
        QTest.mouseClick(true_radio, Qt.LeftButton)
        self.assertFalse(true_radio.isChecked())

        QTest.mouseClick(false_radio, Qt.LeftButton)
        QTest.mouseClick(false_radio, Qt.LeftButton)
        self.assertFalse(false_radio.isChecked())

    def test_radio_button_signal(self):
        item_widgets = self.boolean_items_selector.grid.itemAt(0).widget().children()

        item_widget = item_widgets[0]

        true_radio = item_widget.itemAt(1).widget()

        self.boolean_items_selector.connect(self.handler)

        QTest.mouseClick(true_radio, Qt.LeftButton)

        self.assertEqual(self.emitted_signal, true_radio)

    def handler(self):
        self.emitted_signal = QRadioButton().sender()

    def tearDown(self):
        del self.boolean_items_selector
        del self.app


class TestBooleanGroupItem(unittest.TestCase):
    emit_custom_signal = pyqtSignal(object)

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.boolean_group_item = BooleanGroupItem(BooleanStructuralInvariants.Planar())
        self.emitted_object = None

    def test_signal_emission(self):
        true_radio: QRadioButton = self.boolean_group_item.layout().itemAt(1).widget()

        true_radio.clicked.connect(
            lambda: setattr(self, 'emitted_object', QRadioButton().sender())
        )

        true_radio.click()

        self.assertEqual(self.emitted_object.parentWidget().item, BooleanStructuralInvariants.Planar())

    def tearDown(self):
        del self.boolean_group_item
        del self.app


if __name__ == '__main__':
    unittest.main()
