import sys
from PyQt5.QtWidgets import QApplication
from src.views import main_window


app = QApplication(sys.argv)
window = main_window.MainWindow()

window.show()
# start the event loop
app.exec_()
