"""Stylish formatter."""

from gendiff.constants import CHANGED, NEW, REMOVED, UNCHANGED
from gendiff.formatter.common import stringify


def _get_tab(depth, include=None):
    tab = '    ' * depth
    if include == '+':
        return '{0}+{1}'.format(tab[:-2], tab[-1:])
    if include == '-':
        return '{0}-{1}'.format(tab[:-2], tab[-1:])
    return tab


def format_stylish(diff, depth=0):
    """Format diff to stylish output.

    Args:
        diff: to be formatted
        depth: for the nested structure

    Returns:
        str
    """
    def _process(value, depth):
        if isinstance(value, list):
            return format_stylish(value, depth)
        return stringify(value)

    if isinstance(diff, dict):
        key = diff['key']
        state = diff['state']
        children = diff.get('children')
        new_value = _process(diff.get('new_value'), depth)
        old_value = _process(diff.get('old_value'), depth)
        if state == NEW:
            return '{0}{1}: {2}'.format(
                _get_tab(depth, include='+'), key, new_value,
            )
        if state == REMOVED:
            return '{0}{1}: {2}'.format(
                _get_tab(depth, include='-'), key, old_value,
            )
        if state == UNCHANGED:
            if children:
                return '{0}{1}: {2}'.format(
                    _get_tab(depth), key, format_stylish(children, depth),
                )
            return '{0}{1}: {2}'.format(_get_tab(depth), key, old_value)
        if state == CHANGED:
            return (
                '{0}{1}: {2}'.format(
                    _get_tab(depth, include='-'), key, old_value,
                )
                + '\n'
                + '{0}{1}: {2}'.format(
                    _get_tab(depth, include='+'), key, new_value,
                )
            )
    lines = ['{']
    lines.extend(
        list(map(lambda element: format_stylish(element, depth + 1), diff)),
    )
    lines.append('{0}{1}'.format(_get_tab(depth), '}'))
    return '\n'.join(lines)
