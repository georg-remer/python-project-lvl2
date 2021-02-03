"""Test 'gendiff' module."""


from gendiff.gendiff import generate_diff


def test_generate_diff_plain(
    plain_json_files,
    plain_yaml_files,
    plain_expected,
):
    """Test result for plain files.

    Args:
        plain_json_files: JSON files to compare
        plain_yaml_files: YAML files to compare
        plain_expected: expected output
    """
    assert generate_diff(*plain_json_files) == plain_expected
    assert generate_diff(*plain_yaml_files) == plain_expected


def test_generate_diff_tree(
    tree_json_files,
    tree_yaml_files,
    tree_expected,
):
    """Test result for tree files.

    Args:
        tree_json_files: JSON files to compare
        tree_yaml_files: YAML files to compare
        tree_expected: expected output
    """
    assert generate_diff(*tree_json_files) == tree_expected
    assert generate_diff(*tree_yaml_files) == tree_expected
