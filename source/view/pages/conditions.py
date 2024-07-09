from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QWizard, QHBoxLayout, QRadioButton, QVBoxLayout

from source.domain.entities import BOOLEAN_STRUCTURAL_INVARIANTS, BOOLEAN_SPECTRAL_INVARIANTS
from source.view.components.boolean_items_selector import BooleanItemsSelector
from source.view.elements.icon_label import IconLabel
from source.view.elements.message_box import MessageBoxDescription
from source.view.pages import WizardPage
from source.view.utils.colors import Colors
from source.view.utils.icons import Icons


class Conditions(WizardPage):
    def __init__(self):
        super().__init__()

        self.invariants_boolean_selector = self.InvariantsBooleanSelector()
        self.info_label = self.instance_info_label()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.setTitle("Conditions")
        self.setSubTitle(self.subtitle)

    def set_up_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.invariants_boolean_selector)
        self.setLayout(layout)

    def set_properties(self) -> None:
        self.wizard().setDefaultProperty(
            self.invariants_boolean_selector.__class__.__name__,
            "conditions",
            self.invariants_boolean_selector.conditionsChanged
        )

        self.registerField("conditions*", self.invariants_boolean_selector)

    def isComplete(self) -> bool:
        if len(self.field("conditions")) != 0 or self.field("equation"):
            self.layout().removeWidget(self.info_label)
            self.info_label.deleteLater()
            self.info_label = self.instance_info_label()
            return True

        self.layout().addWidget(self.info_label)
        return False

    def initializePage(self) -> None:
        self.wizard().setOption(QWizard.WizardOption.HaveHelpButton, True)

    @staticmethod
    def instance_info_label() -> IconLabel:
        return IconLabel().set_content_attributes(
            Icons.INFO, "As it has no equation, at least one condition must be selected", color=Colors.BLUE_TEXT()
        )

    class InvariantsBooleanSelector(QWidget):
        conditionsChanged = pyqtSignal()

        def __init__(self):
            super().__init__()
            self.structural_invariants_group = BooleanItemsSelector("Structural", BOOLEAN_STRUCTURAL_INVARIANTS)
            self.spectral_invariants_group = BooleanItemsSelector("Spectral", BOOLEAN_SPECTRAL_INVARIANTS)
            self.selected_conditions = {}
            self.setProperty("conditions", self.selected_conditions)

            self.set_up_layout()
            self.connect_events()

        def set_up_layout(self):
            layout = QHBoxLayout()

            layout.addWidget(self.structural_invariants_group)
            layout.setSpacing(20)
            layout.addWidget(self.spectral_invariants_group)

            self.setLayout(layout)

        def connect_events(self):
            self.structural_invariants_group.connect(self.handler)
            self.spectral_invariants_group.connect(self.handler)

        def handler(self):
            name = QRadioButton().sender().parent().item
            stats: bool = True if QRadioButton().sender().objectName() == 'true' else False

            if name in self.selected_conditions.keys() and self.selected_conditions[name] == stats:
                del self.selected_conditions[name]
            else:
                self.selected_conditions[name] = stats

            self.setProperty("conditions", self.selected_conditions)
            self.conditionsChanged.emit()

    subtitle = """Select invariants to filter graphs"""

    help_message = MessageBoxDescription(title="How the selection of conditions works?",
                                         text="""
            <p>
                The graph conditions can be either:
                 <ul>
                    <li><code>TRUE</code>, if you want that condition to be satisfied</li>
                    <li><code>FALSE</code>, if you want the condition to not be satisfied</li>
                 </ul>
                Blank/Unchecked conditions will not be considered for the filtering.
            </p>
                """
                                         )
