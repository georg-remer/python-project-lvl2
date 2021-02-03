"""Parser module."""

from gendiff.constants import CHANGED, NEW, REMOVED, UNCHANGED


def _get_unique_keys(dict1, dict2):
    """Get unique keys from dictionaries.

    Args:
        dict1: one dict to extract keys from
        dict2: the other dict to extract keys from

    Returns:
        list
    """
    return sorted({*dict1.keys(), *dict2.keys()})


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
            keys = _get_unique_keys(value1, value2)
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
