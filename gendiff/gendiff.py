"""Module gendiff."""

import json
import os

import yaml

from gendiff.constants import STYLISH
from gendiff.formatter import format_diff
from gendiff.parser import construct_diff


def _read(file_path):
    """Read file.

    Args:
        file_path: can be both relative and absolute

    Returns:
        dict

    Raises:
        RuntimeError: unknown file extension
    """
    _, extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file_contents:
        if extension.lower() == '.json':
            return json.load(file_contents)
        if extension.lower() == '.yml':
            return yaml.load(file_contents, Loader=yaml.FullLoader)
        raise RuntimeError(
            "Extension '{ext}' is not implemented".format(ext=extension),
        )


def generate_diff(file_path1, file_path2, style=STYLISH):
    """Generate difference between two files.

    Args:
        file_path1: path to one of the files to compare
        file_path2: path to the other of the files to compare
        style: to be used for result output

    Returns:
        str
    """
    file1 = _read(file_path1)
    file2 = _read(file_path2)
    return format_diff(construct_diff(file1, file2))
