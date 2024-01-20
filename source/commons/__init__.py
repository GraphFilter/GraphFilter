import os
import re
from typing import Dict


def calculate_string_difference(first_string: str, second_string: str) -> str:
    if second_string in first_string:
        return first_string.replace(second_string, '')
    if first_string in second_string:
        return second_string.replace(first_string, '')
    return first_string


def validate_file_name(name):
    forbidden_chars = ['?', '\\', '/', ':', '*', '"', '<', '>', '|', "'"]
    return not any(substring in name for substring in forbidden_chars) and len(name) > 0


def validate_path(path):
    forbidden_chars = ['.', '\\', ":"]
    if len(path) != 0:
        if path[0] in forbidden_chars:
            return False
        if path[len(path) - 1] in forbidden_chars:
            try:
                open(path + "/verify.txt", "x")
                os.remove(path + "/verify.txt")
            except IOError:
                return False
    return os.path.isdir(path)


def empty_values(dictionary: Dict[bool, set]):
    if dictionary is not None:
        for value in dictionary.values():
            if isinstance(value, set) and len(value) > 0:
                return False
    return True


def split_camel_case(name):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
