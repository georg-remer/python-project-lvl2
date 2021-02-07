"""File parser."""

import json
import os

import yaml


def parse_file(file_path):
    """Read file and parse its contents.

    Args:
        file_path: can be both relative and absolute

    Returns:
        dict

    Raises:
        RuntimeError: unknown file extension
    """
    _, extension = os.path.splitext(os.path.abspath(file_path))
    with open(file_path, 'r') as file_contents:
        if extension.lower() == '.json':
            return json.load(file_contents)
        if extension.lower() == '.yml':
            return yaml.load(file_contents, Loader=yaml.FullLoader)
        raise RuntimeError(
            "Extension '{ext}' is not implemented".format(ext=extension),
        )
