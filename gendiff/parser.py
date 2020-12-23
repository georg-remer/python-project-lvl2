"""Utility parser."""

import argparse


def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.parse_args()
