"""Test 'gendiff' module."""

import os

import pytest

from gendiff.gendiff import generate_diff

BASE_PATH = 'tests/fixtures'
JSON_PATH = 'json'
YAML_PATH = 'yaml'


@pytest.fixture
def json_files():
    """Return paths to JSON files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, JSON_PATH, 'file1.json')
    file_path2 = os.path.join(BASE_PATH, JSON_PATH, 'file2.json')
    return file_path1, file_path2


@pytest.fixture
def yaml_files():
    """Return paths to YAML files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, YAML_PATH, 'file1.yml')
    file_path2 = os.path.join(BASE_PATH, YAML_PATH, 'file2.yml')
    return file_path1, file_path2


@pytest.fixture
def expected():
    """Return expected output.

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, 'expected.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


def test_generate_diff(json_files, yaml_files, expected):
    """Test 'gendiff.gendiff.generate_diff' function.

    Args:
        json_files: JSON files to compare
        yaml_files: YAML files to compare
        expected: expected output
    """
    assert generate_diff(*json_files) == expected
    assert generate_diff(*yaml_files) == expected
