"""Entry point."""

from gendiff.gendiff import generate_diff
from gendiff.parser import parse_args


def main():
    """Run gendiff."""
    file_path1, file_path2 = parse_args()
    print(generate_diff(file_path1, file_path2))


if __name__ == '__main__':
    main()
