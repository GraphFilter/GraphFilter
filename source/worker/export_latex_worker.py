from typing import List
from pylatex import Document, Command, NoEscape
import networkx as nx
from source.domain import Parameters


class ExportLatexWorker:
    def __init__(self, parameters: Parameters, filtered_graphs: List[nx.Graph], num_graphs: int):
        self.doc = Document()
        self.name = parameters.name
        self.method = parameters.method
        self.equation = parameters.equation
        self.conditions = parameters.conditions
        self.description = parameters.description
        self.files = parameters.files
        self.location = parameters.location
        self.filtered_graphs = filtered_graphs
        self.num_graphs = num_graphs
        
        self.create_document()

    def header(self):
        self.doc.preamble.append(Command('usepackage', 'graphicx'))
        self.doc.preamble.append(NoEscape(r'\title{Graph Filter}'))
        self.doc.preamble.append(NoEscape(r'\author{}'))
        self.doc.preamble.append(NoEscape(r'\date{}'))
        self.doc.append(NoEscape(r'\maketitle'))
        self.doc.append(NoEscape(r'\begin{center}\includegraphics[width=0.3\textwidth]{resources/icons/graph_filter_logo.png}\end{center}'))
        self.doc.append(NoEscape(r'\begin{center}\Huge Graph Filter \end{center}'))
        self.doc.append(NoEscape(r'\begin{center}\Large Information about the filtering \end{center}'))
        self.doc.append(NoEscape(r'\vspace{1cm}'))

    def footer(self):
        self.doc.preamble.append(NoEscape(r'\usepackage{fancyhdr}'))
        self.doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
        self.doc.preamble.append(NoEscape(r'\fancyhf{}'))
        self.doc.preamble.append(NoEscape(r'\rfoot{Page \thepage}'))

    def information_about_filtering(self):
        cond = str(self.conditions)[1:-1]
        self.doc.append(NoEscape(r'\section*{Information about the Filtering}'))
        self.doc.append(f"\\textbf{{Name:}} {self.name} \\\\")
        self.doc.append(f"\\textbf{{Methods:}} {self.method} \\\\")
        if cond == '':
            self.doc.append(f"\\textbf{{Conditions:}} None \\\\")
        else:
            self.doc.append(f"\\textbf{{Conditions:}} {cond} \\\\")
        if self.equation == '':
            self.doc.append(f"\\textbf{{(In)equation:}} None \\\\")
        else:
            self.doc.append(f"\\textbf{{(In)equation:}} {self.equation} \\\\")
        if self.description == '':
            self.doc.append(f"\\textbf{{Description:}} None \\\\")
        else:
            self.doc.append(f"\\textbf{{Description:}} {self.description.strip()} \\\\")
        self.doc.append(f"\\textbf{{Files:}} \\\\")
        files_txt = ', \\\\ '.join(self.files)
        self.doc.append(files_txt)

    def information_about_graphs(self):
        percent = (len(self.filtered_graphs) / self.num_graphs) if self.num_graphs > 0 * 100 else 0
        self.doc.append(NoEscape(r'\section*{Information about Graphs}'))
        self.doc.append(f"\\textbf{{Number of input graphs:}} {self.num_graphs} \\\\")
        if self.method == 'filter':
            self.doc.append(f"\\textbf{{Number of filtered graphs:}} {len(self.filtered_graphs)} \\\\")
            self.doc.append(f"\\textbf{{Percentage of success:}} {round(percent, 5)}%")
        else:
            if len(self.filtered_graphs) > 0:
                self.doc.append("An example graph was found.")
            else:
                self.doc.append("No example graphs found.")

    def create_document(self):
        self.header()
        self.footer()
        self.information_about_filtering()
        self.information_about_graphs()

    def generate(self):
        # self.doc.generate_tex(self.location)
        self.doc.generate_pdf(self.location)
