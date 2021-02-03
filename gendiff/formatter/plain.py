"""Plain formatter."""

from gendiff.constants import CHANGED, NEW, REMOVED, UNCHANGED
from gendiff.formatter.common import stringify


def format_plain(diff, path=''):
    """Format diff to plain output.

    Args:
        diff: to be formatted
        path: for the nested structure

    Returns:
        str
    """
    def _process(value):
        if isinstance(value, list):
            return '[complex value]'
        if isinstance(value, str):
            return "'{0}'".format(value)
        return stringify(value)

    if isinstance(diff, dict):
        key = '{0}.{1}'.format(path, diff['key']) if path else diff['key']
        state = diff['state']
        children = diff.get('children')
        new_value = _process(diff.get('new_value'))
        old_value = _process(diff.get('old_value'))

        if state == NEW:
            return "Property '{0}' was added with value: {1}".format(
                key, new_value,
            )
        if state == REMOVED:
            return "Property '{0}' was removed".format(key)
        if state == UNCHANGED:
            if children:
                return format_plain(children, key)
            return ''
        if state == CHANGED:
            return "Property '{0}' was updated. From {1} to {2}".format(
                key, old_value, new_value,
            )
    lines = []
    lines.extend(
        list(map(lambda element: format_plain(element, path), diff)),
    )
    lines = [line for line in lines if line != '']
    return '\n'.join(lines)
