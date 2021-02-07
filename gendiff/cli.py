"""CLI parser."""

import argparse

from gendiff.formatter import JSON, PLAIN, STYLISH


def parse_args():
    """Parse arguments.

    Returns:
        (str, str)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        choices=[JSON, PLAIN, STYLISH],
        default=STYLISH,
        help='set format of output',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
