import os
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap


script_dir = os.path.dirname(os.path.abspath(__file__))


class Splash(QSplashScreen):
    def __init__(self):
        image_path = os.path.join(script_dir, "../../../resources/logos/graph_filter.png")
        super().__init__(QPixmap(image_path).scaledToWidth(500))
