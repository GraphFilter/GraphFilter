import sys
from PyQt5.QtWidgets import QApplication
from src.controller.controller import Controller


app = QApplication(sys.argv)
controller = Controller()

controller.show_welcome_window()

app.exec_()
