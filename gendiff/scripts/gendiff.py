"""Entry point."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Run gendiff."""
    file_path1, file_path2, format_name = parse_args()
    print(generate_diff(file_path1, file_path2, format_name))


if __name__ == '__main__':
    main()
