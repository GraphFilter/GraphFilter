import logging.config
import os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

os.chdir(root_directory)

config_file_path = os.path.abspath(os.path.join(root_directory, 'config.ini'))
logging.config.fileConfig(config_file_path)
