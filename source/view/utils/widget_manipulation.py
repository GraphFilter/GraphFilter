from PyQt5.QtWidgets import QWidget, QLayout


def clear_layout_recursively(layout: QLayout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            delete_widget(item.widget())
        elif item.layout():
            clear_layout_recursively(item.layout())


def delete_widget(item: QWidget):
    fake_widget = QWidget()
    item.setParent(fake_widget)
    item.deleteLater()
    fake_widget.deleteLater()
