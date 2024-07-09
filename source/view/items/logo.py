from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QSizePolicy


class Logo(QLabel):
    def __init__(self, file_path: str, width: int = 150, height: int = 150):
        super().__init__()

        self.file_path = file_path

        pixmap = QPixmap(file_path).scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio,
                                           Qt.TransformationMode.SmoothTransformation)

        if not pixmap.isNull():
            self.setPixmap(pixmap)
            self.pixmap = pixmap
        else:
            raise AttributeError("Pixmap is null")


class SoftwareLogo(Logo):
    def __init__(self, width: int = 100, height: int = 100):
        super().__init__("resources/logos/graph_filter.png", width, height)
