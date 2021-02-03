"""Test 'gendiff' module."""

import pytest

from gendiff.constants import PLAIN
from gendiff.gendiff import generate_diff


def test_generate_diff_plain(
    plain_json_files,
    plain_yaml_files,
    expected_stylish_from_plain,
):
    """Test result for plain files.

    Args:
        plain_json_files: JSON files to compare
        plain_yaml_files: YAML files to compare
        expected_stylish_from_plain: expected output
    """
    assert generate_diff(*plain_json_files) == expected_stylish_from_plain
    assert generate_diff(*plain_yaml_files) == expected_stylish_from_plain


def test_generate_diff_tree(
    tree_json_files,
    tree_yaml_files,
    expected_stylish_from_tree,
    expected_plain_from_tree,
):
    """Test result for tree files.

    Args:
        tree_json_files: JSON files to compare
        tree_yaml_files: YAML files to compare
        expected_stylish_from_tree: expected stylish output
        expected_plain_from_tree: expected plain output
    """
    assert generate_diff(*tree_json_files) == expected_stylish_from_tree
    assert generate_diff(*tree_yaml_files) == expected_stylish_from_tree
    assert generate_diff(
        *tree_json_files, style=PLAIN,
    ) == expected_plain_from_tree
    assert generate_diff(
        *tree_yaml_files, style=PLAIN,
    ) == expected_plain_from_tree
