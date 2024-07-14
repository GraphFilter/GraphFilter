from PyQt6.QtGui import QPalette


def is_dark_theme() -> bool:
    theme_color = QPalette().window().color()
    return True if theme_color.value() < 128 else False


class Colors:
    LIGHT_GRAY = "#f8f8f8"
    DARK_GRAY = "#636363"

    LIGHT_TEXT = "#CCCCCC"
    DARK_TEXT = "#333333"

    LIGHT_RED = "#ef9a9a"
    LIGHT_BLUE = "#90caf9"
    LIGHT_GREEN = "#a5d6a7"
    LIGHT_YELLOW = "#fff59d"
    LIGHT_ORANGE = "#ffb74d"
    LIGHT_PURPLE = "#b39ddb"

    DARK_RED = "#b71c1c"
    DARK_BLUE = "#0d47a1"
    DARK_GREEN = "#1b5e20"
    DARK_YELLOW = "#fbc02d"
    DARK_ORANGE = "#e65100"
    DARK_PURPLE = "#4a148c"

    BORDER = staticmethod(lambda: Colors.DARK_GRAY if is_dark_theme() else Colors.LIGHT_TEXT)

    GRAY = staticmethod(lambda: Colors.DARK_GRAY if is_dark_theme() else Colors.LIGHT_GRAY)

    TEXT = staticmethod(lambda: Colors.LIGHT_TEXT if is_dark_theme() else Colors.DARK_TEXT)

    RED_TEXT = staticmethod(lambda: Colors.LIGHT_RED if is_dark_theme() else Colors.DARK_RED)
    BLUE_TEXT = staticmethod(lambda: Colors.LIGHT_BLUE if is_dark_theme() else Colors.DARK_BLUE)
    GREEN_TEXT = staticmethod(lambda: Colors.LIGHT_GREEN if is_dark_theme() else Colors.DARK_GREEN)
    YELLOW_TEXT = staticmethod(lambda: Colors.LIGHT_YELLOW if is_dark_theme() else Colors.DARK_YELLOW)
    ORANGE_TEXT = staticmethod(lambda: Colors.LIGHT_ORANGE if is_dark_theme() else Colors.DARK_ORANGE)
    PURPLE_TEXT = staticmethod(lambda: Colors.LIGHT_PURPLE if is_dark_theme() else Colors.DARK_PURPLE)

    RED = staticmethod(lambda: Colors.DARK_RED if is_dark_theme() else Colors.LIGHT_RED)
    BLUE = staticmethod(lambda: Colors.DARK_BLUE if is_dark_theme() else Colors.LIGHT_BLUE)
    GREEN = staticmethod(lambda: Colors.DARK_GREEN if is_dark_theme() else Colors.LIGHT_GREEN)
    YELLOW = staticmethod(lambda: Colors.DARK_YELLOW if is_dark_theme() else Colors.LIGHT_YELLOW)
    ORANGE = staticmethod(lambda: Colors.DARK_ORANGE if is_dark_theme() else Colors.LIGHT_ORANGE)
    PURPLE = staticmethod(lambda: Colors.DARK_PURPLE if is_dark_theme() else Colors.LIGHT_PURPLE)
