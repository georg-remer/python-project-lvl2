"""Common in formatters."""


def stringify(raw_value):
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
