import sys
from PyQt5.QtWidgets import QApplication
from src.views.windows.main.index import Index
# from src.views.windows.project.project_window import ProjectWindow

app = QApplication(sys.argv)
window = Index()


# stylesheet = ""
#
# with open("views/resources/stylesheet/design.qss", "r") as f:
#     stylesheet = f.read()
#
# app.setStyleSheet(stylesheet)
window.show()
# start the event loop
app.exec_()
