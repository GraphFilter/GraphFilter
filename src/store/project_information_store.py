import json


class ProjectInformationStore:
    def __init__(self):
        self.project_name = ""
        self.project_location = ""
        self.equation = ""
        self.conditions = {}
        self.method = ""
        self.graph_files = []
        self.filtered_graphs = []

    def fill_data(self, data):
        self.project_name = data['project_name']
        self.project_location = data['project_location']
        self.equation = data['equation']
        self.conditions = data['conditions']
        self.method = data['method']
        self.graph_files = data['graph_files']
        self.filtered_graphs = data['filtered_graphs']

    def save_project(self):
        project_dictionary = {
            "project_name": self.project_name,
            "project_location": self.project_location,
            "equation": self.equation,
            "conditions": self.conditions,
            "method": self.method,
            "graph_files": self.graph_files,
            "filtered_graphs": self.filtered_graphs
        }
        project_json = json.dumps(project_dictionary)

        project_location = self.project_location.replace('\\', '/')

        filename = f"{project_location}/{self.project_name}.json"

        with open(filename, "w") as file_json:
            file_json.write(project_json)
            file_json.close()


project_information_store = ProjectInformationStore()
