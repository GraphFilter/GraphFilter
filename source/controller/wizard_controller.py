from source.view.wizard.pages.project_files_page import ProjectFilesWizardPage
from source.view.wizard.pages.equations_page import EquationsPage, TabOperations
from source.view.wizard.pages.conditions_page import ConditionsPage, ComboBoxesGroup
from source.view.wizard.pages.method_page import MethodPage
from source.view.wizard.pages.graph_files_page import GraphFilesPage
from source.view.wizard.pages.review_page import ReviewPage
from source.store.project_information_store import wizard_information_store
from source.view.wizard.wizard_window import WizardWindow
from PyQt5.QtWidgets import *
from source.store.operations_invariants import *
from source.domain.equation import Equation
from source.domain.utils import *
import pathlib


class WizardController:
    def __init__(self):
        self.wizard_window = WizardWindow()
        self.project_files_page = ProjectFilesWizardPage()
        self.equations_page = EquationsPage()
        self.conditions_page = ConditionsPage()
        self.method_page = MethodPage()
        self.graph_files_page = GraphFilesPage()
        self.review_page = ReviewPage()

        self.set_up_window()

    def set_wizard_pages(self):
        self.wizard_window.addPage(self.project_files_page)
        self.wizard_window.addPage(self.equations_page)
        self.wizard_window.addPage(self.conditions_page)
        self.wizard_window.addPage(self.method_page)
        self.wizard_window.addPage(self.graph_files_page)
        self.wizard_window.addPage(self.review_page)

    def set_up_window(self):
        self.set_wizard_pages()
        self.connect_events()
        self.set_default_project_location()
        self.set_conditions_groups()
        self.conditions_page.set_up_layout()
        self.set_equations_tabs()

    def on_wizard_next_page(self):
        if self.wizard_window.currentPage().objectName() == "conditions":
            self.update_complete_conditions_page()
        if self.wizard_window.currentPage().objectName() == "method":
            self.wizard_window.next_button.setToolTip('Select the filtering method')
        if self.wizard_window.currentPage().objectName() == "graph_files":
            self.update_complete_graph_files_page()

    def update_complete_conditions_page(self):
        if len(wizard_information_store.conditions) < 1 and self.equations_page.equation.text() == "":
            self.conditions_page.complete = False
            self.wizard_window.next_button.setToolTip('Equation or conditions must be filled')
        else:
            self.conditions_page.complete = True
            self.wizard_window.next_button.setToolTip('')

    def update_complete_graph_files_page(self):
        if self.graph_files_page.complete:
            self.wizard_window.next_button.setToolTip('')
        else:
            self.wizard_window.next_button.setToolTip('Invalid graph file')
        self.graph_files_page.completeChanged.emit()

    def update_complete_project_files_page(self, complete_project_name=None, complete_project_location=None):
        if complete_project_name is not None:
            self.project_files_page.complete_project_name = complete_project_name
        if complete_project_location is not None:
            self.project_files_page.complete_project_location = complete_project_location

        if not self.project_files_page.complete_project_name and not self.project_files_page.complete_project_location:
            self.wizard_window.next_button.setToolTip('Invalid Project Name and Project Location')
        elif not self.project_files_page.complete_project_location:
            self.wizard_window.next_button.setToolTip('Invalid Project Location')
        elif not self.project_files_page.complete_project_name:
            self.wizard_window.next_button.setToolTip('Invalid Project Name')
        else:
            self.wizard_window.next_button.setToolTip('')

        self.project_files_page.completeChanged.emit()

    def show_window(self):
        self.wizard_window.show()

    def close_window(self):
        self.wizard_window.close()

    def connect_project_files_page_events(self):
        self.project_files_page.project_name_input.textEdited.connect(self.verify_and_save_project_name)
        self.project_files_page.project_location_button.clicked.connect(self.on_open_project_file)
        self.project_files_page.project_location_input.textEdited.connect(self.verify_and_save_project_folder)

    def connect_equations_page_events(self):
        self.equations_page.equation.textEdited.connect(self.on_insert_equation_input)

    def connect_method_page_events(self):
        self.method_page.filter_button.clicked.connect(self.on_button_method_clicked)
        self.method_page.counter_example_button.clicked.connect(self.on_button_method_clicked)

    def connect_graph_files_page_events(self):
        self.graph_files_page.open_graph_file.clicked.connect(self.on_update_graph_file)
        self.graph_files_page.add_graph_file.clicked.connect(self.on_add_graph_file_input)
        self.graph_files_page.graph_files_input.textEdited.connect(self.on_insert_graph_file_path)

    def connect_events(self):
        self.wizard_window.next_button.clicked.connect(self.on_wizard_next_page)

        self.connect_project_files_page_events()
        self.connect_equations_page_events()
        self.connect_method_page_events()
        self.connect_graph_files_page_events()

    def verify_and_save_project_name(self):
        if validate_file_name(self.project_files_page.project_name_input.text()):
            self.update_complete_project_files_page(complete_project_name=True)
            project_name = self.project_files_page.project_name_input.text()
            wizard_information_store.project_name = project_name
            self.review_page.set_project_name(project_name)
        else:
            self.update_complete_project_files_page(complete_project_name=False)

    def verify_and_save_project_folder(self):
        if validate_path(self.project_files_page.project_location_input.text()):
            self.update_complete_project_files_page(complete_project_location=True)
            project_location = self.project_files_page.project_location_input.text()
            wizard_information_store.project_location = project_location
            self.review_page.set_project_location(project_location)
        else:
            self.update_complete_project_files_page(complete_project_location=False)

    def on_open_project_file(self):
        file_dialog = QFileDialog()
        directory_path = file_dialog.getExistingDirectory()
        self.project_files_page.project_location_input.setText(directory_path)
        self.verify_and_save_project_folder()

    def set_default_project_location(self):
        default_path = str(pathlib.Path().absolute())
        self.project_files_page.project_location_input.setText(default_path)
        wizard_information_store.project_location = default_path
        self.review_page.set_project_location(default_path)
        self.wizard_window.next_button.setToolTip('Invalid Project Name')

    def set_equations_tabs(self):
        tab_numeric_invariants = TabOperations(self.add_button_input_to_equation_text, dic_num_invariants_names)
        tab_graph_operations = TabOperations(self.add_button_input_to_equation_text, dic_graph_operations_names)
        tab_math_operations = TabOperations(self.add_button_input_to_equation_text, dic_math_and_basic_operations_names)

        self.equations_page.math_tab.addTab(tab_numeric_invariants, "Numeric Invariants")
        self.equations_page.math_tab.addTab(tab_graph_operations, "Graph Operations")
        self.equations_page.math_tab.addTab(tab_math_operations, "Math Operations")

    def add_button_input_to_equation_text(self):
        button_clicked = QPushButton().sender()
        cursor = self.equations_page.equation.cursorPosition()

        if dict_text_equation[button_clicked.text()].is_a_function:
            self.equations_page.equation.setText(
                self.equations_page.equation.text()[:cursor] +
                dict_text_equation[button_clicked.text()].code + "()" +
                self.equations_page.equation.text()[cursor:]
            )
            self.equations_page.equation.setCursorPosition(
                cursor + len(dict_text_equation[button_clicked.text()].code) + 1)
        else:
            self.equations_page.equation.setText(
                self.equations_page.equation.text()[:cursor] +
                dict_text_equation[button_clicked.text()].code +
                self.equations_page.equation.text()[cursor:]
            )
            self.equations_page.equation.setCursorPosition(cursor + len(dict_text_equation[button_clicked.text()].code))

        self.equations_page.equation.setFocus()
        self.validate_and_save_equation()
        self.equations_page.completeChanged.emit()

    def on_insert_equation_input(self):
        text_equation = self.equations_page.equation.text()
        cursor = self.equations_page.equation.cursorPosition()

        if len(text_equation) == 0:
            self.conditions_page.complete = False
        else:
            self.conditions_page.complete = True

        for text, symbol in dict_text_equation.items():
            text_equation = text_equation.replace(text, symbol.code)
            text_equation = text_equation.replace(str(text).lower(), symbol.code)
            text_equation = text_equation.replace(str(text).replace(" ", ""), symbol.code)
            text_equation = text_equation.replace(str(text).lower().replace(" ", ""), symbol.code)
        for text, symbol in dic_math_symbols.items():
            text_equation = text_equation.replace(text, symbol)
        self.equations_page.equation.setText(text_equation)

        self.validate_and_save_equation()

        self.equations_page.equation.setCursorPosition(cursor)
        self.equations_page.completeChanged.emit()

    def validate_and_save_equation(self):
        equation = self.equations_page.equation.text()
        error_message = Equation.validate_expression(equation)

        if len(error_message) == 0:
            self.equations_page.complete = True
            wizard_information_store.equation = equation
            self.review_page.set_equation(equation)
            if equation == '':
                self.update_complete_conditions_page()
        else:
            self.equations_page.complete = False
            self.wizard_window.next_button.setToolTip('Insert a valid (in)equation or none')

        self.equations_page.set_label_validation_equation(error_message)

    def set_conditions_groups(self):
        structural_invariants_group = ComboBoxesGroup("Structural",
                                                      dic_bool_inv_structural_names,
                                                      self.update_chosen_invariants_conditions)
        spectral_invariants_group = ComboBoxesGroup("Spectral",
                                                    dic_bool_inv_spectral_names,
                                                    self.update_chosen_invariants_conditions)

        self.conditions_page.structural_invariants_group = structural_invariants_group
        self.conditions_page.spectral_invariants_group = spectral_invariants_group

    def update_chosen_invariants_conditions(self):
        radio = QRadioButton().sender()
        groupbox = radio.parentWidget()
        if groupbox.objectName() in wizard_information_store.conditions.keys():
            if wizard_information_store.conditions.get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                wizard_information_store.conditions.pop(groupbox.objectName())
                print(wizard_information_store.conditions)
                self.update_complete_conditions_page()
                self.conditions_page.completeChanged.emit()
                return

        wizard_information_store.conditions[groupbox.objectName()] = radio.objectName()
        self.review_page.set_conditions(wizard_information_store.conditions)
        self.update_complete_conditions_page()
        self.conditions_page.completeChanged.emit()

        print(wizard_information_store.conditions)

    def on_button_method_clicked(self):
        self.method_page.filter_button.setChecked(False)
        self.method_page.counter_example_button.setChecked(False)
        button = QPushButton().sender()
        button.setChecked(True)
        if 'filter' in button.objectName():
            wizard_information_store.method = 'filter'
            self.review_page.set_method('filter')
        else:
            wizard_information_store.method = 'counterexample'
            self.review_page.set_method('counterexample')
        self.method_page.complete = True
        self.method_page.completeChanged.emit()
        self.wizard_window.next_button.setToolTip('')

    def on_update_graph_file(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Graph Filter (*.g6)"])
        # self.graph_files_page.tr("Text files (*.g6)")
        file_path = file_dialog.getOpenFileName(filter="Graph6 Files (*.g6 *.txt);;Text files (*.txt);;Graph6 files (*.g6)")
        self.save_graph_file_path(file_path[0], input_file[-1])

    def on_insert_graph_file_path(self):
        line_input = QLineEdit().sender()
        path = line_input.text()
        self.save_graph_file_path(path, line_input)

    def save_graph_file_path(self, path, line_input):
        if validate_file(path):
            if path not in wizard_information_store.graph_files and path != '':
                if line_input.text() != '' and line_input.text() in wizard_information_store.graph_files:
                    wizard_information_store.graph_files.remove(line_input.text())
                line_input.setText(path)
                wizard_information_store.graph_files.append(path)
                self.review_page.set_graph_files(wizard_information_store.graph_files)
                self.graph_files_page.add_graph_file.setEnabled(True)
            elif path == '':
                self.graph_files_page.complete = False
            self.graph_files_page.complete = True
        else:
            self.graph_files_page.complete = False
        print(wizard_information_store.graph_files)
        self.update_complete_graph_files_page()

    def on_add_graph_file_input(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        if input_file[-1].text() != '':

            input_file = QLineEdit()
            input_file.textEdited.connect(self.on_insert_graph_file_path)

            button = QPushButton("...")
            remove = QPushButton("-")

            button.clicked.connect(self.on_update_graph_file)

            layout = QHBoxLayout()
            layout.addWidget(QLabel("Graph .g6 file:"))
            layout.addWidget(input_file)
            layout.addWidget(button)
            layout.addWidget(remove)

            self.graph_files_page.form.addRow(layout)

            remove.clicked.connect(lambda: self.on_remove_graph_file(layout, input_file))
            self.graph_files_page.add_graph_file.setEnabled(False)

    def on_remove_graph_file(self, layout, input_file):
        text = input_file.text()
        if text in wizard_information_store.graph_files:
            wizard_information_store.graph_files.remove(text)
            self.review_page.set_graph_files(wizard_information_store.graph_files)
        print(wizard_information_store.graph_files)
        self.graph_files_page.form.removeRow(layout)
        self.graph_files_page.add_graph_file.setEnabled(True)

        if len(wizard_information_store.graph_files) == 0:
            self.graph_files_page.complete = False

        self.update_complete_graph_files_page()
