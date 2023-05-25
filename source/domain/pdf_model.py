from fpdf import FPDF

from source.domain.utils import extract_files_to_list


class PDF(FPDF):
    def header(self):
        self.image("resources/icons/hexagon.png", 10, 8, 25)

        self.set_font("Helvetica", 'B', 20)

        self.cell(0, 10, 'Graph Filter', border=False, ln=1, align='C')

        self.set_font("Helvetica", 'B', 14)
        self.cell(0, 10, "Information about the filtering", align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)

        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def information_about_filtering(self, name, method, equations, conditions, input_files):
        self.add_font('DejaVuSans', '', 'resources/fonts/DejaVuSans.ttf')
        self.set_font('DejaVuSans')
        self.cell(0, 10, f"Name: {name}", ln=True)

        self.cell(0, 10, f"Methods: {method}", ln=True)

        self.multi_cell(0, 10, f"Conditions: {conditions}", ln=True)

        self.cell(0, 10, f"Equations: {equations}", ln=True)

        self.cell(0, 10, f"Files: ", ln=True)
        files_txt = ''
        for item in input_files:
            files_txt += item + ', \n'
        self.multi_cell(0, 10, files_txt.strip())
        self.ln()

    def information_about_graphs(self, graph_files, filtered_graphs, method):
        g6_list = extract_files_to_list(graph_files)
        percent = (len(filtered_graphs) / len(g6_list)) * 100

        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, f"Number of inputted graphs: {len(g6_list)}", ln=True)
        if method == 'filter':
            self.cell(0, 10, f"Number of filtered graphs: {len(filtered_graphs)}", ln=True)
            self.cell(0, 10, f"Percentage of success: {round(percent,5)}%")
        else:
            if filtered_graphs >= 0:
                self.cell(0, 10, "An example was found")
            else:
                self.cell(0, 10, "No example found")
