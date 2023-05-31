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

    def information_about_filtering(self, name, method, equations, conditions,description, input_files):
        self.add_font('DejaVuSans', '', 'resources/fonts/DejaVuSans.ttf')
        self.set_font('DejaVuSans')
        cond = str(conditions)[1:-1]
        self.cell(0, 10, f"Name: {name}", ln=True)
        self.cell(0, 10, f"Methods: {method}", ln=True)

        if cond == '':
            self.cell(0,10,"Conditions: None",ln=True)
        else:
            self.multi_cell(0, 10, f"Conditions: {cond}", ln=True)
        if equations == '':
            self.cell(0, 10, f"(In)equations: None", ln=True)
        else:
            self.cell(0, 10, f"(In)equations: {equations}", ln=True)
        if description == '':
            self.cell(0,10,"Description: None", ln=True)
        else:
            self.multi_cell(0,10,f"Description: {description.strip()}",ln=True)

        self.cell(0, 10, f"Files: ", ln=True)
        files_txt = ''
        for item in input_files:
            files_txt += item + ', \n'
        self.multi_cell(0, 10, files_txt.strip())
        self.ln()

    def information_about_graphs(self, filtered_graphs, method,num_graphs):
        percent = (len(filtered_graphs) / num_graphs) * 100

        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, f"Number of inputted graphs: {num_graphs}", ln=True)
        if method == 'filter':
            self.cell(0, 10, f"Number of filtered graphs: {len(filtered_graphs)}", ln=True)
            self.cell(0, 10, f"Percentage of success: {round(percent,5)}%")
        else:
            if filtered_graphs >= 0:
                self.cell(0, 10, "An example was found")
            else:
                self.cell(0, 10, "No example found")
