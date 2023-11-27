from PyQt5.QtWidgets import QScrollArea, QSizePolicy, QVBoxLayout, QLayout, QWidget, QFrame


class ScrollAreaLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.scroll_area = QScrollArea()

        self.set_content_attributes()

    def set_content_attributes(self):
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def add_element(self, element: QWidget | QLayout):
        if isinstance(element, QLayout):
            widget_aux = QWidget()
            widget_aux.setLayout(element)
            self.scroll_area.setWidget(widget_aux)
            self.addWidget(self.scroll_area)
        elif isinstance(element, QWidget):
            self.scroll_area.setWidget(element)
            self.addWidget(self.scroll_area)

    def set_minimum_width(self, value: int):
        self.scroll_area.setMinimumWidth(value)
