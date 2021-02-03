"""Fixtures."""

import os

import pytest

BASE_PATH = 'tests/fixtures'
PLAIN_PATH = 'plain'
TREE_PATH = 'tree'
JSON_PATH = 'json'
YAML_PATH = 'yaml'


@pytest.fixture
def plain_json_files():
    """Return paths to plain JSON files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, PLAIN_PATH, JSON_PATH, 'file1.json')
    file_path2 = os.path.join(BASE_PATH, PLAIN_PATH, JSON_PATH, 'file2.json')
    return file_path1, file_path2


@pytest.fixture
def plain_yaml_files():
    """Return paths to plain YAML files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, PLAIN_PATH, YAML_PATH, 'file1.yml')
    file_path2 = os.path.join(BASE_PATH, PLAIN_PATH, YAML_PATH, 'file2.yml')
    return file_path1, file_path2


@pytest.fixture
def plain_expected():
    """Return expected output.

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, PLAIN_PATH, 'expected.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


@pytest.fixture
def tree_json_files():
    """Return paths to tree JSON files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, TREE_PATH, JSON_PATH, 'file1.json')
    file_path2 = os.path.join(BASE_PATH, TREE_PATH, JSON_PATH, 'file2.json')
    return file_path1, file_path2


@pytest.fixture
def tree_yaml_files():
    """Return paths to tree YAML files.

    Returns:
        (str, str)
    """
    file_path1 = os.path.join(BASE_PATH, TREE_PATH, YAML_PATH, 'file1.yml')
    file_path2 = os.path.join(BASE_PATH, TREE_PATH, YAML_PATH, 'file2.yml')
    return file_path1, file_path2


@pytest.fixture
def tree_expected():
    """Return expected output.

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, TREE_PATH, 'expected.txt')
    with open(pathname, 'r') as opened:
        return opened.read()
