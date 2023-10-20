import json
import os.path

class ProjectInformationStore:
    def __init__(self):
        self.temp_project_name = ""
        self.temp_project_description = ""
        self.temp_equation = ""
        self.temp_conditions = {}
        self.temp_method = ""
        self.temp_graph_input_files = []
        self.temp_filtered_graphs = []
        self.file_path = ""
        self.current_graph = None
        self.current_graph_pos = {}

    def reset_store(self):
        self.temp_project_name = ""
        self.temp_project_description = ""
        self.temp_equation = ""
        self.temp_conditions = {}
        self.temp_method = ""
        self.temp_graph_input_files = []
        self.temp_filtered_graphs = []

    def fill_data(self, data):
        self.temp_project_name = data['project_name']
        self.temp_project_description = data[
            'project_description'] if 'project_description' in data.keys() is not None else ''
        self.temp_equation = data['equation']
        self.temp_conditions = data['conditions']
        self.temp_method = data['method']
        self.temp_graph_input_files = data['graph_files']
        self.temp_filtered_graphs = data['filtered_graphs']

    def save_project(self):
        project_dictionary = {
            "project_name": self.temp_project_name,
            "project_location": self.file_path,
            "project_description": self.temp_project_description,
            "equation": self.temp_equation,
            "conditions": self.temp_conditions,
            "method": self.temp_method,
            "graph_files": self.temp_graph_input_files,
            "filtered_graphs": self.temp_filtered_graphs
        }
        project_json = json.dumps(project_dictionary)

        project_location = self.file_path.replace('\\', '/')

        filename = f"{project_location}/{self.temp_project_name}"[:-1]

        with open(filename, "w") as file_json:
            file_json.write(project_json)
            file_json.close()

    def get_file_directory(self):
        if os.path.isdir(self.file_path):
            return self.file_path

        file_directory = self.file_path.split('/')
        file_directory = file_directory[: -1]
        file_directory = ''.join(element + '/' for element in file_directory)

        return file_directory

    def get_file_name(self):
        return os.path.basename(self.file_path)

    def get_file_name_without_extension(self):
        return os.path.basename(self.file_path).split('.')[0]

    def get_file_type(self):
        file_name, file_type = os.path.splitext(self.file_path)
        return file_type


def update_project_store():
    global project_information_store
    project_information_store.fill_data({
        'project_name': wizard_information_store.temp_project_name,
        'project_location': wizard_information_store.file_path,
        'project_description': wizard_information_store.temp_project_description,
        'equation': wizard_information_store.temp_equation,
        'conditions': wizard_information_store.temp_conditions.copy(),
        'method': wizard_information_store.temp_method,
        'graph_files': wizard_information_store.temp_graph_input_files.copy(),
        'filtered_graphs': []
    })
    project_information_store.file_path = wizard_information_store.file_path
    wizard_information_store.reset_store()
    pass


project_information_store = ProjectInformationStore()
wizard_information_store = ProjectInformationStore()
