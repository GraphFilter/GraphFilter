import os
import sys
import unittest
from PyQt5.QtGui import QKeySequence
from source.store.project_information_store import project_information_store
from source.store.project_information_store import wizard_information_store
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import *
from app import Controller
from PyQt5.QtCore import QStandardPaths as Qs


application = QApplication(sys.argv)


def key_sequence(widget, sequence):
    for text in sequence:
        QTest.keyPress(widget, text)


class TestMainWorkflow(unittest.TestCase):

    def setUp(self):
        self.window = Controller()

    def test_new_project_sequence(self):
        self.set_up_main_window()
        self.set_up_project_file_page()
        self.set_up_method_page()
        self.set_up_equations_page()
        self.set_up_conditions_page()
        self.set_up_graph_files_page()
        self.set_up_review_page()
        self.set_up_project_window()

    def set_up_main_window(self):
        QTest.mouseClick(self.window.welcome_controller.welcome_content.new_button, Qt.LeftButton)

    def set_up_project_file_page(self):
        self.assertTrue(self.window.wizard_controller.project_files_page.isVisible())
        key_sequence(self.window.wizard_controller.project_files_page.project_name_input, "My Title")
        QTest.keySequence(self.window.wizard_controller.project_files_page.project_location_input,
                          QKeySequence("Backspace").SelectAll)
        key_sequence(self.window.wizard_controller.project_files_page.project_location_input,
                     Qs.writableLocation(Qs.DocumentsLocation))
        QTest.mouseClick(self.window.wizard_controller.wizard_window.next_button, Qt.LeftButton)

    def set_up_method_page(self):
        self.assertTrue(self.window.wizard_controller.method_page.isVisible())
        QTest.mouseClick(self.window.wizard_controller.method_page.filter_button, Qt.LeftButton)
        QTest.mouseClick(self.window.wizard_controller.wizard_window.next_button, Qt.LeftButton)

    def set_up_equations_page(self):
        self.assertTrue(self.window.wizard_controller.equations_page.isVisible())
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, "n")
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, "(")
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, "G")
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, ")")
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, ">")
        QTest.keyPress(self.window.wizard_controller.equations_page.equation, "0")
        QTest.mouseClick(self.window.wizard_controller.wizard_window.next_button, Qt.LeftButton)

    def set_up_conditions_page(self):
        self.assertTrue(self.window.wizard_controller.conditions_page.isVisible())
        wizard_information_store.conditions['Planar'] = 'true'
        self.window.wizard_controller.review_page.set_conditions({'Planar': 'true'})
        self.window.wizard_controller.update_conditions_page()
        self.window.wizard_controller.conditions_page.completeChanged.emit()
        QTest.mouseClick(self.window.wizard_controller.wizard_window.next_button, Qt.LeftButton)

    def set_up_graph_files_page(self):
        self.assertTrue(self.window.wizard_controller.graph_files_page.isVisible())
        self.window.wizard_controller.graph_files_page.list_files_input.addItem(
            os.getcwd().replace("\\", "/").replace("/test_interface", "") +
            "/test/domain/resources/graphs/graphs2.g6")
        self.window.wizard_controller.update_complete_graph_files_page()
        QTest.mouseClick(self.window.wizard_controller.wizard_window.next_button, Qt.LeftButton)

    def set_up_review_page(self):
        self.assertTrue(self.window.wizard_controller.review_page.isVisible())
        self.assertEqual(self.window.wizard_controller.review_page.project_name.text(), "My Title")
        self.assertEqual(self.window.wizard_controller.review_page.project_location.text(),
                         Qs.writableLocation(Qs.DocumentsLocation))
        self.assertEqual(self.window.wizard_controller.review_page.method.text(), "Filter Graphs")
        self.assertEqual(self.window.wizard_controller.review_page.equation.text(), "n(G)>0")
        self.assertEqual(self.window.wizard_controller.review_page.conditions, {'Planar': 'true'})
        self.assertEqual(self.window.wizard_controller.review_page.graph_files[0],
                         os.getcwd().replace("\\", "/").replace("/test_interface", "") +
                         "/test/domain/resources/graphs/graphs2.g6")
        QTest.mouseClick(self.window.wizard_controller.wizard_window.start_button, Qt.LeftButton)

    def set_up_project_window(self):
        self.assertTrue(self.window.project_controller.project_window.isVisible())
        self.assertEqual(len(project_information_store.filtered_graphs),
                         len(self.window.project_controller.project_tool_bar.combo_graphs))

