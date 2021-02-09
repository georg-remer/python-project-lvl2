"""Stylish formatter."""

from gendiff.formatters.common import stringify
from gendiff.tree import CHANGED, NEW, REMOVED, UNCHANGED

STYLISH_LINE = '{0}{1}: {2}'


def _generate_line(key, state, depth, old_value=None, new_value=None):
    """Generate line according to node state.

    Args:
        key: node key
        state: node state
        depth: the line is generated at
        old_value: old node value
        new_value: new node value

    Returns:
        str
    """
    if state == NEW:
        tab = _get_tab(depth, insert='+')
        return STYLISH_LINE.format(tab, key, new_value)

    if state == REMOVED:
        tab = _get_tab(depth, insert='-')
        return STYLISH_LINE.format(tab, key, old_value)

    if state == UNCHANGED:
        tab = _get_tab(depth)
        return STYLISH_LINE.format(tab, key, old_value)

    if state == CHANGED:
        old_tab = _get_tab(depth, insert='-')
        new_tab = _get_tab(depth, insert='+')
        return '{0}{1}{2}'.format(
            STYLISH_LINE.format(old_tab, key, old_value),
            '\n',
            STYLISH_LINE.format(new_tab, key, new_value),
        )


def _get_tab(depth, insert=None):
    """Return formatted tab.

    Args:
        depth: the tab will be used at
        insert: symbol to be inserted into tab

    Returns:
        str
    """
    tab = '    ' * depth
    if insert == '+':
        return '{0}+{1}'.format(tab[:-2], tab[-1:])
    if insert == '-':
        return '{0}-{1}'.format(tab[:-2], tab[-1:])
    return tab


def _process(value, depth):
    """Process value.

    Case when value is list, pass it to 'format_stylish' to generate
    output, otherwise stringify and return passed value

    Args:
        value: to be processed
        depth: the value is processed at

    Returns:
        str
    """
    if isinstance(value, list):
        return format_stylish(value, depth)
    return stringify(value)


def format_stylish(diff, depth=0):
    """Format diff to stylish output.

    Args:
        diff: to be formatted
        depth: for the nested structure

    Returns:
        str
    """
    if isinstance(diff, dict):
        key = diff['key']
        children = diff.get('children')

        if children:
            tab = _get_tab(depth)
            value = format_stylish(children, depth)
            return STYLISH_LINE.format(tab, key, value)

        state = diff['state']
        new_value = _process(diff.get('new_value'), depth)
        old_value = _process(diff.get('old_value'), depth)

        return _generate_line(key, state, depth, old_value, new_value)

    lines = ['{']
    lines.extend(
        list(map(lambda element: format_stylish(element, depth + 1), diff)),
    )
    lines.append('{0}{1}'.format(_get_tab(depth), '}'))

    return '\n'.join(lines)
