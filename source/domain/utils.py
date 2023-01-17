import os
import re
import networkx as nx
import gzip

from PyQt5.QtWidgets import QApplication


def validate_path(path: str) -> bool:
    """Check if the path is valid.

    Parameters
    ---------
    path: str
        User-given project path

    Returns
    -------
    out: boolean
        True if the path is valid, False otherwise

    Notes
    -----
    If the file ends with 2 forbidden characters, a temporary
    file is created to perform the verification.
    """
    forbidden_chars = ['.', '\\', '/', ":"]
    if len(path) != 0:
        if path[0] in forbidden_chars:
            return False
        if path[len(path) - 1] in forbidden_chars:
            try:
                open(path + "/verify.txt", "x")
                os.remove(path + "/verify.txt")
            except IOError:
                return False
    return os.path.isdir(path)  # NOTE: or ispath


def validate_file(path: str) -> bool:
    """Check if the file path is valid.

    Parameters
    ---------
    path: str
        User-given project file path

    Returns
    -------
    out: boolean
        True if the file path is valid, False otherwise
    """
    return os.path.isfile(path)  # NOTE: or ispath


def validate_file_name(name: str) -> bool:
    """Check if the file name is valid.

    Parameters
    ---------
    name: str
        User-given project file name

    Returns
    -------
    out: boolean
        True if the file name has none forbidden character , False otherwise
    """
    forbidden_chars = ['?', '\\', '/', ':', '*', '"', '<', '>', '|', "'"]
    return not any(substring in name for substring in forbidden_chars) and len(name) > 0


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def extract_files_to_list(files: list[str]) -> list[str]:
    """Extracts user-given files to a g6 list.

    Parameters
    ---------
    files: list[str]
        User-given list of files

    Returns
    -------
    out: list[str]
        A g6 list extracted from each file in the file list

    Notes
    -----
    If the file is a .gz, the method also unzip it and
    decode.
    """
    list_g6 = []
    for file in files:
        if file.endswith('.gz'):
            file_unzipped = gzip.open(file, 'r')
            list_g6.extend(file_unzipped.read().decode('utf-8').splitlines())
        else:
            list_g6.extend(open(file, 'r').read().splitlines())
    return list_g6


def match_graph_code(text: str) -> str:
    """Gets a g6 code from the text given by filtered graphs combobox.

    Parameters
    ---------
    text: str
        The text from filtered graphs combobox

    Returns
    -------
    out: str
        A g6 code extracted from text attribute
    """
    pattern = re.compile(r'(Graph \d* - )(.*)')
    match = pattern.match(text)
    return match.group(2)


def convert_g6_to_nx(g6code: str) -> object:
    """Converts a g6 code to a NetworkX format.

    Parameters
    ---------
    g6code: str
        A single g6 code

    Returns
    -------
    out: object
        A NetworkX object
    """
    return nx.from_graph6_bytes(g6code.encode('utf-8'))


def set_view_size(window: object, percentage: float) -> None:
    """Dynamically resizes the window.

    Parameters
    ---------
    window: PyQt5 object
        The object of a PyQt5 window
    percentage: float
        Dynamic mathematical variable that contains the percentage
        in decimal to resize the screen
    """
    screen = QApplication.desktop()
    rect = screen.screenGeometry()
    window.width = int(rect.width() / percentage)
    window.height = int(rect.height() / percentage)
