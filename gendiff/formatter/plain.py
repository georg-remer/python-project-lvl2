"""Plain formatter."""

from gendiff.constants import CHANGED, NEW, REMOVED
from gendiff.formatter.common import stringify


def _generate_line(key, state, old_value=None, new_value=None):
    """Generate line according to node state.

    UNCHANGED state is not added to output in plain formatter,
    so this condition is not checked explicitly

    Args:
        key: node key
        state: node state
        old_value: old node value
        new_value: new node value

    Returns:
        str
    """
    if state == NEW:
        return "Property '{0}' was added with value: {1}".format(
            key, new_value,
        )
    if state == REMOVED:
        return "Property '{0}' was removed".format(key)
    if state == CHANGED:
        return "Property '{0}' was updated. From {1} to {2}".format(
            key, old_value, new_value,
        )
    return ''


def _process(value):
    """Process value.

    Return '[complex value]' if value is not primitive, otherwise
    stringify and return passed value

    Args:
        value: to be processed

    Returns:
        str
    """
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, str):
        return "'{0}'".format(value)
    return stringify(value)


def format_plain(diff, path=''):
    """Format diff to plain output.

    Args:
        diff: to be formatted
        path: for the nested structure

    Returns:
        str
    """
    if isinstance(diff, dict):
        key = '{0}.{1}'.format(path, diff['key']) if path else diff['key']
        children = diff.get('children')

        if children:
            return format_plain(children, key)

        state = diff['state']
        new_value = _process(diff.get('new_value'))
        old_value = _process(diff.get('old_value'))

        return _generate_line(key, state, old_value, new_value)

    lines = list(map(lambda element: format_plain(element, path), diff))

    # Exclude empty lines for UNCHANGED nodes
    lines = [line for line in lines if line != '']

    return '\n'.join(lines)
