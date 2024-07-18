from view.windows.wizard.pages.project_information_page import ProjectInformationWizardPage
from view.windows.wizard.pages.equations_page import EquationsPage, TabOperations
from view.windows.wizard.pages.conditions_page import ConditionsPage, ComboBoxesGroup
from view.windows.wizard.pages.method_page import MethodPage
from view.windows.wizard.pages.files_page import FilesPage
from view.windows.wizard.pages.review_page import ReviewPage
from deprecated.store.project_information_store import wizard_information_store
from source.view.windows.wizard_window import WizardWindow
from PyQt6.QtWidgets import *
from PyQt6.Qt import QUrl, QDesktopServices
from source.worker.boolean_expression_solver import Expression
from deprecated.utils import *
from PyQt6.QtCore import QStandardPaths as qs


def open_url(url):
    QDesktopServices.openUrl(QUrl(url))


class WizardController:

    def __init__(self):
        self.wizard_window = WizardWindow()
        self.project_files_page = ProjectInformationWizardPage()
        self.equations_page = EquationsPage()
        self.conditions_page = ConditionsPage()
        self.method_page = MethodPage()
        self.graph_files_page = FilesPage()
        self.review_page = ReviewPage()
        self.number_of_pages = 0

        self.set_up_window()

    def set_wizard_pages(self):
        self.wizard_window.addPage(self.method_page)
        self.wizard_window.addPage(self.project_files_page)
        self.number_of_pages = 2

    def add_filter_wizard_pages(self):
        if self.number_of_pages != 6:
            try:
                self.wizard_window.addPage(self.equations_page)
                self.wizard_window.addPage(self.conditions_page)
                self.wizard_window.addPage(self.graph_files_page)
                self.wizard_window.addPage(self.review_page)
                self.number_of_pages += 4
            except:
                pass
        else:
            pass
        self.enable_method_page_buttons()

    def remove_filter_wizard_pages(self):
        if self.number_of_pages != 2:
            try:
                self.wizard_window.removePage(2)
                self.wizard_window.removePage(3)
                self.wizard_window.removePage(4)
                self.wizard_window.removePage(5)
                self.number_of_pages -= 4
            except:
                pass
        else:
            pass
        self.enable_method_page_buttons()

    def enable_method_page_buttons(self):
        self.method_page.blank_project.setEnabled(True)
        self.method_page.filter_button.setEnabled(True)
        self.method_page.find_example_button.setEnabled(True)

    def disable_method_page_buttons(self):
        self.method_page.blank_project.setDisabled(True)
        self.method_page.filter_button.setDisabled(True)
        self.method_page.find_example_button.setDisabled(True)

    def set_up_window(self):
        self.set_wizard_pages()
        self.connect_events()
        self.set_default_project_location()
        self.set_conditions_groups()
        self.conditions_page.set_up_layout()
        self.set_equations_tabs()

    def on_wizard_page_change(self):
        if self.wizard_window.currentPage() == self.conditions_page:
            self.update_conditions_page()
        if self.wizard_window.currentPage() == self.method_page:
            self.update_complete_method_page()
        if self.wizard_window.currentPage() == self.graph_files_page:
            self.update_complete_graph_files_page()

    def set_alert_text(self):
        pass

    def update_conditions_page(self):
        if self.is_conditions_page_complete():
            self.conditions_page.complete = False
        else:
            self.conditions_page.complete = True

    def is_conditions_page_complete(self):
        return len(wizard_information_store.temp_conditions) < 1 and self.equations_page.equation.text() == ""

    def update_complete_method_page(self):
        self.wizard_window.next_button.setToolTip('Select the filtering method')

    def update_complete_graph_files_page(self):
    def update_complete_graph_files_page(self):
        if self.graph_files_page.list_files_input.count() == 0:
            self.graph_files_page.complete = False
            self.wizard_window.next_button.setToolTip('Insert at least one graph file')
        else:
            self.wizard_window.next_button.setToolTip('')
            self.graph_files_page.complete = True
        self.graph_files_page.completeChanged.emit()
        self.wizard_window.next_button.clicked.connect(self.store_graph_files)

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
        self.project_files_page.project_description_input.textChanged.connect(self.save_project_description)

    def connect_equations_page_events(self):
        self.equations_page.equation.textEdited.connect(self.on_insert_equation_input)

    def connect_method_page_events(self):
        self.method_page.filter_button.clicked.connect(self.on_button_method_clicked)
        self.method_page.find_example_button.clicked.connect(self.on_button_method_clicked)
        self.method_page.blank_project.clicked.connect(self.on_button_method_clicked)

    def connect_graph_files_page_events(self):

        self.graph_files_page.update_file.clicked.connect(self.on_update_graph_file)
        self.graph_files_page.add_file.clicked.connect(self.on_add_graph_file)
        self.graph_files_page.remove_file.clicked.connect(self.on_remove_graph_file)
        self.graph_files_page.remove_all_files.clicked.connect(self.on_remove_all_files)
        self.graph_files_page.list_files_input.itemClicked.connect(
            lambda: self.graph_files_page.update_file.setEnabled(
                len(self.graph_files_page.list_files_input.selectedItems()) == 1))
        self.graph_files_page.list_files_input.itemClicked.connect(
            lambda: self.graph_files_page.remove_file.setEnabled(True))
        self.graph_files_page.download_button_hog.clicked.connect(
            lambda: open_url("https://houseofgraphs.org/meta-directory"))
        self.graph_files_page.download_button_mckay.clicked.connect(
            lambda: open_url("http://users.cecs.anu.edu.au/~bdm/data/graphs.html"))

    def connect_events(self):
        self.wizard_window.currentIdChanged.connect(self.on_wizard_page_change)
        self.wizard_window.help_button.clicked.connect(self.open_message_box)
        self.connect_project_files_page_events()
        self.connect_equations_page_events()
        self.connect_method_page_events()
        self.connect_graph_files_page_events()

    def open_message_box(self):
        message_box = MessageBox(self.wizard_window.currentPage().alert_text)
        message_box.exec()

    def verify_and_save_project_name(self):
        if validate_file_name(self.project_files_page.project_name_input.text()):
            self.update_complete_project_files_page(complete_project_name=True)
            project_name = self.project_files_page.project_name_input.text()
            wizard_information_store.temp_project_name = project_name
            self.review_page.set_project_name(project_name)
        else:
            self.update_complete_project_files_page(complete_project_name=False)
            self.update_complete_project_files_page(complete_project_name=False)


    def verify_and_save_project_folder(self):
        if validate_path(self.project_files_page.project_location_input.text()):
            self.update_complete_project_files_page(complete_project_location=True)
            project_location = self.project_files_page.project_location_input.text()
            wizard_information_store.file_path = project_location
            self.review_page.set_project_location(project_location)
        else:
            self.update_complete_project_files_page(complete_project_location=False)

    def save_project_description(self):
        description = self.project_files_page.project_description_input.toPlainText()
        wizard_information_store.temp_project_description = description
        self.review_page.set_project_description(description)

    def on_open_project_file(self):
        file_dialog = QFileDialog.getExistingDirectory(
            directory=wizard_information_store.file_path)
        directory_path = file_dialog

        if directory_path != "":
            self.project_files_page.project_location_input.setText(directory_path)
            self.verify_and_save_project_folder()
        else:
            self.project_files_page.project_location_input.setText(wizard_information_store.file_path)

    def set_default_project_location(self):
        default_path = qs.writableLocation(qs.DocumentsLocation)
        self.project_files_page.project_location_input.setText(default_path)
        wizard_information_store.file_path = default_path
        self.review_page.set_project_location(default_path)
        self.wizard_window.next_button.setToolTip('Invalid Project Name')

    def set_equations_tabs(self):
        n = len(dic_num_inv_spectral_names)
        dic_num_inv_spectral_names1 = dict(list(dic_num_inv_spectral_names.items())[0: 30])
        dic_num_inv_spectral_names2 = dict(list(dic_num_inv_spectral_names.items())[30: n])

        tab_num_structural_invariants = TabOperations(self.add_button_input_to_equation_text,
                                                      dic_num_inv_structural_names)
        tab_num_spectral_invariants1 = TabOperations(self.add_button_input_to_equation_text,
                                                     dic_num_inv_spectral_names1)
        tab_num_spectral_invariants2 = TabOperations(self.add_button_input_to_equation_text,
                                                     dic_num_inv_spectral_names2)
        tab_graph_operations = TabOperations(self.add_button_input_to_equation_text, dic_graph_operations_names)
        tab_math_operations = TabOperations(self.add_button_input_to_equation_text, dic_math_and_basic_operations_names)

        self.equations_page.math_tab.addTab(tab_num_structural_invariants, "Structural Invariants")
        self.equations_page.math_tab.addTab(tab_num_spectral_invariants1, "Spectral Invariants [1]")
        self.equations_page.math_tab.addTab(tab_num_spectral_invariants2, "Spectral Invariants [2]")
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
        error_message = Expression.validate(equation)

        if len(error_message) == 0:
            self.equations_page.complete = True
            wizard_information_store.temp_equation = equation
            self.review_page.set_equation(equation)
            if equation == '':
                self.update_conditions_page()
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
        if groupbox.objectName() in wizard_information_store.temp_conditions.keys():
            if wizard_information_store.temp_conditions.get(groupbox.objectName()) == radio.objectName():
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
                wizard_information_store.temp_conditions.pop(groupbox.objectName())
                print(wizard_information_store.temp_conditions)
                self.review_page.set_conditions(wizard_information_store.temp_conditions)
                self.update_conditions_page()
                self.conditions_page.completeChanged.emit()
                return

        wizard_information_store.temp_conditions[groupbox.objectName()] = radio.objectName()
        self.review_page.set_conditions(wizard_information_store.temp_conditions)
        self.update_conditions_page()
        self.conditions_page.completeChanged.emit()

        # print(wizard_information_store.temp_conditions)

    def on_button_method_clicked(self):
        self.method_page.filter_button.setChecked(False)
        self.method_page.find_example_button.setChecked(False)
        self.method_page.blank_project.setChecked(False)
        button = QPushButton().sender()
        button.setChecked(True)

        if 'blank' in button.objectName():
            self.project_files_page.setFinalPage(True)
            wizard_information_store.temp_method = 'blank'
            self.review_page.set_method('blank')
            self.disable_method_page_buttons()
            self.project_files_page.project_description_input.setDisabled(True)
            self.remove_filter_wizard_pages()
        if 'filter' in button.objectName():
            self.project_files_page.setFinalPage(False)
            wizard_information_store.temp_method = 'filter'
            self.review_page.set_method('filter')
            self.disable_method_page_buttons()
            self.project_files_page.project_description_input.setDisabled(False)
            self.add_filter_wizard_pages()
        if 'find_example' in button.objectName():
            self.project_files_page.setFinalPage(False)
            wizard_information_store.temp_method = 'find_example'
            self.review_page.set_method('find_example')
            self.disable_method_page_buttons()
            self.project_files_page.project_description_input.setDisabled(False)
            self.add_filter_wizard_pages()
        self.method_page.complete = True
        self.method_page.completeChanged.emit()
        self.wizard_window.next_button.setToolTip('')

    def on_update_graph_file(self):
        number_of_files = self.graph_files_page.list_files_input.count()
        self.on_add_graph_file()
        if number_of_files != self.graph_files_page.list_files_input.count():
            self.on_remove_graph_file()

    def on_insert_graph_file_path(self):
        line_input = QLineEdit().sender()
        path = line_input.text()
        self.save_graph_file_path(path, line_input)

    def save_graph_file_path(self, path, line_input):
        if validate_file(path):
            if path not in wizard_information_store.temp_graph_input_files and path != '':

                if line_input.text() != '' and line_input.text() in wizard_information_store.temp_graph_input_files:
                    wizard_information_store.temp_graph_input_files.remove(line_input.text())
                line_input.setText(path)
                wizard_information_store.temp_graph_input_files.append(path)
                self.review_page.set_graph_files(wizard_information_store.temp_graph_input_files)
                self.graph_files_page.add_file.setEnabled(True)
            elif path == '':
                self.graph_files_page.complete = False
            self.graph_files_page.complete = True
        else:
            self.graph_files_page.complete = False
        # print(wizard_information_store.temp_graph_input_files)
        self.update_complete_graph_files_page()

    def on_add_graph_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt *.txt.gz)", "Graph6 File (*.g6 *.g6.gz)"])
        file_path = file_dialog.getOpenFileNames(
            filter="Graph6 Files (*.g6 *.txt *.g6.gz *.txt.gz);;"
                   "Text files (*.txt *.txt.gz);;"
                   "Graph6 files (*.g6 *.g6.gz)"
        )
        for file_name in file_path[0]:
            duplicate_file = False
            for i in range(self.graph_files_page.list_files_input.count()):
                if self.graph_files_page.list_files_input.item(i).text() == file_name:
                    duplicate_file = True
            if not duplicate_file:
                self.graph_files_page.list_files_input.addItem(file_name)
        self.graph_files_page.remove_all_files.setEnabled(True)
        self.update_complete_graph_files_page()

    def on_remove_graph_file(self):
        list_files = self.graph_files_page.list_files_input
        for item in list_files.selectedItems():
            list_files.takeItem(list_files.row(item))
        self.graph_files_page.remove_file.setEnabled(False)
        self.graph_files_page.update_file.setEnabled(False)
        if list_files.count() == 0:
            self.graph_files_page.remove_all_files.setEnabled(False)
        self.update_complete_graph_files_page()

    def on_remove_all_files(self):
        self.graph_files_page.list_files_input.clear()
        self.graph_files_page.remove_file.setEnabled(False)
        self.graph_files_page.update_file.setEnabled(False)
        self.graph_files_page.remove_all_files.setEnabled(False)
        self.update_complete_graph_files_page()

    def store_graph_files(self):
        list_files = self.graph_files_page.list_files_input
        wizard_information_store.temp_graph_input_files = [list_files.item(x).text() for x in range(list_files.count())]
        self.review_page.set_graph_files(wizard_information_store.temp_graph_input_files)
