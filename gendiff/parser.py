"""Utility parser."""

import argparse
import os


def parse_args():
    """Parse arguments.

    Returns:
        (str, str)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    first_file = os.path.abspath(args.first_file)
    second_file = os.path.abspath(args.second_file)

    return first_file, second_file
