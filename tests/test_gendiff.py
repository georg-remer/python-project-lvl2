"""Test 'gendiff' module."""

import os

import pytest

from gendiff.gendiff import generate_diff

FIXTURES_PATH = 'tests/fixtures'


@pytest.fixture
def first_file():
    """Return path to first file.

    Returns:
        str
    """
    return os.path.join(FIXTURES_PATH, 'file1.json')


@pytest.fixture
def second_file():
    """Return path to second file.

    Returns:
        str
    """
    return os.path.join(FIXTURES_PATH, 'file2.json')


@pytest.fixture
def expected():
    """Return expected output.

    Returns:
        str
    """
    pathname = os.path.join(FIXTURES_PATH, 'expected.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


def test_generate_diff(first_file, second_file, expected):
    """Test 'gendiff.gendiff.generate_diff' function.

    Args:
        first_file: one file to compare against
        second_file: the other file to compare against
        expected: expected ooutput
    """
    assert generate_diff(first_file, second_file) == expected
