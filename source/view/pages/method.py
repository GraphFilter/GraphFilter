from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QWizard, QWidget

from source.domain.filter import Filter, FindAnExample
from source.view.elements.buttons.default_button import DefaultButton
from source.view.elements.message_box import MessageBoxDescription
from source.view.pages import WizardPage
from source.view.utils.icons import Icons


class Method(WizardPage):
    def __init__(self):
        super().__init__()

        self.options = self.Options()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setTitle("Method")
        self.setSubTitle(self.subtitle)

    def set_up_layout(self):
        self.setLayout(self.options.layout())

    def set_properties(self) -> None:
        self.wizard().setDefaultProperty(
            self.options.__class__.__name__,
            "method",
            self.options.methodChanged
        )

        self.registerField("method*", self.options)

    def isComplete(self):
        return True if self.field("method") else False

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.HaveHelpButton, True)

    def cleanupPage(self) -> None:
        self.wizard().setOption(QWizard.HaveHelpButton, True)

    class Options(QWidget):
        methodChanged = pyqtSignal()

        def __init__(self):
            super().__init__()

            self.filter_button = DefaultButton(Filter(), Icons.FILTER, 16)
            self.find_example_button = DefaultButton(FindAnExample(), Icons.SEARCH, 16)
            self.setProperty("method", None)

            self.set_content_attributes()
            self.set_up_layout()
            self.connect_buttons()

        def set_content_attributes(self):
            button_stylesheet = "padding-left: 20px; text-align: center;"
            self.filter_button.setStyleSheet(self.filter_button.styleSheet() + button_stylesheet)
            self.find_example_button.setStyleSheet(self.find_example_button.styleSheet() + button_stylesheet)
            self.filter_button.setFixedWidth(400)
            self.find_example_button.setFixedWidth(400)
            self.filter_button.setCheckable(True)
            self.find_example_button.setCheckable(True)

        def set_up_layout(self):
            layout = QVBoxLayout()

            spacer_item_top = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer_item_top)

            button_layout = QVBoxLayout()

            button_layout.addWidget(self.filter_button)
            button_layout.setSpacing(30)
            button_layout.setAlignment(self.filter_button, Qt.AlignHCenter)

            button_layout.addWidget(self.find_example_button)
            button_layout.setAlignment(self.find_example_button, Qt.AlignHCenter)

            layout.addLayout(button_layout)

            spacer_item_bottom = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer_item_bottom)

            self.filter_button.setFocusPolicy(Qt.NoFocus)
            self.find_example_button.setFocusPolicy(Qt.NoFocus)

            self.setLayout(layout)

        def connect_buttons(self):
            self.filter_button.clicked.connect(self.handle_button_click)
            self.find_example_button.clicked.connect(self.handle_button_click)

        def handle_button_click(self):
            button_clicked = DefaultButton().sender()

            other_button = self.find_example_button if button_clicked == self.filter_button else self.filter_button
            other_button.setChecked(False)

            self.setProperty("method", button_clicked.translation_object if button_clicked.isChecked() else None)
            self.methodChanged.emit()

    subtitle = """Choose the filtering method for the project"""

    help_message = MessageBoxDescription(title="What each method does?",
                                         text="""
            <p>
                <dl>
                    <dt><code>Filter Graphs</code></dt>
                    <dd>analyzes each graph and discard from the result list those that do not satisfy the conditions</dd>
                    <dt><code>Find an example</code></dt>
                    <dd>stop the search in the first graph that satisfy the conditions, or when the list ends</dd>
                </dl>
            </p>
                """
                                         )
