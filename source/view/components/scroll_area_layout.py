from PyQt5.QtWidgets import QScrollArea, QSizePolicy, QVBoxLayout, QLayout, QWidget, QFrame


class ScrollAreaLayout(QVBoxLayout):
    def __init__(self):
        """
        This layout is designed to organize and display other widgets in a scrollable area.
        It displays the scrollBar only when needed.
        """
        super().__init__()
        self.scroll_area = QScrollArea()
        self.element_layout = None

        self._set_content_attributes()

    def _set_content_attributes(self):
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def add_element(self, element: QWidget | QLayout):
        if isinstance(element, QLayout):
            self.element_layout = element
            widget_aux = QWidget()
            widget_aux.setLayout(element)
            self.scroll_area.setWidget(widget_aux)
            self.addWidget(self.scroll_area)
        elif isinstance(element, QWidget):
            self.scroll_area.setWidget(element)
            self.addWidget(self.scroll_area)

    def set_minimum_width(self, value: int):
        self.scroll_area.setMinimumWidth(value)
