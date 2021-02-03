"""Fixtures."""

import os

import pytest

BASE_PATH = 'tests/fixtures'
EXPECTED_PATH = 'expected'
PLAIN_PATH = 'plain'
TREE_PATH = 'tree'
JSON_PATH = 'json'
YAML_PATH = 'yaml'


@pytest.fixture
def expected_plain_from_tree():
    """Return expected output.

    Plain result of comparison of plain files

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, EXPECTED_PATH, 'plain_from_tree.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


@pytest.fixture
def expected_stylish_from_plain():
    """Return expected output.

    Stylish result of comparison of plain files

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, EXPECTED_PATH, 'stylish_from_plain.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


@pytest.fixture
def expected_stylish_from_tree():
    """Return expected output.

    Stylish result of comparison of tree files

    Returns:
        str
    """
    pathname = os.path.join(BASE_PATH, EXPECTED_PATH, 'stylish_from_tree.txt')
    with open(pathname, 'r') as opened:
        return opened.read()


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
