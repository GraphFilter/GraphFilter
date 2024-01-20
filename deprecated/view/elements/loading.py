from PyQt5.QtGui import QMovie


class Loading(QMovie):

    def __init__(self):
        super().__init__()
        self.setFileName(f"resources/gifs/loading.gif")

    def start_animation(self):
        self.start()
