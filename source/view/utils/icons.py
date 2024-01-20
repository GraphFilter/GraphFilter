import qtawesome

from source.view.utils.colors import Colors

from PyQt5.QtGui import QIcon


class Icons:

    def __call__(self, color: str):
        return self

    @staticmethod
    def _get(name: str, color=Colors.TEXT) -> QIcon:
        icon = qtawesome.icon(name, color=color)
        return QIcon(icon)

    FILE_DOWNLOAD = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.file-download", color))
    FILE = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.file", color))
    INFO = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.info-circle", color))
    CHECK = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.check-circle", color))
    WRONG = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.times-circle", color))
    PLUS = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.plus-circle", color))
    ADD_FOLDER = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.folder-plus", color))
    FILTER = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.filter", color))
    SEARCH = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.search", color))
    SUCCESS = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.check-square", color))
    WARNING = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.exclamation-triangle", color))
    ERROR = staticmethod(lambda color=Colors.TEXT: Icons._get("fa5s.times-circle", color))
