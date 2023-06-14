from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


class Icon(QIcon):
    def __init__(self, name):
        super().__init__()
        self.addFile(f"resources/icons/{name}.png")

class Logo(QPixmap):
    def __init__(self, name):
        super().__init__()
        self.addFile(f"resources/logos/{name}.png")
