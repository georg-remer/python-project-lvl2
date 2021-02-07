"""Difference tree constructor."""

from gendiff.constants import CHANGED, NEW, REMOVED, UNCHANGED
from gendiff.formatter import STYLISH, format_diff
from gendiff.parser import parse_file


def construct_diff(file1, file2):
    """Compare structures and construct diff.

    Args:
        file1: one dictionary to be compared
        file2: the other dictionary to be compared

    Returns:
        list
    """
    def _process(value):
        if isinstance(value, dict):
            return iterate(value, value)
        return value

    def iterate(value1, value2, key=None, structure1=None, structure2=None):
        if isinstance(value1, dict) and isinstance(value2, dict):
            children = []
            keys = sorted({*value1.keys(), *value2.keys()})
            structure1 = value1
            structure2 = value2
            for unique_key in keys:
                value1 = structure1.get(unique_key)
                value2 = structure2.get(unique_key)
                children.append(
                    (value1, value2, unique_key, structure1, structure2),
                )
            if key:
                return {
                    'key': key,
                    'state': UNCHANGED,
                    'children': list(
                        map(lambda child: iterate(*child), children),
                    ),
                }
            return list(map(lambda child: iterate(*child), children))
        if key in structure1 and key not in structure2:
            return {
                'key': key,
                'state': REMOVED,
                'old_value': _process(value1),
                'new_value': None,
            }
        if key in structure2 and key not in structure1:
            return {
                'key': key,
                'state': NEW,
                'old_value': None,
                'new_value': _process(value2),
            }
        if value1 == value2:
            return {
                'key': key,
                'state': UNCHANGED,
                'old_value': value1,
                'new_value': value2,
            }
        if value1 != value2:
            return {
                'key': key,
                'state': CHANGED,
                'old_value': _process(value1),
                'new_value': _process(value2),
            }
    return iterate(file1, file2)


def generate_diff(file_path1, file_path2, style=STYLISH):
    """Generate difference between two files.

    Args:
        file_path1: path to one of the files to compare
        file_path2: path to the other of the files to compare
        style: to be used for result output

    Returns:
        str
    """
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = construct_diff(file1, file2)
    return format_diff(diff, style)
