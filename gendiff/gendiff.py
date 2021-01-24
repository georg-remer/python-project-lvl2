"""Module gendiff."""

import json
import os

import yaml

NEW = 'new'
CHANGED = 'changed'
REMOVED = 'removed'
UNCHANGED = 'unchanged'


def _compare_values(value1, value2):
    """Compare two values.

    Return:
    1. NEW if value1 is None and value2 is stated
    2. CHANGED if both value1 and value2 are stated, but are different
    3. REMOVED if value1 is stated, but value2 is None
    4. UNCHANGED if both values are equal

    Args:
        value1: one value to be compared
        value2: the other value to be compared

    Returns:
        str
    """
    if value1 is None and value2 is not None:
        return NEW
    if value1 is not None and value2 is None:
        return REMOVED
    if value1 != value2:
        return CHANGED
    return UNCHANGED


def _get_unique_keys(dict1, dict2):
    """Get unique keys from dictionaries.

    Args:
        dict1: one dict to extract keys from
        dict2: the other dict to extract keys from

    Returns:
        list
    """
    return sorted({*dict1.keys(), *dict2.keys()})


def _stringify(raw_value):
    """Return text representation of value.

    Args:
        raw_value: to be converted

    Returns:
        str
    """
    if raw_value is True:
        return 'true'
    if raw_value is False:
        return 'false'
    return raw_value


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


def generate_diff(file_path1, file_path2):
    """Generate difference between two files.

    Generated difference consists of alphabatically sorted keys with
    values and a corresponding sign:
    1. '+' sign corresponds to new or changed key;
    2. '-' sign corresponds to removed key
    3. no sign - key is present in both files and stays unchanged

    Args:
        file_path1: one file to be compared
        file_path2: the other file to be compared

    Returns:
        str
    """
    file1 = _read(file_path1)
    file2 = _read(file_path2)
    keys = _get_unique_keys(file1, file2)
    diff = ['{']
    for key in keys:
        value1 = _stringify(file1.get(key))
        value2 = _stringify(file2.get(key))
        state = _compare_values(value1, value2)
        if state == NEW:
            diff.append('  + {0}: {1}'.format(key, value2))
        elif state == CHANGED:
            diff.append('  - {0}: {1}'.format(key, value1))
            diff.append('  + {0}: {1}'.format(key, value2))
        elif state == REMOVED:
            diff.append('  - {0}: {1}'.format(key, value1))
        elif state == UNCHANGED:
            diff.append('    {0}: {1}'.format(key, value1))
    diff.append('}')
    return '\n'.join(diff)
