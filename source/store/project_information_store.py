import json


class ProjectInformationStore:
    def __init__(self):
        self.project_name = ""
        self.project_location = ""
        self.project_description = ""
        self.equation = ""
        self.conditions = {}
        self.method = ""
        self.graph_files = []
        self.filtered_graphs = []

    def reset_store(self):
        self.project_name = ""
        self.project_location = ""
        self.project_description = ""
        self.equation = ""
        self.conditions = {}
        self.method = ""
        self.graph_files = []
        self.filtered_graphs = []
        self.file_path = ""

    def fill_data(self, data):
        self.project_name = data['project_name']
        self.project_location = data['project_location']
        self.project_description = data['project_description'] if 'project_description' in data.keys() is not None else ''
        self.equation = data['equation']
        self.conditions = data['conditions']
        self.method = data['method']
        self.graph_files = data['graph_files']
        self.filtered_graphs = data['filtered_graphs']

    def save_project(self):
        project_dictionary = {
            "project_name": self.project_name,
            "project_location": self.project_location,
            "project_description": self.project_description,
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


def update_project_store():
    global project_information_store
    project_information_store.fill_data({
        'project_name': wizard_information_store.project_name,
        'project_location': wizard_information_store.project_location,
        'project_description':  wizard_information_store.project_description,
        'equation': wizard_information_store.equation,
        'conditions': wizard_information_store.conditions.copy(),
        'method': wizard_information_store.method,
        'graph_files': wizard_information_store.graph_files.copy(),
        'filtered_graphs': []

    })
    wizard_information_store.reset_store()
    pass


project_information_store = ProjectInformationStore()
wizard_information_store = ProjectInformationStore()
