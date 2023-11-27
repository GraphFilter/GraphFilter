import qtawesome
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel


class IconizableLabel(QWidget):

    def __init__(self):
        super().__init__()

        self.icon_label = QLabel()
        self.message_label = QLabel()

        self.set_up_layout()

    def set_content_attributes(self, icon: str, message: str, color: str = None, styles: str = None):
        icon = icon
        message = message
        color = color if color is not None else self.palette().color(QPalette.WindowText).name()

        icon_object = qtawesome.icon(icon, color=color)

        icon_pixmap = icon_object.pixmap(15, 15)
        self.icon_label.setPixmap(icon_pixmap)

        self.message_label.setText(message)

        self.message_label.setStyleSheet(f" color: {color}; {styles}")

    def set_up_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.icon_label)
        layout.addWidget(self.message_label)
        layout.setAlignment(Qt.AlignLeft)
        layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(layout)

    def set_font(self, font: str):
        self.message_label.setFont(font)
