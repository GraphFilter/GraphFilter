from PyQt6.QtWidgets import QWizard

from source.commons.objects.translation_object import TranslationObject
from source.view.components.file_selection_manager import FileSelectionManager
from source.view.components.group_button import GroupButton
from source.view.elements.buttons.key_button import KeyButton
from source.view.elements.message_box import MessageBoxDescription
from source.view.pages import WizardPage
from source.view.utils.button_collection import ButtonCollection
from source.view.utils.file_types import GraphTypes
from source.view.utils.icons import Icons


class Files(WizardPage):

    def __init__(self):
        super().__init__()

        self.file_selector = FileSelectionManager(GraphTypes(), self.DownloadGraphsButtons())

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setTitle("Files")
        self.setSubTitle(self.subtitle)

    def set_up_layout(self):
        self.setLayout(self.file_selector.layout())

    def set_properties(self) -> None:
        self.wizard().setDefaultProperty(
            self.file_selector.__class__.__name__,
            "files",
            self.file_selector.listChanged
        )

        self.registerField("files*", self.file_selector)

    def isComplete(self):
        return True if self.field("files") else False

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, True)

    def cleanupPage(self) -> None:
        return

    class DownloadGraphsButtons(GroupButton):
        def __init__(self):
            super().__init__(ButtonCollection().factory(
                [TranslationObject(name="By Brandon", code="https://houseofgraphs.org/meta-directory"),
                 TranslationObject(name="House of Graphs",
                                   code="http://users.cecs.anu.edu.au/~bdm/data/graphs.html")],
                KeyButton, Icons.FILE_DOWNLOAD), "Download Graphs")

    subtitle = """Insert files containing the lists of the graphs to be analyzed."""

    help_message = MessageBoxDescription(title="Which files can I add?",
                                         text="""
              <p>
                    The program is capable of load list of graphs contained in graph6 format, stored in files with
                    extension  <code>.txt</code> or <code>.g6</code>.

                    <blockquote>
                        The graph6 format stores the graph in a compact way, allowing thousands of graphs in a
                        single file. Files in this format are text type and contain one line per graph.

                        The <code>.txt</code> format is an alternative form for graph6.
                    </blockquote>

                    It  is also provided two trustable sources for downloading collections of graphs in graph6 format.
                    After downloading, simply add them to the filter.

              </p>
                   """
                                         )
