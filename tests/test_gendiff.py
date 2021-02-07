"""Test 'gendiff' module."""

import json
import os

import pytest

from gendiff import generate_diff
from gendiff.formatter import JSON, PLAIN, STYLISH

BASE = 'tests/fixtures'
EXPECTED = 'expected'
PLAIN_PATH = 'plain'
TREE_PATH = 'tree'
JSON1 = 'file1.json'
JSON2 = 'file2.json'
YAML1 = 'file1.yml'
YAML2 = 'file2.yml'
PLAIN_STYLISH = 'plain_stylish.txt'
TREE_STYLISH = 'tree_stylish.txt'
TREE_JSON = 'tree_json.json'
TREE_PLAIN = 'tree_plain.txt'


@pytest.mark.parametrize(
    'path, file1, file2, style, expected',
    [
        (PLAIN_PATH, JSON1, JSON2, None, PLAIN_STYLISH),
        (PLAIN_PATH, YAML1, YAML2, None, PLAIN_STYLISH),
        (PLAIN_PATH, JSON1, JSON2, STYLISH, PLAIN_STYLISH),
        (PLAIN_PATH, YAML1, YAML2, STYLISH, PLAIN_STYLISH),
        (TREE_PATH, JSON1, JSON2, None, TREE_STYLISH),
        (TREE_PATH, YAML1, YAML2, None, TREE_STYLISH),
        (TREE_PATH, JSON1, JSON2, STYLISH, TREE_STYLISH),
        (TREE_PATH, YAML1, YAML2, STYLISH, TREE_STYLISH),
        (TREE_PATH, JSON1, JSON2, JSON, TREE_JSON),
        (TREE_PATH, YAML1, YAML2, JSON, TREE_JSON),
        (TREE_PATH, JSON1, JSON2, PLAIN, TREE_PLAIN),
        (TREE_PATH, YAML1, YAML2, PLAIN, TREE_PLAIN),
    ],
)
def test_generate_diff(path, file1, file2, style, expected):
    """Test 'generate_diff' function.

    Args:
        path: source file path depending on file structure
        file1: one file to compare
        file2: another file to compare
        style: formatting style
        expected: expected result
    """
    file1 = os.path.join(BASE, path, 'file1.json')
    file2 = os.path.join(BASE, path, 'file2.json')
    with open(os.path.join(BASE, EXPECTED, expected), 'r') as opened:
        expected = opened.read()
    if style == JSON:
        expected = json.loads(expected)
        result = generate_diff(file1, file2, style)
        assert json.loads(result) == expected
    elif style:
        assert generate_diff(file1, file2, style) == expected
    else:
        assert generate_diff(file1, file2) == expected
