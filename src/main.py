import sys
from PyQt5.QtWidgets import QApplication
from src.views.central import Central
from src.views.project_window import ProjectWindow
from src.views.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()

# stylesheet = ""
#
# with open("views/resources/stylesheet/design.qss", "r") as f:
#     stylesheet = f.read()
#
# app.setStyleSheet(stylesheet)
window.show()
# start the event loop
app.exec_()
