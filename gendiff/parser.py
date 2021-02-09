"""File parser."""

import json

import yaml


def parse(data, format_name):
    """Parse data based on file format.

    Args:
        data: file contents
        format_name: file format

    Returns:
        dict

    Raises:
        RuntimeError: unknown file format
    """
    if format_name == 'json':
        return json.load(data)
    if format_name in {'yml', 'yaml'}:
        return yaml.load(data, Loader=yaml.FullLoader)
    raise RuntimeError(
        "Unknown file format: '{format}'!".format(format=format_name),
    )
