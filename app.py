import os
import sys
from PyQt5.QtWidgets import QApplication
from source.controller.controller import Controller
import multiprocessing as mp

try:
    os.chdir(sys._MEIPASS)
except (OSError, AttributeError) as e:
    pass

if __name__ == '__main__':
    mp.freeze_support()
    app = QApplication(sys.argv)
    controller = Controller()

    controller.show_welcome_window()

    app.exec_()
