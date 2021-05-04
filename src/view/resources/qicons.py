from PyQt5.QtGui import QIcon


class Icon(QIcon):
    def __init__(self, name):
        super().__init__()
        self.addFile(f"../resources/icons/{name}.png")