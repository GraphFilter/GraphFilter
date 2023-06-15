from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


class Icon(QIcon):
    def __init__(self, name):
        super().__init__()
        self.addFile(f"resources/icons/{name}.png")

@staticmethod
class Logo():
    def get_logo(self, name):
        return f"resources/logos/{name}.png"
