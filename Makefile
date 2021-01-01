install:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl