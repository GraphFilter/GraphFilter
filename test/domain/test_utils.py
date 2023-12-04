import unittest
from source.domain.utils import *
from PyQt5.QtCore import QStandardPaths as Qs


class TestUtils(unittest.TestCase):

    def test_should_not_fail_validate_path(self):
        self.assertTrue(validate_path(Qs.writableLocation(Qs.DocumentsLocation)))

    def test_should_fail_validate_empty_path(self):
        self.assertFalse("")

    def test_should_fail_validate_path_starts_dot(self):
        self.assertFalse(validate_path("." + Qs.writableLocation(Qs.DocumentsLocation)))

    def test_should_fail_validate_path_ends_dots(self):
        self.assertFalse(validate_path(Qs.writableLocation(Qs.DocumentsLocation) + ".."))
