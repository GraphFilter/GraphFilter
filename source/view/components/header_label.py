from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout, QLayout


class HeaderLabel(QWidget):

    def __init__(self, title: str, body: QWidget):
        super().__init__()

        self.header = Header(title)
        self.body = Body(body)

        layout = QVBoxLayout()
        layout.addWidget(self.header)
        layout.addWidget(self.body)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)


class Header(QGroupBox):

    def __init__(self, text: str):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        self.setLayout(layout)
        self.setFixedHeight(40)


class Body(QGroupBox):
    def __init__(self, element: QWidget | QLayout):
        super().__init__()
        self.setStyleSheet(
            f"Body {{background: transparent; border: 3px solid {self.palette().color(3).name()}; border-top: 0px;}}")
        self.setFlat(True)
        self.add_element(element)

    def add_element(self, element: QWidget | QLayout):
        if isinstance(element, QLayout):
            self.setLayout(element)
        elif isinstance(element, QWidget):
            layout = QVBoxLayout()
            layout.addWidget(element)
            self.setLayout(layout)
