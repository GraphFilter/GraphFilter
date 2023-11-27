import os
import sys
from PyQt5.QtWidgets import QApplication
import multiprocessing as mp

from source.view.windows.wizard_window import WizardWindow

try:
    os.chdir(sys._MEIPASS)
except (OSError, AttributeError) as e:
    pass


if __name__ == '__main__':
    mp.freeze_support()
    app = QApplication(sys.argv)
    wizard = WizardWindow()

    wizard.show()

    app.exec_()
