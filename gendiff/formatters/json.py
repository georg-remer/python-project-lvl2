"""JSON formatter."""

import json


def format_json(diff):
    """Format diff to plain output.

    Args:
        diff: to be formatted

    Returns:
        str
    """
    return json.dumps(diff)
