from PyQt6.QtWidgets import QSplashScreen

from source.view.items.logo import SoftwareLogo


class Splash(QSplashScreen):
    def __init__(self):
        super().__init__(SoftwareLogo(300, 300).pixmap)
