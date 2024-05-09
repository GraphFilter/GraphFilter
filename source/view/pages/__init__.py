from PyQt5.QtWidgets import QWizardPage


class WizardPage(QWizardPage):
    def __init__(self):
        super().__init__()

    def setTitle(self, title: str) -> None:
        super().setTitle(f"<h2>{title}</h2>")

    def setSubTitle(self, sub_title: str) -> None:
        super().setSubTitle(f"<font size='3'>{sub_title}</font>")

    def set_properties(self):
        pass

    def validatePage(self) -> bool:
        return self.isComplete()
