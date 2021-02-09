"""Diff generator."""

import os

from gendiff.formatter import STYLISH, format_diff
from gendiff.parser import parse
from gendiff.tree import build_diff


def get_format(file_path):
    """Return file format based on its extension.

    Args:
        file_path: file path, containing filename with extension

    Returns:
        str
    """
    _, extension = os.path.splitext(os.path.abspath(file_path))
    return extension.lower()[1:]


def read(file_path):
    """Read file.

    Args:
        file_path: can be both relative and absolute

    Returns:
        dict
    """
    format_name = get_format(os.path.abspath(file_path))
    with open(file_path, 'r') as contents:
        return parse(contents, format_name)


def generate_diff(file_path1, file_path2, style=STYLISH):
    """Generate difference between two files.

    Args:
        file_path1: path to one of the files to compare
        file_path2: path to the other of the files to compare
        style: to be used for result output

    Returns:
        str
    """
    file1 = read(file_path1)
    file2 = read(file_path2)
    return format_diff(build_diff(file1, file2), style)
