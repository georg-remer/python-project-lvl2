"""Formatter module."""

from gendiff.constants import (
    CHANGED,
    NEW,
    NEW_SIGN,
    OLD_SIGN,
    REMOVED,
    STYLISH,
    STYLISH_LINE,
    UNCHANGED,
)


def _get_tab(depth, include=None):
    tab = '    ' * depth
    if include == NEW_SIGN:
        return tab[:-2] + NEW_SIGN + tab[-1:]
    if include == OLD_SIGN:
        return tab[:-2] + OLD_SIGN + tab[-1:]
    return tab


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
    if raw_value is None:
        return 'null'
    return raw_value


def _to_stylish(diff, depth=0):
    def _process(value, depth):
        if isinstance(value, list):
            return _to_stylish(value, depth)
        return _stringify(value)

    if isinstance(diff, dict):
        key = diff['key']
        state = diff['state']
        children = diff.get('children')
        new_value = _process(diff.get('new_value'), depth)
        old_value = _process(diff.get('old_value'), depth)
        if state == NEW:
            return STYLISH_LINE.format(
                _get_tab(depth, include=NEW_SIGN), key, new_value,
            )
        if state == REMOVED:
            return STYLISH_LINE.format(
                _get_tab(depth, include=OLD_SIGN), key, old_value,
            )
        if state == UNCHANGED:
            if children:
                return STYLISH_LINE.format(
                    _get_tab(depth), key, _to_stylish(children, depth),
                )
            return STYLISH_LINE.format(_get_tab(depth), key, old_value)
        if state == CHANGED:
            return (
                STYLISH_LINE.format(
                    _get_tab(depth, include=OLD_SIGN), key, old_value,
                )
                + '\n'
                + STYLISH_LINE.format(
                    _get_tab(depth, include=NEW_SIGN), key, new_value,
                )
            )
    lines = ['{']
    lines.extend(
        list(map(lambda element: _to_stylish(element, depth + 1), diff)),
    )
    lines.append('{0}{1}'.format(_get_tab(depth), '}'))
    return '\n'.join(lines)


def format_diff(diff, to=STYLISH):
    """Format diff using style (default - 'stylish').

    Args:
        diff: to be formatted
        to: style to be used

    Returns:
        str
    """
    if to == STYLISH:
        return _to_stylish(diff)
