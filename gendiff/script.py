"""Entry point."""

import argparse
import os

from gendiff.constants import PLAIN, STYLISH
from gendiff.gendiff import generate_diff


def parse_args():
    """Parse arguments.

    Returns:
        (str, str)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        choices=[PLAIN, STYLISH],
        default=STYLISH,
        help='set format of output',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    first_file = os.path.abspath(args.first_file)
    second_file = os.path.abspath(args.second_file)
    format_name = args.format

    return first_file, second_file, format_name


def main():
    """Run gendiff."""
    file_path1, file_path2, format_name = parse_args()
    print(generate_diff(file_path1, file_path2, format_name))


if __name__ == '__main__':
    main()
