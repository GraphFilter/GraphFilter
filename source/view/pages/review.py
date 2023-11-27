from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from source.domain.entities.invariants.boolean_spectral_invariants import BOOLEAN_SPECTRAL_INVARIANTS
from source.domain.entities.invariants.boolean_structural_invariants import BOOLEAN_STRUCTURAL_INVARIANTS
from source.view.components.form_template_layout import FormTemplateLayout
from source.view.components.header_label import HeaderLabel
from source.view.components.responsive_layout import ResponsiveLayout
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.elements.buttons import ListButton
from source.view.elements.caption_container import CaptionContainer
from source.view.elements.chip import Chip
from source.view.elements.file_list import FileList
from source.view.items.typography import H4
from source.view.utils.PairWidgets import PairWidgets
from source.view.utils.constants.colors import Colors


class Review(QWizardPage):

    def __init__(self):
        super().__init__()

        self.basic_information = self.basic_information()
        self.filtering_information = self.filtering_information()
        self.input = self.input()
        self.output = self.output()

        self.set_up_layout()

    def basic_information(self):
        scroll_area_layout = ScrollAreaLayout()

        inside = QVBoxLayout()

        inside.addWidget(CaptionContainer("Project Name", "asdkjhaoisdha"))
        inside.addWidget(CaptionContainer("Project Location", "asdkjhaoisdha"))
        inside.addWidget(CaptionContainer("Project Description", "asdkjhaoisdha"))

        scroll_area_layout.add_element(inside)

        return HeaderLabel("Basic Information", scroll_area_layout)

    def input(self):
        inside = FileList()

        inside.add_items(["asdkjhaoisdha", "asdkjhaoisdha1", "asdkjhaoisdha2", "asdkjhaoisdha3", "asdkjhaoisdha4"])

        return HeaderLabel("Input", inside)

    def output(self):
        inside = FileList()

        inside.add_items(["asdkjhaoisdha", "asdkjhaoisdha1"])

        return HeaderLabel("Output", inside)

    def filtering_information(self):
        scroll_area_layout = ScrollAreaLayout()

        fields = [
            PairWidgets(H4("Method"), QLabel("Filter Graphs")),
            PairWidgets(H4("Equation"), QLabel("A")),
        ]

        inside = FormTemplateLayout(fields)
        inside.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        vlayout = QVBoxLayout()

        vlayout.addLayout(ResponsiveLayout(
            ListButton().factory(BOOLEAN_STRUCTURAL_INVARIANTS, Chip, background_color=Colors.DARK_RED) +
            ListButton().factory(BOOLEAN_SPECTRAL_INVARIANTS, Chip, background_color=Colors.DARK_GREEN)))
        conditions = QGroupBox()
        conditions.setLayout(vlayout)
        conditions.setTitle("Conditions")
        scroll_area_layout.add_element(conditions)

        layout = QVBoxLayout()
        layout.addLayout(inside)
        layout.addLayout(scroll_area_layout)

        return HeaderLabel("Filtering Information", layout)

    def set_up_layout(self):
        self.setTitle("Review")

        layout = QHBoxLayout()

        layout.addWidget(self.basic_information, stretch=1)
        layout.addWidget(self.filtering_information, stretch=2)

        vlayout = QVBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addWidget(self.input, stretch=2)

        vlayout.addWidget(self.output, stretch=1)

        self.setLayout(vlayout)

    def isComplete(self):
        return True
