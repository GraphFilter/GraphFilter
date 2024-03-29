import sys
from PyQt5.QtWidgets import QApplication
import os

# NOTE:
#  This code opens project from Wizard
# from source.view.windows.welcome.index import Index
# app = QApplication(sys.argv)
# window = Index()

# NOTE:
#  This code opens project from Visualize
from source.view.project.project_window import ProjectWindow
app = QApplication(sys.argv)
window = ProjectWindow()
file_dir = os.path.dirname(os.path.realpath('__file__'))
#current_file_dir = os.path.join(file_dir, '../../domain/tests/resources/graphs/graphs1.g6').replace('\\', '/')
list_graphs = ["L??????????^~@", "K?????????^~", "L???????????~~", "M?????????????~~_"]
window.visualize.fill_combo(list_graphs)
# with open(current_file_dir) as f:
#     for line in f:
#         list.append(line[-2])
# window.visualize.fill_combo(list)

# NOTE:
#  Do not comment the following code
window.show()
# start the event loop
app.exec_()
