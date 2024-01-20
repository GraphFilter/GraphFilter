from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel

from source.view.utils.icons import Icons


class IconLabel(QWidget):

    def __init__(self):
        super().__init__()

        self.icon_label = QLabel()
        self.message_label = QLabel()

        self.set_up_layout()

    def set_content_attributes(self, icon: Icons, message: str, color: str = None, styles: str = None):
        message = message

        icon_object = icon(color) if color is not None else icon(self.palette().color(QPalette.WindowText).name())

        self.icon_label.setPixmap(icon_object.pixmap(15, 15))
        self.message_label.setWordWrap(True)

        self.message_label.setText(message)

        self.message_label.setStyleSheet(f" color: {color}; {styles}")

        return self

    def set_up_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.icon_label)
        layout.addWidget(self.message_label, stretch=1)
        layout.setAlignment(Qt.AlignLeft)
        layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(layout)

    def set_font(self, font: str):
        self.message_label.setFont(font)
