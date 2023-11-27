import multiprocessing as mp
import sys

from PyQt5.QtWidgets import QApplication

from source.controller import Controller
from source.view.elements.splash import Splash

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp.freeze_support()
    splash = Splash()
    splash.show()
    controller = Controller()
    splash.close()
    controller.start()

    app.exec_()
