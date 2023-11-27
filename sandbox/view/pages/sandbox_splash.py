import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from source.view.pages.splash import Splash

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = Splash()
    splash.show()

    timer = QTimer()
    timer.timeout.connect(splash.close)
    timer.timeout.connect(app.quit)
    timer.start(3000)

    sys.exit(app.exec_())
