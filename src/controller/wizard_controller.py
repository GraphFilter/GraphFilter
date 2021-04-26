from src.view.wizard.pages.project_files_page import ProjectFilesWizardPage
from src.view.wizard.pages.equations_page import EquationsPage, TabOperations
from src.view.wizard.pages.conditions_page import ConditionsPage, ComboBoxesGroup
from src.view.wizard.pages.method_page import MethodPage
from src.view.wizard.pages.graph_files_page import GraphFilesPage
from src.view.wizard.pages.review_page import ReviewPage
from src.view.project.project_window import ProjectWindow
from src.domain.filter_list import FilterList
from src.store.project_information_store import project_information_store
from src.view.wizard.wizard_window import WizardWindow
from PyQt5.QtWidgets import *
from src.store.operations_invariants import *
from src.domain.equation import Equation
from src.domain.utils import *
import pathlib


class WizardController:
    def __init__(self):
        self.wizard_window = WizardWindow()

        self.filter_list = FilterList()

        self.project_files_page = ProjectFilesWizardPage()
        self.equations_page = EquationsPage()
        self.conditions_page = ConditionsPage()
        self.method_page = MethodPage()
        self.graph_files_page = GraphFilesPage()
        self.review_page = ReviewPage()

        self.project_window_page = ProjectWindow()

    def set_wizard_pages(self):
        self.wizard_window.addPage(self.project_files_page)
        self.wizard_window.addPage(self.equations_page)
        self.wizard_window.addPage(self.conditions_page)
        self.wizard_window.addPage(self.method_page)
        self.wizard_window.addPage(self.graph_files_page)
        self.wizard_window.addPage(self.review_page)

    def on_wizard_close(self):
        pass

    def on_wizard_start(self):
        pass

    def on_wizard_next_page(self):
        if self.wizard_window.currentPage().objectName() == "conditions":
            self.update_complete_conditions_page()
        if self.wizard_window.currentPage().objectName() == "method":
            self.wizard_window.next_button.setToolTip('Select the filtering method')
        if self.wizard_window.currentPage().objectName() == "graph_files":
            self.update_complete_graph_files_page(False)


    def on_wizard_cancel(self):
        pass

    def update_complete_conditions_page(self):
        if len(project_information_store.conditions) < 1 and self.equations_page.equation.text() == "":
            self.conditions_page.complete = False
            self.wizard_window.next_button.setToolTip('Equation or conditions must be filled')
        else:
            self.conditions_page.complete = True
            self.wizard_window.next_button.setToolTip('')

    def update_complete_graph_files_page(self, state):
        if state:
            self.graph_files_page.complete = True
            self.wizard_window.next_button.setToolTip('')
        else:
            self.graph_files_page.complete = False
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
        self.set_wizard_pages()
        self.connect_buttons()
        self.set_default_project_location()
        self.set_conditions_groups()
        self.conditions_page.set_up_layout()
        self.set_equations_tabs()
        self.wizard_window.show()

    def start_filter(self):
        # list_g6_in = []
        # for file in self.graph_files.files_added:
        #     list_g6_in.extend(open(file, 'r').read().splitlines())
        #
        # expression = self.equations.equation.text()
        #
        # list_inv_bool_choices = self.conditions.dict_inv_bool_choices.items()
        #
        # self.filter_backend.set_inputs(list_g6_in, expression, list_inv_bool_choices)
        # self.save_project()
        #
        # if self.method.method == 'filter':
        #     self.filter_backend.run_filter()
        # elif self.method.method == 'counterexample':
        #     self.filter_backend.run_find_counterexample()
        #
        # # TODO: Use the percentage returned by filtering
        # self.project_window.visualize.fill_combo(self.filter_backend.list_out)
        # self.project_window.show()
        pass

    def connect_buttons(self):

        self.wizard_window.next_button.clicked.connect(self.on_wizard_next_page)

        self.project_files_page.project_location_button.clicked.connect(self.on_open_project_file)
        self.project_files_page.project_location_input.textEdited.connect(self.verify_and_save_project_folder)

        self.project_files_page.project_name_input.textEdited.connect(self.verify_and_save_project_name)

        self.equations_page.equation.textEdited.connect(self.on_insert_equation_input)

        self.method_page.filter_button.clicked.connect(self.on_button_method_clicked)
        self.method_page.counter_example_button.clicked.connect(self.on_button_method_clicked)

        self.graph_files_page.open_graph_file.clicked.connect(self.on_update_graph_file)
        self.graph_files_page.add_graph_file.clicked.connect(self.on_add_graph_file_input)

        self.graph_files_page.graph_files_input.textEdited.connect(self.on_insert_graph_file_path)

    def verify_and_save_project_name(self):
        if validate_file_name(self.project_files_page.project_name_input.text()):
            self.update_complete_project_files_page(complete_project_name=True)
            project_name = self.project_files_page.project_name_input.text()
            project_information_store.project_name = project_name
            self.review_page.set_project_name(project_name)
        else:
            self.update_complete_project_files_page(complete_project_name=False)

    def verify_and_save_project_folder(self):
        if validate_path(self.project_files_page.project_location_input.text()):
            self.update_complete_project_files_page(complete_project_location=True)
            project_location = self.project_files_page.project_location_input.text()
            project_information_store.project_location = project_location
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
        project_information_store.project_location = default_path
        self.review_page.set_project_location(default_path)
        self.wizard_window.next_button.setToolTip('Invalid Project Name')

    def set_equations_tabs(self):
        tab_numeric_invariants = TabOperations(self.add_button_input_to_equation_text, dic_num_invariants_names)
        tab_graph_operations = TabOperations(self.add_button_input_to_equation_text, dic_graph_operations_names)
        tab_math_operations = TabOperations(self.add_button_input_to_equation_text, dic_math_operations_names)

        self.equations_page.math_tab.addTab(tab_numeric_invariants, "Numeric Invariants")
        self.equations_page.math_tab.addTab(tab_graph_operations, "Graph Operations")
        self.equations_page.math_tab.addTab(tab_math_operations, "Math Operations")

    def add_button_input_to_equation_text(self):
        button_clicked = QPushButton().sender()
        cursor = self.equations_page.equation.cursorPosition()
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
        self.equations_page.equation.setText(text_equation)

        self.validate_and_save_equation()

        self.equations_page.equation.setCursorPosition(cursor)
        self.equations_page.completeChanged.emit()

    def validate_and_save_equation(self):
        equation = self.equations_page.equation.text()
        error_message = Equation.validate_expression(equation)

        if len(error_message) == 0:
            self.equations_page.complete = True
            project_information_store.equation = equation
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
        if groupbox.objectName() in project_information_store.conditions.keys():
            if project_information_store.conditions.get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                project_information_store.conditions.pop(groupbox.objectName())
                print(project_information_store.conditions)
                self.update_complete_conditions_page()
                self.conditions_page.completeChanged.emit()
                return

        project_information_store.conditions[groupbox.objectName()] = radio.objectName()
        self.review_page.set_conditions(project_information_store.conditions)
        self.update_complete_conditions_page()
        self.conditions_page.completeChanged.emit()

        print(project_information_store.conditions)

    def on_button_method_clicked(self):
        self.method_page.filter_button.setChecked(False)
        self.method_page.counter_example_button.setChecked(False)
        button = QPushButton().sender()
        button.setChecked(True)
        if 'filter' in button.objectName():
            project_information_store.method = 'filter'
            self.review_page.set_method('filter')
        else:
            project_information_store.method = 'counterexample'
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
        file_path = file_dialog.getOpenFileName(filter="Graph Filter (*.g6)")
        self.save_graph_file_path(file_path[0], input_file[-1])

    def on_insert_graph_file_path(self):
        line_input = QLineEdit().sender()
        path = line_input.text()
        self.save_graph_file_path(path, line_input)

    def save_graph_file_path(self, path, line_input):
        if validate_file(path):
            if path not in project_information_store.graphs and path != '':
                if line_input.text() != '' and line_input.text() in project_information_store.graphs:
                    project_information_store.graphs.remove(line_input.text())
                line_input.setText(path)
                project_information_store.graphs.append(path)
                self.review_page.set_graph_files(project_information_store.graphs)
                self.graph_files_page.add_graph_file.setEnabled(True)
            self.update_complete_graph_files_page(True)
        else:
            self.update_complete_graph_files_page(False)
        print(project_information_store.graphs)

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
        if text in project_information_store.graphs:
            project_information_store.graphs.remove(text)
            self.review_page.set_graph_files(project_information_store.graphs)
        print(project_information_store.graphs)
        self.graph_files_page.form.removeRow(layout)
        self.graph_files_page.add_graph_file.setEnabled(True)
        self.update_complete_graph_files_page()

