import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Graph Filter")
label = QLabel("Hello World!")
label.setAlignment(Qt.AlignCenter)
window.setCentralWidget(label)
window.show()
# start the event loop
app.exec_()
