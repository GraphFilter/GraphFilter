import sys
from PyQt5.QtWidgets import QApplication
from src.view.welcome.welcome_window import WelcomeWindow
from src.controller.welcome_controller import WelcomeController


app = QApplication(sys.argv)
welcome_window = WelcomeWindow()
welcome_controller = WelcomeController(welcome_window)

welcome_controller.show_window()

app.exec_()
