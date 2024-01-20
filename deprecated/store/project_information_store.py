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


project_information_store = ProjectInformationStore()
