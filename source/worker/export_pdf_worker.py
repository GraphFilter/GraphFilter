from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os
from source.domain import Parameters


class ExportPDFWorker:
    def __init__(self, parameters: Parameters, num_filtered_graphs: int, num_input_graphs: int):
        self.parameters = parameters
        self.num_filtered_graphs = num_filtered_graphs
        self.num_input_graphs = num_input_graphs

    def create_document(self):
        output_path = os.path.normpath(self.parameters.location)
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        doc = SimpleDocTemplate(
            output_path + f"\\{self.parameters.name}.pdf",
            pagesize=letter,
            topMargin=1 * inch,
            bottomMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            rightMargin=0.75 * inch
        )
        story = self.build_story()
        doc.build(story)

    def build_story(self):
        elements = []

        elements.extend(self.header())
        elements.extend(self.information_about_filtering())
        elements.extend(self.conditions_table())
        elements.extend(self.additional_information())

        return elements

    def header(self):
        elements = []
        image = self.add_image()
        if image:
            elements.append(image)
        elements.append(Paragraph("Graph Filter", self.get_title_style()))
        elements.append(Paragraph("Information about the filtering", self.get_subtitle_style()))
        elements.append(Paragraph("<br/><br/>", self.get_normal_style()))  # Extra space
        return elements

    def information_about_filtering(self):
        elements = [
            self.create_field_paragraph("Name", self.parameters.name),
            self.create_field_paragraph("Method", self.parameters.method.name)
        ]
        if self.parameters.equation:
            elements.append(self.create_field_paragraph("In (equation)", self.parameters.equation))
        return elements

    def conditions_table(self):
        elements = []
        true_conditions = [cond.name for cond, value in self.parameters.conditions.items() if value]
        false_conditions = [cond.name for cond, value in self.parameters.conditions.items() if not value]

        max_len = max(len(true_conditions), len(false_conditions))

        data = [['True', 'False']]
        for i in range(max_len):
            row = []
            if i < len(true_conditions):
                row.append(true_conditions[i])
            else:
                row.append('')

            if i < len(false_conditions):
                row.append(false_conditions[i])
            else:
                row.append('')

            data.append(row)

        table = Table(data, colWidths=[3.2 * inch, 3.2 * inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))

        elements.append(Paragraph("Conditions:", self.get_bold_style()))
        elements.append(Paragraph("<br/>", self.get_normal_style()))
        elements.append(table)
        elements.append(Paragraph("<br/>", self.get_normal_style()))

        return elements

    def additional_information(self):
        elements = []
        if self.parameters.description.strip():
            elements.append(self.create_field_paragraph("Description", self.parameters.description))
        elements.append(Paragraph("Files:", self.get_bold_style()))
        for file in self.parameters.files:
            elements.append(Paragraph(f"\u2022 {file}", self.get_indented_style()))
        elements.append(self.create_field_paragraph("Number of input graphs", str(self.num_input_graphs)))

        if self.parameters.method.name == 'Filter':
            percent = (self.num_filtered_graphs / self.num_input_graphs) * 100 if self.num_input_graphs > 0 else 0
            elements.append(self.create_field_paragraph("Number of filtered graphs", str(self.num_filtered_graphs)))
            elements.append(self.create_field_paragraph("Percentage of success", f"{percent:.5f}%"))

        return elements

    def create_field_paragraph(self, field_name, field_value):
        return Paragraph(f"<b>{field_name}:</b> {field_value}", self.get_normal_style())

    def get_indented_style(self):
        return ParagraphStyle(
            'Indented',
            parent=self.get_normal_style(),
            leftIndent=0.5 * inch
        )

    @staticmethod
    def get_title_style():
        styles = getSampleStyleSheet()
        return ParagraphStyle(
            'Title',
            parent=styles['Title'],
            fontSize=24,
            alignment=1,
            spaceAfter=0.2 * inch
        )

    @staticmethod
    def get_subtitle_style():
        return ParagraphStyle(
            'Subtitle',
            parent=getSampleStyleSheet()['Normal'],
            fontSize=18,
            alignment=1,
            spaceAfter=0.1 * inch
        )

    @staticmethod
    def get_normal_style():
        return ParagraphStyle(
            'Normal',
            parent=getSampleStyleSheet()['Normal'],
            fontSize=14,
            spaceAfter=0.2 * inch
        )

    @staticmethod
    def get_bold_style():
        return ParagraphStyle(
            'Bold',
            parent=getSampleStyleSheet()['Normal'],
            fontName='Helvetica-Bold',
            fontSize=14
        )

    @staticmethod
    def add_image():
        image_path = "resources/icons/graph_filter_logo.png"
        if os.path.exists(image_path):
            img = Image(image_path)
            img_width, img_height = img.imageWidth, img.imageHeight

            max_width = 5 * inch
            max_height = 1.3 * inch
            if img_width > max_width:
                scale = max_width / img_width
                img_width = max_width
                img_height = img_height * scale
            if img_height > max_height:
                scale = max_height / img_height
                img_height = max_height
                img_width = img_width * scale

            img.drawWidth = img_width
            img.drawHeight = img_height
            return img
        else:
            return None
