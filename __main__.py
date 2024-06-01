import multiprocessing as mp
import sys

from PyQt5.QtWidgets import QApplication

from source.controller import Controller
from source.view.elements.splash import Splash

if __name__ == '__main__':
    mp.freeze_support()
    app = QApplication(sys.argv)
    splash = Splash()
    splash.show()
    controller = Controller()
    splash.close()
    controller.start()

    app.exec_()
