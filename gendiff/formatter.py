"""Formatter choice."""

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'


def format_diff(diff, style):
    """Format diff using passed style.

    Return 'stylish' as default format

    Args:
        diff: difference tree
        style: formatting style

    Returns:
        str
    """
    if style == JSON:
        return format_json(diff)
    if style == PLAIN:
        return format_plain(diff)
    return format_stylish(diff)
