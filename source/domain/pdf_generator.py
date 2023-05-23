from fpdf import FPDF

from source.domain.utils import extract_files_to_list


class PDF(FPDF):
    def header(self):
        self.image("resources/icons/hexagon.png", 10, 8, 25)

        self.set_font("helvetica",'B', 20)

        self.cell(0,10, 'Graph Filter', border = False, ln=1, align='C')

        self.set_font("helvetica",'B', 14)
        self.cell(0,10,"Information about the filtering", align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)

        self.set_font('helvetica', 'I', 10)

        self.cell(0,10, f'Page {self.page_no()}/{{nb}}', align = 'C')

    def information_about_filtering(self, name,method,equations,conditions,input_files):
        self.set_font('arial','', 12)
        self.cell(0, 10, f"Name: {name}", ln = True)

        #self.multi_cell(0,10,f"Description: {description}")
        self.cell(0,10,f"Methods: {method}", ln = True)
        self.multi_cell(0,10,f"Equations: {' '.join(equations)}", ln=True)
        self.multi_cell(0,10,f"Conditions: {conditions}",ln=True)
        self.cell(0,10,f"Files: {' '.join(input_files)}", ln=True)

    def information_about_graphs(self,graph_files, filtered_graphs):
        g6_list = extract_files_to_list(graph_files)
        percent = ( len(filtered_graphs) / len(g6_list)) * 100
        self.set_fill_color(200,220,255)
        self.cell(0,10,f"Number of inputted graphs: {len(g6_list)}", ln=True)
        self.cell(0,10,f"Number of filtered graphs: {len(filtered_graphs)}", ln=True)
        self.cell(0,10,f"Percentage of success: {round(percent)}%")