from PyQt5.QtWidgets import QProgressBar, QApplication


class ProgressBar(QProgressBar):

    def __init__(self):
        super().__init__()
        self.setGeometry(25, 25, 300, 40)

    def increase_step(self, value):
        self.setValue(value)
        QApplication.processEvents()

    def set_maximum(self, value):
        self.setMaximum(value)
