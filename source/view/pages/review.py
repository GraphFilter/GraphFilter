from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from source.commons.objects.translation_object import TranslationObject
from source.view.components.form_template_layout import FormTemplateLayout
from source.view.components.header_label import HeaderLabel
from source.view.components.responsive_layout import ResponsiveLayout
from source.view.components.scroll_area_layout import ScrollAreaLayout
from source.view.elements.caption_container import CaptionContainer
from source.view.elements.chip import Chip
from source.view.elements.file_list import FileList
from source.view.elements.icon_label import IconLabel
from source.view.elements.inputs.read_only_input import ReadOnlyInput
from source.view.items.pair_widgets import PairWidgets
from source.view.items.typography import Code, H4
from source.view.pages import WizardPage
from source.view.utils.button_collection import ButtonCollection
from source.view.utils.colors import Colors
from source.view.utils.icons import Icons


class Review(WizardPage):
    def __init__(self):
        super().__init__()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.setTitle("Review")
        self.setSubTitle(self.subtitle)

    def fill(self) -> QLayout:
        layout = QVBoxLayout()
        layout.addWidget(self.Information(self.field("name"), self.field("location"), self.field("description")))
        layout.addWidget(self.Settings(self.field("equation"), self.field("conditions"), self.field("method")))
        layout.addWidget(self.Input(self.field("files")))
        layout.addWidget(self.Output(self.field("name"), self.field("location")))

        return layout

    def set_up_layout(self):
        scroll_layout = ScrollAreaLayout() if self.layout() is None else self.layout()
        scroll_layout.add_element(self.fill())

        if not self.layout():
            self.setLayout(scroll_layout)

    def isComplete(self):
        return True

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.HaveHelpButton, False)
        self.set_up_layout()

    def cleanupPage(self) -> None:
        self.update()
        self.wizard().setOption(QWizard.HaveHelpButton, True)

    class Information(HeaderLabel):

        def __init__(self, name: str, location: str, description: str):
            layout = QVBoxLayout()

            self.name = CaptionContainer("Project Name", name)
            self.location = CaptionContainer("Project Location", Code(location))
            self.description = CaptionContainer("Project Description", description)

            layout.addWidget(self.name)
            layout.addWidget(self.location)
            if description and description.strip():
                layout.addWidget(self.description)

            super().__init__("Basic Information", layout)

    class Settings(HeaderLabel):

        def __init__(self, equation: str, conditions: Dict[bool, set[TranslationObject]], method: TranslationObject):
            layout = QVBoxLayout()

            if equation:
                layout.addLayout(self.Equation(equation))

            if conditions and len(conditions) != 0:
                layout.addWidget(self.Conditions(conditions))

            super().__init__(f"<p>Settings for method <b><code>{method.name}</code></b></p>", layout)

        class Equation(FormTemplateLayout):
            def __init__(self, equation: str):
                equation_input = ReadOnlyInput()
                equation_input.setText(equation)
                equation_input.setReadOnly(True)
                super().__init__(
                    [
                        PairWidgets(H4("Equation"), equation_input),
                    ]
                )

                self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        class Conditions(QGroupBox):
            def __init__(self, conditions):
                super().__init__()

                self.setLayout(
                    ResponsiveLayout(
                        ButtonCollection().factory(
                            [invariant for invariant, selected in conditions.items() if selected], Chip, Icons.CHECK,
                            background_color=Colors.GREEN()
                        ) +
                        ButtonCollection().factory(
                            [invariant for invariant, selected in conditions.items() if not selected], Chip, Icons.WRONG,
                            background_color=Colors.DARK_RED
                        )
                    )
                )
                self.setTitle("Conditions")

    class Input(HeaderLabel):
        def __init__(self, files: list[str]):
            content = FileList()

            content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            content.add_items(files)
            content.setFixedHeight((content.sizeHintForRow(0) + 1) * content.count())

            super().__init__("Input", content)

    class Output(HeaderLabel):
        def __init__(self, name: str, location: str):
            layout = QVBoxLayout()

            content = FileList()
            content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            content.add_items([f"{location}/{name}.g6", f"{location}/{name}.pdf"])
            content.setFixedHeight((content.sizeHintForRow(0) + content.getContentsMargins()[1] * 2) * content.count())

            layout.addWidget(content)

            label = IconLabel().set_content_attributes(
                    Icons.INFO,
                    """
                            Filtering will generate a <code>g6</code> file with all the resulting graphs and a 
                            <code>pdf</code> with the report
                            """,
                    color=Colors.BLUE_TEXT()
                )
            layout.addWidget(label)

            super().__init__("Output", layout)

    subtitle = """Review all parameters inserted on previous steps."""
