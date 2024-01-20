from unittest.mock import patch

from sandbox import Sandbox
from source.commons.objects.translation_object import TranslationObject
from source.domain.filter import Filter


class SandboxReview(Sandbox):
    def __init__(self):
        super().__init__()
        self.source_path = __file__


if __name__ == '__main__':
    sandbox = SandboxReview()
    sandbox.instantiate_element()

    with patch.object(sandbox.element, 'field', autospec=True, side_effect=[
        "My New Project",
        "root/folder/folder",
        "This project is meant to research graphs given certain conditions",
        "n(G)>0 AND n(G)>3 OR n(G)>50",
        {True: {TranslationObject("a", "b")}, False: {TranslationObject("a", "b")}},
        Filter(),
        [
            "root/folder/folder/file1.txt",
            "root/folder/folder/file2.txt",
            "root/folder/folder/file3.txt",
            "root/folder/folder/file4.txt"
        ],
        "My New Project",
        "root/folder/folder",
    ]):
        sandbox.element.set_up_layout()
        sandbox.start()
