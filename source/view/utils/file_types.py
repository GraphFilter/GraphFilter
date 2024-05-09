class FileTypes:

    def __call__(self):
        return self

    def __init__(self, name="", type_list=None):
        if type_list is None:
            type_list = []
        self.name: str = None if name is None else name
        self.type_list: list = [] if type_list is None else type_list
        self.type_in_full = f"{self.name} {self.to_formatted_string()}"

    def to_formatted_string(self):
        return ' '.join(['*' + ext if ext.startswith('.') else '*' + ext[1:] for ext in self.type_list])


class GraphTypes(FileTypes):

    def __init__(self):
        name = "Graph Files"
        type_list = [".g6", ".txt", ".g6.gz", ".txt.gz"]
        super().__init__(name, type_list)
