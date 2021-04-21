import os


def ValidatePath(path):
    return os.path.isdir(os.path.dirname(path)) #or ispath

def ValidateNameToFile(name):
    return os.path.isdir(os.path.dirname(path))  # or ispath