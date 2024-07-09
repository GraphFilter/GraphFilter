from PyQt6.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout, QLayout

from source.view.utils.colors import Colors


class HeaderLabel(QWidget):

    def __init__(self, title: str, body: QLayout | QWidget):
        """
        This widget is designed to combine a header and a body widget within a vertical layout.
        It provides a convenient way to organize and display a title along with additional content.

        :param title: The title to be displayed in the header.
        :type title: str
        :param body: The widget representing the body or content below the header.
        :type body: QWidget
        """
        super().__init__()

        self.header = self.Header(title)
        self.body = self.Body(body)

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
            self.setFixedHeight(45)
            self.setStyleSheet(
                f"""
                    Header{{
                            background-color: {Colors.GRAY()};
                            border: 1px solid {Colors.BORDER()}; 
                            border-top-left-radius: 5px;
                            border-top-right-radius: 5px;
                    }}
                """
            )

    class Body(QGroupBox):
        def __init__(self, element):
            super().__init__()
            self.setStyleSheet(
                f"""
                    Body{{
                            background: transparent; 
                            border: 1px solid {Colors.BORDER()}; 
                            border-top: 0px;
                    }}
                """
            )

            self.setFlat(True)
            self.add_element(element)

        def add_element(self, element):
            if isinstance(element, QLayout):
                self.setLayout(element)
            elif isinstance(element, QWidget):
                layout = QVBoxLayout()
                layout.addWidget(element)
                self.setLayout(layout)
