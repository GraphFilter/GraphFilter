import sys
from PyQt5.QtWidgets import QApplication
from src.views import main_window


app = QApplication(sys.argv)
window = main_window.MainWindow()

# stylesheet = ""
#
# with open("views/resources/stylesheet/design.qss", "r") as f:
#     stylesheet = f.read()
#
# app.setStyleSheet(stylesheet)
window.show()
# start the event loop
app.exec_()
