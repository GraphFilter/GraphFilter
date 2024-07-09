import sys
import unittest

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QRadioButton, QApplication

from source.domain.entities import BOOLEAN_STRUCTURAL_INVARIANTS, BooleanStructuralInvariants
from source.view.components.boolean_items_selector import BooleanItemsSelector


class TestBooleanItemsSelector(unittest.TestCase):
    emitted_signal = None
    app = None

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
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

    @classmethod
    def tearDownClass(cls):
        del cls.app


class TestBooleanGroupItem(unittest.TestCase):
    app = None
    emit_custom_signal = pyqtSignal(object)

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.boolean_group_item = BooleanItemsSelector.BooleanGroupItem(BooleanStructuralInvariants.Planar())
        self.emitted_object = None

    def test_signal_emission(self):
        true_radio: QRadioButton = self.boolean_group_item.layout().itemAt(1).widget()

        true_radio.clicked.connect(
            lambda: setattr(self, 'emitted_object', QRadioButton().sender())
        )

        QTest.mouseClick(true_radio, Qt.LeftButton)

        self.assertEqual(self.emitted_object.parentWidget().item, BooleanStructuralInvariants.Planar())

    def tearDown(self):
        del self.boolean_group_item

    @classmethod
    def tearDownClass(cls):
        del cls.app


if __name__ == '__main__':
    unittest.main()
