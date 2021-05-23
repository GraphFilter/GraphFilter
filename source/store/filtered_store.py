class FilteredStore:
    def __init__(self):
        self.filtered_graphs = []
        self.changed_graphs = []

    def get_filtered_graphs(self):
        return self.filtered_graphs

    def set_filtered_graphs(self, filtered_graphs):
        self.filtered_graphs = filtered_graphs

    def add_filtered_graph(self, filtered_graph):
        self.filtered_graphs.insert(filtered_graph)

    def get_changed_graphs(self):
        return self.changed_graphs

    def set_changed_graphs(self, changed_graphs):
        self.changed_graphs = changed_graphs

    def add_changed_graph(self, changed_graph):
        self.changed_graphs.insert(changed_graph)


filtered_store = FilteredStore()
