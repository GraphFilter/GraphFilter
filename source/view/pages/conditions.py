from PyQt5.QtWidgets import *

from source.domain.entities.invariants.boolean_spectral_invariants import BOOLEAN_SPECTRAL_INVARIANTS
from source.domain.entities.invariants.boolean_structural_invariants import BOOLEAN_STRUCTURAL_INVARIANTS
from source.view.components.boolean_items_selector import BooleanItemsSelector


class Conditions(QWizardPage):

    def __init__(self):
        super().__init__()

        self.selected_conditions = {}

        self.structural_invariants_group = BooleanItemsSelector(title="Structural", items=BOOLEAN_STRUCTURAL_INVARIANTS)
        self.spectral_invariants_group = BooleanItemsSelector(title="Spectral", items=BOOLEAN_SPECTRAL_INVARIANTS)

        self.set_up_layout()
        self.connect()

    def set_up_layout(self):
        self.setTitle("Conditions")

        layout = QHBoxLayout()
        layout.addWidget(self.structural_invariants_group)
        layout.setSpacing(20)
        layout.addWidget(self.spectral_invariants_group)

        self.setLayout(layout)

    def connect(self):
        self.structural_invariants_group.connect(self.handler)
        self.spectral_invariants_group.connect(self.handler)

    def handler(self):
        name = QRadioButton().sender().parent().item.name
        stats = True if QRadioButton().sender().objectName() == 'true' else False
        if name in self.selected_conditions.keys() and self.selected_conditions[name] is stats:
            del self.selected_conditions[name]
        else:
            self.selected_conditions[name] = stats
        self.completeChanged.emit()

    def isComplete(self):
        return True if self.selected_conditions.keys() else False
