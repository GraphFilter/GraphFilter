import sys
from PyQt5.QtWidgets import QApplication
import os

# NOTE:
#  This code opens project from Wizard
# from src.views.windows.main.index import Index
# app = QApplication(sys.argv)
# window = Index()

# NOTE:
#  This code opens project from Visualize
from src.views.windows.project.project_window import ProjectWindow
app = QApplication(sys.argv)
window = ProjectWindow()
file_dir = os.path.dirname(os.path.realpath('__file__'))
current_file_dir = os.path.join(file_dir, '../../domain/tests/resources/graphs/graphs1.g6').replace('\\', '/')
window.visualize.fill_combo([current_file_dir])
# with open(current_file_dir) as f:
#     for line in f:
#         list.append(line[-2])
# window.visualize.fill_combo(list)

# NOTE:
#  Do not comment the following code
window.show()
# start the event loop
app.exec_()
