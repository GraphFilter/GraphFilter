class FileTypes:
    def __init__(self):
        self.name: str = None
        self.type_list: list = []
        self.type_in_full: str = ""

    def transform_list_to_formatted_string(self):
        formatted_string = ' '.join(['*' + ext if ext.startswith('.') else '*' + ext[1:] for ext in self.type_list])
        return formatted_string


class GraphTypes(FileTypes):

    def __init__(self):
        super().__init__()
        self.name = "Graph Files"
        self.type_list = [".g6", ".txt", ".g6.gz", ".txt.gz"]
        self.type_in_full = f"{self.name} {self.transform_list_to_formatted_string()}"
