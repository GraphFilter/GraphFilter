class ProjectInformationStore:
    def __init__(self):
        self.project_name = ""
        self.project_folder = ""
        self.equation = ""
        self.conditions = {}
        self.method = ""
        self.graphs = []

    def get_project_name(self):
        return self.project_name

    def get_project_folder(self):
        return self.project_folder

    def get_equation(self):
        return self.equation

    def get_conditions(self):
        return self.conditions

    def get_method(self):
        return self.method

    def get_graphs(self):
        return self.graphs

    def set_project_name(self, project_name):
        self.project_name = project_name

    def set_project_folder(self, project_folder):
        self.project_folder = project_folder

    def set_equation(self, equation):
        self.equation = equation
        print(equation)

    def set_conditions(self, conditions):
        self.conditions = conditions

    def set_method(self, method):
        self.method = method

    def set_graphs(self, graphs):
        self.graphs = graphs


project_information_store = ProjectInformationStore()
