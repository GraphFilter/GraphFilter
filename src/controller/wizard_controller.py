from src.view.wizard.pages.project_files_page import ProjectFilesWizardPage
from src.view.wizard.pages.equations_page import EquationsPage, TabOperations
from src.view.wizard.pages.conditions_page import ConditionsPage, ComboBoxesGroup
from src.view.wizard.pages.method_page import MethodPage
from src.view.wizard.pages.graph_files_page import GraphFilesPage
# from src.view.wizard.pages.review_page import Review
from src.view.project.project_window import ProjectWindow
from src.domain.filter_list import FilterList
from src.store.project_information_store import project_information_store
from src.view.wizard.wizard_window import WizardWindow
from PyQt5.QtWidgets import *
from src.store.operations_invariants import *
from src.domain.equation import Equation
from src.domain.utils import *


class WizardController:
    def __init__(self):
        self.wizard_window = WizardWindow()

        self.filter_list = FilterList()

        self.project_files_page = ProjectFilesWizardPage()
        self.equations_page = EquationsPage()
        self.conditions_page = ConditionsPage()
        self.method_page = MethodPage()
        self.graph_files_page = GraphFilesPage()
        # self.review_page = Review()

        self.project_window_page = ProjectWindow()

    def set_wizard_pages(self):
        self.wizard_window.addPage(self.project_files_page)
        self.wizard_window.addPage(self.equations_page)
        self.wizard_window.addPage(self.conditions_page)
        self.wizard_window.addPage(self.method_page)
        self.wizard_window.addPage(self.graph_files_page)
        # self.wizard_window.addPage(self.review_page)

    def set_equations_tabs(self):
        tab_numeric_invariants = TabOperations(self.add_button_input_to_line_text, dic_num_invariants_names)
        tab_graph_operations = TabOperations(self.add_button_input_to_line_text, dic_graph_operations_names)
        tab_math_operations = TabOperations(self.add_button_input_to_line_text, dic_math_operations_names)

        self.equations_page.math_tab.addTab(tab_numeric_invariants, "Numeric Invariants")
        self.equations_page.math_tab.addTab(tab_graph_operations, "Graph Operations")
        self.equations_page.math_tab.addTab(tab_math_operations, "Math Operations")

    def set_conditions_groups(self):
        structural_invariants_group = ComboBoxesGroup("Structural",
                                                      dic_bool_inv_structural_names,
                                                      self.update_chosen_invariants_conditions)
        spectral_invariants_group = ComboBoxesGroup("Spectral",
                                                    dic_bool_inv_spectral_names,
                                                    self.update_chosen_invariants_conditions)

        self.conditions_page.structural_invariants_group = structural_invariants_group
        self.conditions_page.spectral_invariants_group = spectral_invariants_group

    def connect_buttons(self):
        self.project_files_page.project_location_button.clicked.connect(self.on_open_project_file)
        self.project_files_page.project_name_input.textEdited.connect(self.save_project_name)

        self.equations_page.equation.textEdited.connect(self.on_insert_equation_input)

        self.method_page.filter_button.clicked.connect(self.on_button_method_clicked)
        self.method_page.counter_example_button.clicked.connect(self.on_button_method_clicked)

        self.graph_files_page.open_graph_file.clicked.connect(self.on_update_graph_file)
        self.graph_files_page.add_graph_file.clicked.connect(self.on_add_graph_file)

    def validate_equation(self):
        equation = self.equations_page.equation.text()
        error_message = Equation.validate_expression(equation)

        if len(error_message) == 0:
            self.equations_page.valid_equation = True
        else:
            self.equations_page.valid_equation = False

        self.equations_page.set_label_validation_equation(error_message)

    def update_chosen_invariants_conditions(self):
        radio = QRadioButton().sender()
        groupbox = radio.parentWidget()
        if groupbox.objectName() in project_information_store.get_conditions().keys():
            if project_information_store.get_conditions().get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                project_information_store.conditions.pop(groupbox.objectName())
                print(project_information_store.get_conditions())
                self.update_complete_conditions_page()
                self.conditions_page.completeChanged.emit()
                return

        project_information_store.conditions[groupbox.objectName()] = radio.objectName()
        self.update_complete_conditions_page()
        self.conditions_page.completeChanged.emit()

        print(project_information_store.get_conditions())

    def on_button_method_clicked(self):
        self.method_page.filter_button.setChecked(False)
        self.method_page.counter_example_button.setChecked(False)
        button = QPushButton().sender()
        button.setChecked(True)
        if 'filter' in button.objectName():
            project_information_store.set_method('filter')
        else:
            project_information_store.set_method('counterexample')
        self.method_page.complete = True
        self.method_page.completeChanged.emit()

    def on_wizard_close(self):
        pass

    def on_wizard_start(self):
        pass

    def on_wizard_next_page(self):
        pass

    def on_wizard_cancel(self):
        pass

    def update_complete_conditions_page(self):
        if len(project_information_store.get_conditions()) < 1 and self.equations_page.equation.text() == "":
            self.conditions_page.complete = False
        else:
            self.conditions_page.complete = True

    def update_complete_project_files_page(self):
        if ValidatePath(self.project_files_page.project_location_input):
            self.project_files_page.complete = True
        else:
            self.conditions_page.complete = False

    def show_window(self):
        self.set_wizard_pages()
        self.connect_buttons()
        self.set_conditions_groups()
        self.conditions_page.set_up_layout()
        self.set_equations_tabs()
        self.wizard_window.show()

    def save_project_name(self):
        project_name = self.project_files_page.project_name_input.text()
        project_information_store.set_project_name(project_name)

    def on_open_project_file(self):
        file_dialog = QFileDialog()
        directory_path = file_dialog.getExistingDirectory()
        self.project_files_page.project_location_input.setText(directory_path)
        project_information_store.set_project_folder(directory_path)

    def add_button_input_to_line_text(self):
        button_clicked = QPushButton().sender()
        cursor = self.equations_page.equation.cursorPosition()
        self.equations_page.equation.setText(
            self.equations_page.equation.text()[:cursor] +
            dict_text_equation[button_clicked.text()].code +
            self.equations_page.equation.text()[cursor:]
        )

        self.equations_page.equation.setCursorPosition(cursor + len(dict_text_equation[button_clicked.text()].code))
        self.equations_page.equation.setFocus()
        self.validate_equation()
        self.equations_page.completeChanged.emit()

    def on_update_graph_file(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "Graph Filter (*.g6)"])
        file_path = file_dialog.getOpenFileName(filter="Graph Filter (*.g6)")
        if file_path[0] not in project_information_store.get_graphs() and file_path[0] != '':
            input_file[-1].setText(file_path[0])
            project_information_store.graphs.append(file_path[0])
            self.graph_files_page.add_graph_file.setEnabled(True)
        print(project_information_store.get_graphs())

    def on_add_graph_file(self):
        button_clicked = QPushButton().sender()
        form = button_clicked.parentWidget()
        input_file = form.findChildren(QLineEdit)
        if input_file[-1].text() != '':
            input_file = QLineEdit()
            button = QPushButton("...")
            remove = QPushButton("-")

            button.clicked.connect(self.on_add_graph_file)

            layout = QHBoxLayout()
            layout.addWidget(QLabel("Graph .g6 file:"))
            layout.addWidget(input_file)
            layout.addWidget(button)
            layout.addWidget(remove)

            self.graph_files_page.form.addRow(layout)

            # remove.clicked.connect(lambda: self.remove_row(layout, input_file))
            self.graph_files_page.add_graph_file.setEnabled(False)

    def on_remove_graph_file(self, layout, input_file):
        text = input_file.text()
        if text in project_information_store.graphs:
            project_information_store.graphs.remove(text)
        print(project_information_store.graphs)
        self.graph_files_page.form.removeRow(layout)
        self.graph_files_page.add_graph_file.setEnabled(True)

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

        self.validate_equation()

        self.equations_page.equation.setCursorPosition(cursor)
        self.equations_page.completeChanged.emit()

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
